const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  }));
}

document.querySelectorAll('[data-year]').forEach(e => e.textContent = new Date().getFullYear());

const io = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('in'); });
}, { threshold: .12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Language switcher and country-based first-visit routing.
// Static GitHub Pages cannot read the visitor IP server-side, so this uses a browser-side
// country lookup and redirects only when there is a matching translated route.
(() => {
  const groups = [
    ['/', '/en/', '/fr/'],
    ['/atelier/', '/en/atelier/', '/fr/atelier/'],
    ['/servicos/', '/en/services/', '/fr/services/'],
    ['/processo/', '/en/process/', '/fr/processus/'],
    ['/catalogos/', '/en/catalogues/', '/fr/catalogues/'],
    ['/paris/', '/en/paris/', '/fr/paris/'],
    ['/contacto/', '/en/contact/', '/fr/contact/'],
    ['/catalogos/alta-costura.html', '/en/catalogues/haute-couture.html', '/fr/catalogues/haute-couture.html'],
    ['/catalogos/lencos.html', '/en/catalogues/scarves.html', '/fr/catalogues/foulards.html'],
    ['/catalogos/tailoring.html', '/en/catalogues/tailoring.html', '/fr/catalogues/tailoring.html'],
    ['/fr/politique-de-confidentialite/', '/fr/politique-de-confidentialite/', '/fr/politique-de-confidentialite/']
  ];
  const langs = ['pt', 'en', 'fr'];
  const path = window.location.pathname.replace(/\/index\.html$/, '/');
  const currentGroup = groups.find(g => g.includes(path));
  const currentLang = currentGroup ? langs[currentGroup.indexOf(path)] : (path.startsWith('/fr/') ? 'fr' : path.startsWith('/en/') ? 'en' : 'pt');

  document.documentElement.setAttribute('data-lang', currentLang);
  document.querySelectorAll('.lang a').forEach(a => {
    const label = (a.textContent || '').trim().toLowerCase();
    if (label === currentLang) a.classList.add('active');
    a.addEventListener('click', () => {
      try { localStorage.setItem('tfLangManual', label || 'manual'); } catch (_) {}
    });
  });

  const params = new URLSearchParams(window.location.search);
  if (params.has('lang') || params.has('no_geo')) return;
  try {
    if (localStorage.getItem('tfLangManual')) return;
    if (sessionStorage.getItem('tfGeoLangChecked')) return;
    sessionStorage.setItem('tfGeoLangChecked', '1');
  } catch (_) {}

  function countryToLang(country) {
    const c = String(country || '').toUpperCase();
    if (['PT', 'BR', 'AO', 'MZ', 'CV', 'GW', 'ST'].includes(c)) return 'pt';
    if (['FR', 'BE', 'CH', 'LU', 'MC'].includes(c)) return 'fr';
    return 'en';
  }
  function browserLang() {
    const l = (navigator.language || navigator.userLanguage || '').toLowerCase();
    if (l.startsWith('pt')) return 'pt';
    if (l.startsWith('fr')) return 'fr';
    return 'en';
  }
  function redirectTo(lang) {
    if (!currentGroup) return;
    const target = currentGroup[langs.indexOf(lang)] || currentGroup[1];
    if (!target || target === path) return;
    window.location.replace(target + window.location.search + window.location.hash);
  }

  fetch('https://ipapi.co/json/', { cache: 'no-store' })
    .then(r => r.ok ? r.json() : Promise.reject())
    .then(data => redirectTo(countryToLang(data.country_code)))
    .catch(() => redirectTo(browserLang()));
})();
