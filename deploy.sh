#!/usr/bin/env bash
#
# VARNET Xalqaro Biotexnologiyalar Universiteti — serverga yangilanish o'rnatish.
#
# Bitta buyruq bilan: GitHub'dan kodni oladi, kutubxonalarni yangilaydi,
# migratsiyalarni bajaradi, tarjima va statik fayllarni yig'adi va saytni
# qayta ishga tushiradi (cPanel / Passenger).
#
# Ishlatish (server SSH terminalida):
#     cd ~/varnet && ./deploy.sh
#
# Sozlash: yonida `deploy.conf` fayli bo'lsa, undan qiymatlar o'qiladi
# (git'ga yuklanmaydi). Namuna uchun `deploy.conf.example` ga qarang.
#
# MUHIM: `varnet/settings.py` va `.env` fayllari git'da saqlanmaydi va bu
# skript ularga tegmaydi — serverdagi sozlamalar o'z holicha qoladi.

set -uo pipefail

APP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$APP_DIR"

# ── Sozlamalar ────────────────────────────────────────────────────────────
REMOTE="${REMOTE:-origin}"
BRANCH="${BRANCH:-main}"
PYTHON_BIN="${PYTHON_BIN:-}"
RESTART_CMD="${RESTART_CMD:-}"
SKIP_PIP="${SKIP_PIP:-0}"

if [ -f "$APP_DIR/deploy.conf" ]; then
    # shellcheck disable=SC1091
    . "$APP_DIR/deploy.conf"
fi

PROTECTED_FILES=("varnet/settings.py" ".env")
BACKUP_DIR="$APP_DIR/.deploy-backup"

# ── Ko'rinish ─────────────────────────────────────────────────────────────
if [ -t 1 ]; then
    C_OK=$'\033[32m'; C_ERR=$'\033[31m'; C_WARN=$'\033[33m'; C_HEAD=$'\033[1;36m'; C_OFF=$'\033[0m'
else
    C_OK=''; C_ERR=''; C_WARN=''; C_HEAD=''; C_OFF=''
fi

STEP=0
step()  { STEP=$((STEP + 1)); printf '\n%s[%d/8] %s%s\n' "$C_HEAD" "$STEP" "$1" "$C_OFF"; }
ok()    { printf '      %s✓%s %s\n' "$C_OK" "$C_OFF" "$1"; }
warn()  { printf '      %s!%s %s\n' "$C_WARN" "$C_OFF" "$1"; }
fail()  { printf '\n%sXATO:%s %s\n' "$C_ERR" "$C_OFF" "$1" >&2; exit 1; }

run() {
    # Buyruqni bajaradi; xato bo'lsa chiqishni ko'rsatib to'xtaydi.
    local description="$1"; shift
    local output
    if output="$("$@" 2>&1)"; then
        ok "$description"
        [ -n "$output" ] && printf '%s\n' "$output" | sed 's/^/        /'
        return 0
    fi
    printf '%s\n' "$output" | sed 's/^/        /' >&2
    fail "$description — bajarilmadi"
}

# ── 1. Tekshiruvlar ───────────────────────────────────────────────────────
step "Muhitni tekshirish"

[ -f "$APP_DIR/manage.py" ] || fail "manage.py topilmadi. Skript loyiha papkasida turishi kerak."
command -v git >/dev/null 2>&1 || fail "git o'rnatilmagan."
git -C "$APP_DIR" rev-parse --git-dir >/dev/null 2>&1 || fail "Bu papka git repozitoriysi emas."

if [ -z "$PYTHON_BIN" ]; then
    if [ -n "${VIRTUAL_ENV:-}" ] && [ -x "$VIRTUAL_ENV/bin/python" ]; then
        PYTHON_BIN="$VIRTUAL_ENV/bin/python"
    else
        # cPanel "Setup Python App" virtualenv'ni ~/virtualenv/<papka>/<versiya> ga joylaydi.
        PYTHON_BIN="$(ls -1 "$HOME/virtualenv/$(basename "$APP_DIR")"/*/bin/python 2>/dev/null | sort -V | tail -n 1)"
    fi
fi
[ -n "$PYTHON_BIN" ] && [ -x "$PYTHON_BIN" ] || PYTHON_BIN="$(command -v python3 || true)"
[ -n "$PYTHON_BIN" ] || fail "Python topilmadi. deploy.conf ichida PYTHON_BIN=... ni ko'rsating."

ok "papka:  $APP_DIR"
ok "python: $PYTHON_BIN ($("$PYTHON_BIN" -V 2>&1))"
ok "tarmoq: $REMOTE/$BRANCH"

