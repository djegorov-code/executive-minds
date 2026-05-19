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

### Из анализа Wispr Flow
Источник: `/Users/yegorovandrei/claude/mini/style_catch/wisperflow_catalog_v5.html`

| Параметр | Wispr Flow | У нас сейчас | Статус |
|----------|-----------|--------------|--------|
| Основной акцент | `#FF6C4C` (coral) | `--amber-soft: #C9A065` | ❓ обсудить |
| Семантические токены цвета | `text-color-primary/secondary/tertiary` | Нет, только `--ink/--ink-soft` | ❓ |
| Spacer-система | `spacer-xxsmall` … `spacer-xxlarge` | `clamp()` напрямую | ❓ |
| Кнопки размеры | `is-small`, `is-medium-small` | `btn--sm` | ❓ |

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
