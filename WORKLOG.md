# WORKLOG — Executive Minds

Лог изменений и известных настроек «to be».

---

## Сделано

### Шрифты (все 8 HTML-файлов)
| Было | Стало |
|------|-------|
| `Fraunces` (serif) | `EB Garamond` (serif) |
| `Inter Tight` (sans) | `Figtree` (sans) |
| Google Fonts: `Fraunces:ital,wght@...&Inter+Tight:wght@...` | `EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&Figtree:wght@400;500;600` |

**CSS-переменные (site.css):**
| Было | Стало |
|------|-------|
| `--serif: 'Fraunces'` | `--serif: 'EB Garamond', Garamond, Georgia, serif` |
| `--sans: 'Inter Tight'` | `--sans: 'Figtree', system-ui, ...` |

### Типографика заголовков (site.css)
| Параметр | Было | Стало |
|----------|------|-------|
| `h1 font-size` | `clamp(2.2rem, 4vw, 3.8rem)` | `clamp(2.4rem, 5.8vw, 4.6rem)` |
| `h1 letter-spacing` | `-0.03em` | `-0.05em` |
| `h1 line-height` | `1.1` | `0.88` |
| `h2 font-size` | `clamp(1.6rem, 3vw, 2.4rem)` | `clamp(1.8rem, 3.6vw, 2.9rem)` |
| `h2 letter-spacing` | `-0.02em` | `-0.03em` |
| `h2 line-height` | `1.2` | `0.95` |
| `h1–h4 font-weight` | `500` | `400` |

### Hero-секция (index.html)
| Параметр | Было | Стало |
|----------|------|-------|
| Структура | Две секции: `program-slab` + `course-hero` | Одна секция `hero-v2` |
| Высота | `min-height: clamp(500px, 68vh, 760px)` | `height: calc(100vh - 52px)` |
| Layout | Два столбца: текст + карточка фактов | Один столбец, по центру |
| Оверлей | `linear-gradient(to top, rgba(12,31,26,0.82)...)` | Нет |
| Картинка | `people-wall.avif` | `фон руки комп апельсин.avif` |
| Кнопка | `btn--cream` (белая) | `btn--outline-light` (прозрачная) |
| h1 | Два `<h1>` на странице | Один `<h1 id="hero-title">` |
| Pill-тег | Был (`Поток · 5 суббот · Онлайн`) | Убран |
| Карточка фактов | Была (aside) | Убрана |

### Остальные секции (index.html + site.css)
| Что | Было | Стало |
|-----|------|-------|
| Strip-секция оверлей | `linear-gradient(90deg, rgba(12,31,26,0.85)...)` | Убран |
| Единственная `section-tight` (строка 325) | `.section-tight` | `.section` |
| Section-header inline padding | `style="padding-top:2rem;"` | Убрано |

### Глобальное (site.css)
| Что | Было | Стало |
|-----|------|-------|
| `scroll-padding-top` | Не было | `64px` |

---

## To Be — известные настройки, ещё не внедрённые

### Из анализа Wispr Flow CSS
Источник: `https://cdn.prod.website-files.com/682f84b3838c89f8ff7667db/css/flowsite-dev.webflow.shared.17b04da35.min.css`

#### Заголовки

| Параметр | Wispr Flow | У нас сейчас | ✅/❌ |
|----------|-----------|--------------|------|
| h1 font-size | `7.5rem` | `clamp(2.4rem, 5.8vw, 4.6rem)` | ❌ значительно меньше |
| h1 font-weight | `400` | `400` | ✅ |
| h1 line-height | `0.85` | `0.88` | ≈ близко |
| h1 letter-spacing | `-0.05em` | `-0.05em` | ✅ |
| h2 font-size | `4rem` | `clamp(1.8rem, 3.6vw, 2.9rem)` | ❌ наш max меньше |
| h2 line-height | `0.95` | `0.95` | ✅ |
| h2 letter-spacing | `-0.03em` | `-0.03em` | ✅ |
| h3 font-size | `3rem` | `clamp(1.25rem, 2vw, 1.55rem)` | ❌ сильно меньше |
| h3 line-height | `1.1` | `1.1` | ✅ |
| h4 font-size | `2rem` | `1.05rem` | ❌ вдвое меньше |
| h4 line-height | `1.3` | `1.2` | ≈ |
| h4 letter-spacing | `-0.03em` | `-0.01em` | ❌ |

#### Цвета

| Параметр | Wispr Flow | У нас сейчас | ✅/❌ |
|----------|-----------|--------------|------|
| Фон страницы (cream) | `#ffffeb` | `#F4EFE3` | ❌ разные оттенки |
| Тёмный фон | `#1a1a1a` | `#0C1F1A` | ❌ |
| Текст primary | `#1a1a1a` | `#16201B` | ≈ |
| Акцент (glow/amber) | `#ffa946` | `#C9A065` | ❌ |
| Акцент 2 (dawn) | `#f0d7ff` (лавандовый) | нет | ❌ |
| Зелёный акцент | `#034f46` | `#3B5A45` (`--moss`) | ≈ |

#### Кнопки

| Параметр | Wispr Flow | У нас сейчас | ✅/❌ |
|----------|-----------|--------------|------|
| border-radius | `0.75rem` | `999px` (pill) | ❌ |
| padding default | `1rem 1.5rem` | `0.9rem 1.4rem` | ≈ |
| padding large | `1rem 2rem` | нет варианта | ❌ |
| font-weight | `600` | `500` | ❌ |
| line-height | `1` | не задан | ❌ |

#### Секции и отступы

| Параметр | Wispr Flow | У нас сейчас | ✅/❌ |
|----------|-----------|--------------|------|
| Section padding large | `8rem` | `clamp(3.5rem, 7vw, 6rem)` | ❌ меньше |
| Section padding medium | `6rem` | `clamp(2.5rem, 5vw, 4rem)` | ❌ |
| Section border-radius | `2.5rem / 4rem / 5rem` | нет | ❌ |
| Container max-width | `77.5rem` (1240px) | `1240px` | ✅ |

#### Шрифты (подтверждено)
| | Wispr Flow | У нас | ✅/❌ |
|-|-----------|-------|------|
| Serif | `"Eb garamond"` | `'EB Garamond'` | ✅ |
| Sans | `Figtree` | `Figtree` | ✅ |
| Mono | `Monaspace Neon` / `IBM Plex Mono` | `JetBrains Mono` | ❌ (не критично) |

### Технические
| Задача | Статус |
|--------|--------|
| Playwright MCP (скриншоты для Клода) | ⏳ установить: `claude mcp add playwright npx @playwright/mcp@latest` |
| Полное сравнение стилей Wispr Flow | ⏳ не завершено |

### Страницы
| Страница | Статус |
|----------|--------|
| `index.html` | 🔧 в работе |
| `space.html` | ⏳ не начата |
| `programs.html` | ⏳ не начата |
| `signup.html` | ⏳ не начата |