# ── 2. Himoyalangan fayllarni zaxiralash ──────────────────────────────────
step "Sozlama fayllarini zaxiralash"

mkdir -p "$BACKUP_DIR"
for file in "${PROTECTED_FILES[@]}"; do
    if [ -f "$APP_DIR/$file" ]; then
        mkdir -p "$BACKUP_DIR/$(dirname "$file")"
        cp -p "$APP_DIR/$file" "$BACKUP_DIR/$file"
        ok "$file zaxiralandi"
    else
        warn "$file mavjud emas"
    fi
done

# ── 3. GitHub'dan yangilanishni olish ─────────────────────────────────────
step "GitHub'dan kodni olish"

run "git fetch" git fetch --prune "$REMOTE"

CURRENT="$(git rev-parse --short HEAD)"
TARGET="$(git rev-parse --short "$REMOTE/$BRANCH" 2>/dev/null)" \
    || fail "$REMOTE/$BRANCH topilmadi."

if [ "$CURRENT" = "$TARGET" ]; then
    ok "kod allaqachon eng so'nggi holatda ($CURRENT)"
else
    printf '      yangi commitlar:\n'
    git log --oneline --no-decorate "HEAD..$REMOTE/$BRANCH" | sed 's/^/        /'
    run "git reset --hard $REMOTE/$BRANCH" git reset --hard "$REMOTE/$BRANCH"
    ok "$CURRENT -> $TARGET"
fi

# ── 4. Sozlama fayllarini tiklash ─────────────────────────────────────────
step "Sozlama fayllarini tiklash"

for file in "${PROTECTED_FILES[@]}"; do
    if [ ! -f "$APP_DIR/$file" ] && [ -f "$BACKUP_DIR/$file" ]; then
        mkdir -p "$APP_DIR/$(dirname "$file")"
        cp -p "$BACKUP_DIR/$file" "$APP_DIR/$file"
        ok "$file zaxiradan tiklandi"
    fi
done

if [ ! -f "$APP_DIR/varnet/settings.py" ]; then
    cp "$APP_DIR/varnet/settings.example.py" "$APP_DIR/varnet/settings.py"
    warn "varnet/settings.py namunadan yaratildi — uni tekshirib chiqing"
fi
[ -f "$APP_DIR/.env" ] || warn ".env yo'q: SECRET_KEY va ALLOWED_HOSTS o'rnatilganiga ishonch hosil qiling"
ok "serverdagi sozlamalar o'zgarmadi"

# ── 5. Kutubxonalar ───────────────────────────────────────────────────────
step "Kutubxonalarni o'rnatish"

if [ "$SKIP_PIP" = "1" ]; then
    warn "o'tkazib yuborildi (SKIP_PIP=1)"
else
    run "pip install -r requirements.txt" \
        "$PYTHON_BIN" -m pip install --no-cache-dir --disable-pip-version-check -q -r requirements.txt
fi

# ── 6. Ma'lumotlar bazasi ─────────────────────────────────────────────────
step "Migratsiyalarni bajarish"

run "manage.py migrate" "$PYTHON_BIN" manage.py migrate --noinput

# ── 7. Tarjima va statik fayllar ──────────────────────────────────────────
step "Tarjima va statik fayllarni yig'ish"

run "manage.py buildmessages" "$PYTHON_BIN" manage.py buildmessages
run "manage.py collectstatic" "$PYTHON_BIN" manage.py collectstatic --noinput --clear

if ! "$PYTHON_BIN" manage.py check --deploy --fail-level ERROR >/dev/null 2>&1; then
    warn "manage.py check --deploy ogohlantirish berdi (batafsil: $PYTHON_BIN manage.py check --deploy)"
fi

# ── 8. Qayta ishga tushirish ──────────────────────────────────────────────
step "Saytni qayta ishga tushirish"

if [ -n "$RESTART_CMD" ]; then
    run "RESTART_CMD" bash -c "$RESTART_CMD"
else
    # Passenger (cPanel) tmp/restart.txt o'zgarganini ko'rib, jarayonni yangilaydi.
    mkdir -p "$APP_DIR/tmp"
    touch "$APP_DIR/tmp/restart.txt"
    ok "tmp/restart.txt yangilandi (Passenger qayta ishga tushiradi)"
fi

printf '\n%sTayyor.%s Sayt %s holatida ishlamoqda.\n\n' \
    "$C_OK" "$C_OFF" "$(git rev-parse --short HEAD)"
