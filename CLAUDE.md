# CLAUDE.md — Executive Minds

## Что это

Лендинг образовательной платформы **Executive Minds** для сертифицированных практиков Hogan Assessment.
Разрабатывается Андреем. Клод — исполнитель.

**Путь проекта:** `/Users/yegorovandrei/Desktop/lasttry desktop/Executive Minds/`

---

## Структура файлов

```
index.html          — главная страница (основная работа здесь)
space.html          — страница «О пространстве»
programs.html       — все программы
signup.html         — запись (принимает ?context=)
consent.html        — согласие на обработку данных
cookies.html        — политика cookies
privacy.html        — политика конфиденциальности
_partials.html      — переиспользуемые фрагменты (nav, footer)

assets/css/
  site.css          — основной стилевой файл
  legal.css         — стили для правовых страниц

assets/img/
  фон руки комп апельсин.avif   — hero (текущий)
  people-wall.avif              — альтернативный hero (оранжевый/бирюзовый сплит)
  people-wall-2.avif            — запасной
  group-board.avif              — группа за доской
  people-two.avif               — двое людей

assets/js/
  site.js           — мобильное меню, cookie-баннер
```

---

## Дизайн-система

**Референс:** Wispr Flow (`/Users/yegorovandrei/claude/mini/style_catch/wisperflow_catalog_v5.html`)

**Шрифты:**
- Serif: `EB Garamond` — заголовки (400, 500, 600, italic)
- Sans: `Figtree` — интерфейс, кнопки, подписи (400, 500, 600)
- Подключены через Google Fonts на всех 8 HTML-файлах

**Ключевые CSS-переменные (site.css):**
```css
--cream: #F4EFE3       /* фон страниц */
--forest: #0C1F1A      /* nav, тёмные секции */
--amber-soft: #C9A065  /* акцент */
--serif: 'EB Garamond'
--sans: 'Figtree'
--maxw: 1240px
--pad: clamp(1.25rem, 3vw, 2.5rem)
```

**Типографика:**
```css
h1: clamp(2.4rem, 5.8vw, 4.6rem) — letter-spacing: -0.05em — line-height: 0.88
h2: clamp(1.8rem, 3.6vw, 2.9rem) — letter-spacing: -0.03em — line-height: 0.95
h3: clamp(1.25rem, 2vw, 1.55rem)
```

**Секции:**
```css
.section       → padding: clamp(3.5rem, 7vw, 6rem) 0   /* стандарт — использовать везде */
.section-tight → padding: clamp(2.5rem, 5vw, 4rem) 0   /* только по явному запросу */
```

---

## Hero (текущее состояние)

```html
<section class="hero-v2">
  <img src="assets/img/фон руки комп апельсин.avif" class="hero-v2-img">
  <div class="hero-v2-body">
    <h1>Инструменты<br>глубинного анализа<br>Hogan</h1>
    <p>Практический курс для специалистов...</p>
    <a href="signup.html?context=group" class="btn btn--outline-light">Записаться в группу</a>
  </div>
</section>
```

**CSS героя** (inline `<style>` в index.html):
- `height: calc(100vh - 52px)` — полный экран под навом
- `object-fit: cover; object-position: center center` — без фильтров и оверлея
- Контент: `justify-content: center; align-items: center; text-align: center`
- Кнопка: `btn--outline-light` — прозрачная с белой рамкой

**Правила по изображению:** никаких CSS `filter` и оверлеев на картинке. Только `::after` если нужен градиент — но сейчас его нет.

---

## Правила работы

1. **Менять только то, о чём явно сказал Андрей.** Не трогать ничего лишнего.
2. Никаких inline-стилей если есть CSS-класс.
3. Все секции используют `.section` — не `.section-tight`.
4. Коммит только по запросу.
5. Перед коммитом — `git status` чтобы убедиться что лишнего нет.

---

## Где остановились (2026-05-19)

- ✅ Hero переделан: полноэкранный, новая картинка, центрированный текст
- ✅ Шрифты: EB Garamond + Figtree на всех страницах
- ✅ Оверлеи убраны (hero + strip-секция)
- ✅ Отступы секций выровнены
- ✅ Локальный git-репозиторий создан

**В процессе:**
- Сравнение стилей с Wispr Flow — начали, не завершили
- Playwright MCP — установка поручена (команда: `claude mcp add playwright npx @playwright/mcp@latest`)

**Следующие шаги (ещё не обсуждались):**
- Доработка остальных страниц (space.html, programs.html, signup.html)
- Контент секций index.html (тексты ещё placeholder)
