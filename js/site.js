/* ==========================================================================
   ALIANZA CONTABLE — Comportamiento del sitio
   Propuesta de rediseño · DataLab 2026
   Prototipo sin backend: los formularios no envían datos reales.
   ========================================================================== */
(function () {
  'use strict';

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 1. Navegación ---------- */
  function nav() {
    var bar = $('.nav'), burger = $('.burger'), menu = $('#menu');
    if (bar) {
      var onScroll = function () { bar.classList.toggle('is-stuck', window.scrollY > 6); };
      onScroll();
      window.addEventListener('scroll', onScroll, { passive: true });
    }
    if (burger && menu) {
      burger.addEventListener('click', function () {
        var open = menu.classList.toggle('open');
        burger.setAttribute('aria-expanded', open ? 'true' : 'false');
        document.body.style.overflow = open ? 'hidden' : '';
      });
    }
    // En móvil el primer toque sobre "Servicios" despliega el submenú
    $$('.menu > li').forEach(function (li) {
      var sub = $('.submenu', li), a = li.querySelector(':scope > a');
      if (!sub || !a) return;
      a.addEventListener('click', function (e) {
        if (window.innerWidth <= 1040) {
          e.preventDefault();
          li.classList.toggle('sub-open');
        }
      });
    });
    // Cerrar el menú móvil al navegar
    $$('.submenu a, .menu > li > a').forEach(function (a) {
      a.addEventListener('click', function () {
        if (window.innerWidth <= 1040 && a.getAttribute('href') && a.getAttribute('href')[0] !== '#') {
          document.body.style.overflow = '';
        }
      });
    });
  }

  /* ---------- 2. Revelado al hacer scroll ---------- */
  function reveal() {
    var els = $$('.reveal');
    if (!els.length) return;
    if (reduce || !('IntersectionObserver' in window)) {
      els.forEach(function (e) { e.classList.add('in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (e) { io.observe(e); });
  }

  /* ---------- 3. Contadores ---------- */
  function counters() {
    var els = $$('[data-count]');
    if (!els.length) return;
    var run = function (el) {
      var to = parseFloat(el.getAttribute('data-count'));
      var dec = (el.getAttribute('data-dec') | 0);
      if (reduce) { el.textContent = to.toFixed(dec); return; }
      var t0 = null, dur = 1500;
      var step = function (t) {
        if (!t0) t0 = t;
        var p = Math.min((t - t0) / dur, 1);
        var e = 1 - Math.pow(1 - p, 3);
        el.textContent = (to * e).toFixed(dec).replace('.', ',');
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };
    if (!('IntersectionObserver' in window)) { els.forEach(run); return; }
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { run(x.target); io.unobserve(x.target); } });
    }, { threshold: 0.5 });
    els.forEach(function (e) { io.observe(e); });
  }

  /* ---------- 4. Cotizador de outsourcing contable ---------- */
  var COP = function (n) {
    return '$ ' + Math.round(n).toLocaleString('es-CO', { maximumFractionDigits: 0 });
  };

  function cotizador() {
    var form = $('#cotizador');
    if (!form) return;

    // Tarifas de referencia (parametrizables): valores mensuales en COP.
    var BASE = { micro: 420000, pequena: 780000, mediana: 1520000, grande: 2650000 };
    var VOL = { b1: 1, b2: 1.16, b3: 1.36, b4: 1.6 };
    var ADD = {
      iva: 95000, reteft: 85000, nomina: 130000,
      niif: 160000, revisoria: 520000, exogena: 90000
    };
    var LABEL = {
      iva: 'IVA (bimestral o cuatrimestral)',
      reteft: 'Retención en la fuente',
      nomina: 'Nómina y nómina electrónica',
      niif: 'Estados financieros bajo NIIF',
      revisoria: 'Revisoría fiscal',
      exogena: 'Información exógena'
    };

    var out = $('#quote-amount'), rows = $('#quote-rows'), hint = $('#quote-hint');

    function calc() {
      var size = (form.querySelector('input[name="tam"]:checked') || {}).value || 'pequena';
      var vol = (form.querySelector('input[name="vol"]:checked') || {}).value || 'b1';
      var base = BASE[size], mult = VOL[vol];
      var ajuste = base * mult - base;
      var extras = 0, list = [];
      $$('input[name="obl"]:checked', form).forEach(function (i) {
        extras += ADD[i.value] || 0;
        list.push(LABEL[i.value]);
      });
      var total = base + ajuste + extras;
      var lo = Math.round(total / 10000) * 10000;
      var hi = Math.round((total * 1.22) / 10000) * 10000;

      out.innerHTML = '<small>Rango mensual estimado</small>' +
        '<span class="qa-lo">' + COP(lo) + '</span>' +
        '<span class="qa-hi">hasta ' + COP(hi) + '</span>';

      var html = '';
      html += '<li><span>Base por tamaño de empresa</span><b>' + COP(base) + '</b></li>';
      html += '<li><span>Ajuste por volumen de documentos</span><b>' +
        (ajuste > 0 ? '+ ' + COP(ajuste) : 'incluido') + '</b></li>';
      html += '<li><span>Obligaciones adicionales (' + list.length + ')</span><b>' +
        (extras > 0 ? '+ ' + COP(extras) : '—') + '</b></li>';
      html += '<li class="total"><span>Estimado mensual, antes de IVA</span><b>' + COP(lo) + '</b></li>';
      rows.innerHTML = html;

      if (hint) {
        hint.textContent = list.length
          ? 'Incluye: ' + list.join(' · ') + '.'
          : 'Seleccione las obligaciones a cargo para afinar el estimado.';
      }
    }

    form.addEventListener('change', calc);
    form.addEventListener('submit', function (e) { e.preventDefault(); });
    calc();
  }

  /* ---------- 5. Calendario tributario por último dígito del NIT ---------- */
  function dian() {
    var grid = $('#dian-grid');
    if (!grid) return;
    var out = $('#dian-out');

    // Calendario ILUSTRATIVO. Se reemplaza por el decreto oficial de la DIAN
    // al publicar el sitio. El desplazamiento por dígito reproduce la mecánica real.
    var OBL = [
      { n: 'Mensual', t: 'Retención en la fuente · período agosto', base: 9, mes: 'septiembre de 2026' },
      { n: 'Bimestral', t: 'IVA · bimestre julio – agosto', base: 9, mes: 'septiembre de 2026' },
      { n: 'Bimestral', t: 'ICA Bogotá · bimestre julio – agosto', base: 12, mes: 'septiembre de 2026' },
      { n: 'Anual', t: 'Renta personas jurídicas · primera cuota', base: 8, mes: 'abril de 2027' }
    ];

    for (var d = 0; d <= 9; d++) {
      var b = document.createElement('button');
      b.type = 'button';
      b.textContent = d;
      b.setAttribute('aria-pressed', 'false');
      b.setAttribute('aria-label', 'Último dígito del NIT: ' + d);
      b.dataset.d = d;
      grid.appendChild(b);
    }

    // Estado inicial: en vez de dejar la columna vacía, se anticipa el resultado.
    function renderEmpty() {
      var filas = OBL.map(function (o) {
        return '<li><span>' + o.n + '</span><b>' + o.t.split(' · ')[0] + '</b><em>—</em></li>';
      }).join('');
      out.innerHTML =
        '<div class="dian-empty">' +
          '<span class="ic"><svg width="26" height="26" viewBox="0 0 24 24" fill="none">' +
            '<rect x="3" y="5" width="18" height="16" rx="2.4" stroke="currentColor" stroke-width="1.7"/>' +
            '<path d="M3 9.6h18M8 3v4M16 3v4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>' +
            '<circle cx="8.4" cy="13.6" r="1.15" fill="currentColor"/>' +
            '<circle cx="12" cy="13.6" r="1.15" fill="currentColor"/>' +
          '</svg></span>' +
          '<b>Elija un dígito y vea sus fechas</b>' +
          '<p>La DIAN escalona los vencimientos según el último dígito del NIT. ' +
            'Toque el suyo y le mostramos las cuatro obligaciones que vienen.</p>' +
          '<ul class="dian-preview">' + filas + '</ul>' +
        '</div>';
      out.hidden = false;
    }
    renderEmpty();

    grid.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      $$('button', grid).forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      b.setAttribute('aria-pressed', 'true');
      render(parseInt(b.dataset.d, 10));
    });

    function render(dig) {
      // Los dígitos altos vencen más tarde: mecánica escalonada de la DIAN.
      var order = [1, 0, 9, 8, 7, 6, 5, 4, 3, 2];
      var pos = order.indexOf(dig);
      var html = '';
      OBL.forEach(function (o, i) {
        var day = o.base + pos;
        var soon = i === 0;
        html += '<div class="dian-row' + (soon ? ' soon' : '') + '">' +
          '<span class="n">' + o.n + '</span>' +
          '<b>' + o.t + '</b>' +
          '<span class="d">' + day + ' de ' + o.mes + '</span></div>';
      });
      html += '<p class="note" style="margin-top:6px">Fechas ilustrativas del formato. ' +
        'Al publicar el sitio se carga el calendario oficial de la DIAN vigente y se ' +
        'actualiza cada año de forma automática.</p>';
      out.innerHTML = html;
      out.hidden = false;
    }
  }

  /* ---------- 6. Agendamiento del diagnóstico ---------- */
  function agenda() {
    var days = $('#agenda-days');
    if (!days) return;
    var slots = $('#agenda-slots'), picked = $('#agenda-picked'), field = $('#agenda-value');

    var DIA = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];
    var DIA_C = ['dom', 'lun', 'mar', 'mié', 'jue', 'vie', 'sáb'];
    var MES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
      'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
    var MES_C = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];

    var list = [], cur = new Date();
    cur.setDate(cur.getDate() + 1);
    while (list.length < 10) {
      if (cur.getDay() !== 0 && cur.getDay() !== 6) list.push(new Date(cur));
      cur.setDate(cur.getDate() + 1);
    }

    list.forEach(function (dt, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-pressed', 'false');
      b.innerHTML = '<i>' + DIA_C[dt.getDay()] + '</i><b>' + dt.getDate() + '</b><em>' +
        MES_C[dt.getMonth()] + '</em>';
      b.dataset.i = i;
      days.appendChild(b);
    });

    var HORAS = ['08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00',
      '14:00', '14:30', '15:00', '15:30', '16:00', '16:30'];

    function showSlots(i) {
      var dt = list[i];
      slots.innerHTML = '';
      HORAS.forEach(function (h, k) {
        var b = document.createElement('button');
        b.type = 'button';
        b.textContent = h;
        b.setAttribute('aria-pressed', 'false');
        // Ocupación simulada de forma determinista para que la demo sea estable.
        if ((dt.getDate() * 7 + k * 3) % 5 === 0) b.disabled = true;
        b.dataset.h = h;
        slots.appendChild(b);
      });
      slots.hidden = false;
      $('#agenda-slots-label').hidden = false;
      slots.onclick = function (e) {
        var b = e.target.closest('button');
        if (!b || b.disabled) return;
        $$('button', slots).forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
        b.setAttribute('aria-pressed', 'true');
        var txt = DIA[dt.getDay()] + ' ' + dt.getDate() + ' de ' + MES[dt.getMonth()] +
          ', ' + b.dataset.h + ' h';
        picked.innerHTML = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none">' +
          '<path d="M3 8.5l3.2 3.2L13 5" stroke="currentColor" stroke-width="2.2" ' +
          'stroke-linecap="round" stroke-linejoin="round"/></svg> Cita seleccionada: <b>' + txt + '</b>';
        picked.hidden = false;
        if (field) field.value = txt;
      };
    }

    days.addEventListener('click', function (e) {
      var b = e.target.closest('button');
      if (!b) return;
      $$('button', days).forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      b.setAttribute('aria-pressed', 'true');
      picked.hidden = true;
      if (field) field.value = '';
      showSlots(parseInt(b.dataset.i, 10));
    });
  }

  /* ---------- 7. Formularios (prototipo, sin envío real) ---------- */
  function forms() {
    // Preselección del servicio según la página de origen (?servicio=…)
    var qs = new URLSearchParams(location.search).get('servicio');
    if (qs) {
      $$('select[name="servicio"]').forEach(function (s) {
        if ($$('option', s).some(function (o) { return o.value === qs; })) s.value = qs;
      });
    }
    $$('form[data-demo]').forEach(function (f) {
      f.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!f.checkValidity()) { f.reportValidity(); return; }
        var ok = $('.form-ok', f.parentNode) || $('.form-ok', f);
        f.querySelectorAll('input,select,textarea,button').forEach(function (el) { el.disabled = true; });
        if (ok) {
          ok.classList.add('show');
          ok.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
        }
      });
    });
  }

  /* ---------- 8. Banner de cookies (Ley 1581 de 2012) ---------- */
  function cookies() {
    var box = $('#cookies');
    if (!box) return;
    var KEY = 'ac-consent-2026';
    var stored = null;
    try { stored = localStorage.getItem(KEY); } catch (e) { stored = 'x'; }
    if (!stored) setTimeout(function () { box.classList.add('show'); }, 1400);
    $$('[data-consent]', box).forEach(function (b) {
      b.addEventListener('click', function () {
        try {
          localStorage.setItem(KEY, JSON.stringify({
            v: b.dataset.consent, ts: new Date().toISOString()
          }));
        } catch (e) { /* modo privado */ }
        box.classList.remove('show');
      });
    });
  }

  /* ---------- 9. Varios ---------- */
  function misc() {
    $$('[data-year]').forEach(function (e) { e.textContent = new Date().getFullYear(); });
  }

  function init() {
    nav(); reveal(); counters(); cotizador(); dian(); agenda(); forms(); cookies(); misc();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else { init(); }
})();
