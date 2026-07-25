/* Varnet Biotech University — umumiy skriptlar.
   Har bir blok o'ziga tegishli element mavjudligini tekshiradi, shuning uchun
   bitta fayl barcha sahifalarda xavfsiz ishlaydi. */

(function () {
    'use strict';

    /* ── Mobil navigatsiya ───────────────────────────────────────── */
    (function mobileNav() {
        const toggle = document.getElementById('navToggle');
        const menu = document.getElementById('navMenu');
        const overlay = document.getElementById('navOverlay');
        const close = document.getElementById('navClose');
        if (!toggle || !menu) return;

        function setOpen(open) {
            menu.classList.toggle('open', open);
            toggle.classList.toggle('active', open);
            toggle.setAttribute('aria-expanded', String(open));
            document.body.classList.toggle('nav-locked', open);
            if (overlay) overlay.classList.toggle('show', open);
        }

        toggle.addEventListener('click', () => setOpen(!menu.classList.contains('open')));
        if (overlay) overlay.addEventListener('click', () => setOpen(false));
        if (close) close.addEventListener('click', () => {
            setOpen(false);
            toggle.focus();
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && menu.classList.contains('open')) {
                setOpen(false);
                toggle.focus();
            }
        });

        // Mobil rejimda dropdownlar akkordeon sifatida ochiladi.
        menu.querySelectorAll('.nav-item > a').forEach((link) => {
            link.addEventListener('click', (e) => {
                if (!isMobileNav()) return;
                const item = link.parentElement;
                if (!item.querySelector('.dropdown')) return;
                e.preventDefault();
                const wasOpen = item.classList.contains('expanded');
                menu.querySelectorAll('.nav-item.expanded').forEach((i) => i.classList.remove('expanded'));
                item.classList.toggle('expanded', !wasOpen);
            });
        });

        // Haqiqiy havolaga o'tilganda menyuni yopamiz. Akkordeon ochadigan ota
        // havolalar bundan mustasno — ular sahifaga o'tmaydi.
        menu.querySelectorAll('a[href]:not([href^="#"])').forEach((link) => {
            const opensAccordion = link.parentElement.classList.contains('nav-item')
                && link.parentElement.querySelector('.dropdown');
            if (opensAccordion) return;

            link.addEventListener('click', () => {
                if (isMobileNav()) setOpen(false);
            });
        });

        function isMobileNav() {
            return window.matchMedia('(max-width: 1200px)').matches;
        }

        window.addEventListener('resize', () => {
            if (!isMobileNav() && menu.classList.contains('open')) setOpen(false);
        });
    })();

    /* ── Til tanlash ─────────────────────────────────────────────── */
    (function langPicker() {
        const dropdown = document.getElementById('langDropdown');
        const menu = document.getElementById('langMenu');
        const arrow = document.getElementById('langArrow');
        if (!dropdown || !menu) return;

        function close() {
            menu.classList.remove('open');
            if (arrow) arrow.style.transform = 'rotate(180deg)';
        }

        window.toggleLangMenu = function () {
            const isOpen = menu.classList.toggle('open');
            if (arrow) arrow.style.transform = isOpen ? 'rotate(0deg)' : 'rotate(180deg)';
        };

        window.setLang = function (event, code, name) {
            event.preventDefault();
            const flag = document.getElementById('activeLangFlag');
            const text = document.getElementById('activeLangText');
            if (flag) flag.src = 'https://flagcdn.com/w20/' + code + '.png';
            if (text) text.textContent = name;
            close();
        };

        document.addEventListener('click', (e) => {
            if (!dropdown.contains(e.target)) close();
        });
    })();

    /* ── Statistika raqamlari animatsiyasi ───────────────────────── */
    (function counters() {
        const nums = document.querySelectorAll('.hm-stat-num[data-target]');
        if (!nums.length || !('IntersectionObserver' in window)) return;

        const format = (n) => n.toLocaleString('uz-UZ').replace(/,/g, ' ');

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                const el = entry.target;
                observer.unobserve(el);

                const target = parseInt(el.dataset.target, 10);
                if (Number.isNaN(target)) return;

                const duration = 1400;
                const start = performance.now();

                (function tick(now) {
                    const progress = Math.min((now - start) / duration, 1);
                    const eased = 1 - Math.pow(1 - progress, 3);
                    el.textContent = format(Math.round(target * eased));
                    if (progress < 1) requestAnimationFrame(tick);
                })(start);
            });
        }, { threshold: 0.4 });

        nums.forEach((n) => observer.observe(n));
    })();

    /* ── Bosh sahifa: yozuv animatsiyasi ─────────────────────────── */
    (function typing() {
        const el = document.getElementById('typed-text');
        if (!el) return;

        const texts = [
            'Innovatsion bilimlar markazi',
            'Zamonaviy tadqiqotlar laboratoriyasi',
            'Barqaror kelajak uchun ilmiy maskani',
            'Biotexnologiya sohasida yetakchi universitet'
        ];
        let textIndex = 0;
        let charIndex = 0;

        function type() {
            const current = texts[textIndex];
            if (charIndex < current.length) {
                el.textContent = current.substring(0, ++charIndex);
                setTimeout(type, 50);
            } else {
                setTimeout(() => {
                    charIndex = 0;
                    textIndex = (textIndex + 1) % texts.length;
                    el.textContent = '';
                    type();
                }, 4000);
            }
        }

        setTimeout(type, 1000);
    })();

    /* ── Kartochkalar filtri + sahifalash (yangiliklar / e'lonlar) ─ */
    function setupCardFilter(options) {
        const cards = document.querySelectorAll(options.cardSelector);
        const buttons = document.querySelectorAll(options.buttonSelector);
        if (!cards.length || !buttons.length) return;

        const PER_PAGE = 8;
        let page = 1;
        let filtered = [...cards];

        const prev = document.getElementById(options.prevId);
        const next = document.getElementById(options.nextId);
        const pageButtons = document.querySelectorAll(options.pageSelector);

        function render() {
            cards.forEach((c) => { c.style.display = 'none'; });
            const start = (page - 1) * PER_PAGE;
            filtered.slice(start, start + PER_PAGE).forEach((c) => { c.style.display = 'block'; });

            const totalPages = Math.max(1, Math.ceil(filtered.length / PER_PAGE));
            pageButtons.forEach((btn) => {
                const p = parseInt(btn.dataset.page, 10);
                btn.classList.toggle('active', p === page);
                btn.style.display = p <= totalPages ? 'flex' : 'none';
            });
            if (prev) prev.disabled = page === 1;
            if (next) next.disabled = page >= totalPages;
        }

        buttons.forEach((btn) => {
            btn.addEventListener('click', () => {
                buttons.forEach((b) => b.classList.remove('active'));
                btn.classList.add('active');
                const filter = btn.dataset.filter;
                filtered = filter === 'all' ? [...cards] : [...cards].filter((c) => c.dataset.category === filter);
                page = 1;
                render();
            });
        });

        if (prev) prev.addEventListener('click', () => { if (page > 1) { page--; render(); } });
        if (next) next.addEventListener('click', () => {
            if (page < Math.ceil(filtered.length / PER_PAGE)) { page++; render(); }
        });
        pageButtons.forEach((btn) => {
            btn.addEventListener('click', () => {
                page = parseInt(btn.dataset.page, 10);
                render();
            });
        });

        render();
    }

    const isElonPage = document.querySelector('.elon-grid');
    if (isElonPage) {
        setupCardFilter({
            cardSelector: '.elon-grid .news-page-card[data-category]',
            buttonSelector: '.news-filter-bar .news-filter-btn[data-filter]',
            pageSelector: '#elonPagination .pag-btn[data-page]',
            prevId: 'elonPagPrev',
            nextId: 'elonPagNext'
        });
    } else {
        setupCardFilter({
            cardSelector: '.news-page-card[data-category]',
            buttonSelector: '.news-filter-btn[data-filter]',
            pageSelector: '.pag-btn[data-page]',
            prevId: 'pagPrev',
            nextId: 'pagNext'
        });
    }

    /* ── Yangilik sahifasi karuseli ──────────────────────────────── */
    (function carousel() {
        const track = document.getElementById('carouselTrack');
        if (!track) return;

        const slides = track.querySelectorAll('.nd-slide');
        const dots = document.getElementById('carouselDots');
        if (!slides.length) return;

        let current = 0;

        function goTo(index) {
            current = (index + slides.length) % slides.length;
            track.style.transform = `translateX(-${current * 100}%)`;
            document.querySelectorAll('.nd-dot').forEach((d, i) => d.classList.toggle('active', i === current));
        }

        if (dots) {
            slides.forEach((_, i) => {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'nd-dot' + (i === 0 ? ' active' : '');
                btn.setAttribute('aria-label', `${i + 1}-rasm`);
                btn.addEventListener('click', () => goTo(i));
                dots.appendChild(btn);
            });
        }

        window.changeSlide = (dir) => goTo(current + dir);
        setInterval(() => goTo(current + 1), 5000);
    })();

    /* ── Normativ hujjatlar: bo'limlar ───────────────────────────── */
    (function normativTabs() {
        const navItems = document.querySelectorAll('.nh-nav-item');
        const panes = document.querySelectorAll('.nh-pane');
        if (!navItems.length) return;

        navItems.forEach((item) => {
            item.addEventListener('click', () => {
                navItems.forEach((n) => n.classList.remove('active'));
                item.classList.add('active');
                panes.forEach((p) => p.classList.remove('active'));
                const pane = document.getElementById(item.getAttribute('data-target'));
                if (pane) pane.classList.add('active');
            });
        });
    })();

    /* ── Universitet haqida: yo'nalish tablari ───────────────────── */
    window.showYon = function (key, btn) {
        document.querySelectorAll('.uh-yon-grid').forEach((g) => g.classList.remove('show'));
        document.querySelectorAll('.uh-yon-tab').forEach((b) => b.classList.remove('active'));
        const grid = document.getElementById('yon-' + key);
        if (grid) grid.classList.add('show');
        if (btn) btn.classList.add('active');
    };

    /* ── Rahbariyat: akkordeon ───────────────────────────────────── */
    window.toggleAccordion = function (btn) {
        const body = btn.nextElementSibling;
        const icon = btn.querySelector('i');
        const wasOpen = body && body.classList.contains('open');

        document.querySelectorAll('.rd-accordion-body').forEach((b) => b.classList.remove('open'));
        document.querySelectorAll('.rd-accordion-btn i').forEach((i) => { i.style.transform = 'rotate(0deg)'; });

        if (!wasOpen && body) {
            body.classList.add('open');
            if (icon) icon.style.transform = 'rotate(180deg)';
        }
    };

    /* ── Hujjat topshirish formasi (alohida sahifa) ──────────────── */
    (function admissionForm() {
        const phoneInput = document.getElementById('phoneInput');
        const phoneWrap = document.getElementById('phoneWrap');
        const phoneError = document.getElementById('phoneError');
        if (!phoneInput) return;

        function formatPhone(el) {
            const raw = el.value.replace(/\D/g, '').slice(0, 9);
            let out = raw.slice(0, 2);
            if (raw.length > 2) out += ' ' + raw.slice(2, 5);
            if (raw.length > 5) out += ' ' + raw.slice(5, 7);
            if (raw.length > 7) out += ' ' + raw.slice(7, 9);
            el.value = out;
        }

        phoneInput.addEventListener('input', function () {
            formatPhone(this);
            if (phoneError) phoneError.style.display = 'none';
            if (phoneWrap) phoneWrap.style.borderColor = '';
        });

        const phone2 = document.getElementById('phone2');
        if (phone2) phone2.addEventListener('input', function () { formatPhone(this); });

        function setStep(n) {
            ['s1', 's2', 's3', 's4'].forEach((id, i) => {
                const el = document.getElementById(id);
                if (el) el.className = 'ht-step ' + (i + 1 < n ? 'done' : i + 1 === n ? 'active' : 'pending');
            });
            ['line1', 'line2', 'line3'].forEach((id, i) => {
                const el = document.getElementById(id);
                if (el) el.className = 'ht-step-line' + (i + 1 < n ? ' done' : '');
            });
        }

        function showPanel(n) {
            document.querySelectorAll('.ht-panel').forEach((p) => p.classList.remove('active'));
            const panel = document.getElementById('panel' + n);
            if (panel) panel.classList.add('active');
            setStep(n);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        window.submitPhone = function (e) {
            e.preventDefault();
            if (phoneInput.value.replace(/\D/g, '').length < 9) {
                if (phoneError) phoneError.style.display = 'flex';
                if (phoneWrap) phoneWrap.style.borderColor = '#e53e3e';
                phoneInput.focus();
                return;
            }
            const display = document.getElementById('displayPhone');
            if (display) display.textContent = '+998 ' + phoneInput.value;
            showPanel(2);
            setTimeout(() => document.getElementById('familiya')?.focus(), 400);
        };

        window.goBack = function () {
            showPanel(1);
            setTimeout(() => phoneInput.focus(), 400);
        };

        const yonalishlar = {
            bakalavr: [
                'Biotexnologiya', 'Molekulyar biologiya', 'Ekologiya va atrof-muhit muhofazasi',
                'Kimyo (biotexnologiya)', 'Oziq-ovqat texnologiyasi', 'Agrokimyo va agrotuproqshunoslik'
            ],
            magistr: ['Biotexnologiya (magistr)', 'Molekulyar genetika', 'Ekologiya (magistr)'],
            malaka: ['Biotexnologik jarayonlar', 'Laboratoriya tahlili']
        };

        window.updateYonalish = function () {
            const bosqich = document.getElementById('bosqich');
            const select = document.getElementById('yonalish');
            if (!bosqich || !select) return;

            select.innerHTML = bosqich.value
                ? '<option value="">Yo\'nalishni tanlang...</option>'
                : '<option value="">Avval ta\'lim bosqichini tanlang...</option>';

            (yonalishlar[bosqich.value] || []).forEach((name) => {
                const option = document.createElement('option');
                option.value = name.toLowerCase().replace(/\s+/g, '_');
                option.textContent = name;
                select.appendChild(option);
            });
        };

        window.submitReg = function (e) {
            e.preventDefault();
            const value = (id) => document.getElementById(id)?.value || '—';
            const selected = (id) => {
                const el = document.getElementById(id);
                return el?.options[el.selectedIndex]?.text || '—';
            };
            const setText = (id, text) => {
                const el = document.getElementById(id);
                if (el) el.textContent = text;
            };

            setText('rv-familiya', value('familiya'));
            setText('rv-ism', value('ism'));
            setText('rv-sharifi', value('sharifi'));
            setText('rv-phone', '+998 ' + value('phoneInput'));
            const p2 = document.getElementById('phone2')?.value;
            setText('rv-phone2', p2 ? '+998 ' + p2 : 'Kiritilmagan');
            setText('rv-bosqich', selected('bosqich'));
            setText('rv-shakl', selected('shakl'));
            setText('rv-til', selected('til'));
            setText('rv-filial', selected('filial'));
            setText('rv-yonalish', selected('yonalish'));
            setText('rv-phone-final', '+998 ' + value('phoneInput'));

            showPanel(3);
        };

        window.submitFinal = function () { showPanel(4); };

        phoneInput.focus();
    })();
})();
