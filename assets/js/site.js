// Executive Minds — site scripts

(function () {
  // Mobile nav toggle
  var toggle = document.getElementById('navToggle');
  var list = document.getElementById('navList');
  if (toggle && list) {
    toggle.addEventListener('click', function () {
      var open = list.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Cookie notice — restored logic: show until accepted, store 30 days.
  function getCookie(name) {
    var parts = document.cookie.split(';');
    for (var i = 0; i < parts.length; i++) {
      var p = parts[i].trim();
      if (p.indexOf(name + '=') === 0) return decodeURIComponent(p.substring(name.length + 1));
    }
    return null;
  }
  function setCookie(name, value, days) {
    var d = new Date();
    d.setTime(d.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + d.toUTCString() + '; path=/; SameSite=Lax';
  }

  var banner = document.getElementById('cookieBanner');
  var acceptBtn = document.getElementById('cookieAccept');
  if (banner && acceptBtn) {
    if (!getCookie('em_cookie_consent')) {
      // small delay so it doesn't fight initial hero
      setTimeout(function () { banner.classList.add('is-visible'); }, 700);
    }
    acceptBtn.addEventListener('click', function () {
      setCookie('em_cookie_consent', 'accepted', 30);
      banner.classList.remove('is-visible');
    });
  }
})();
