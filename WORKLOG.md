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

## Сессия 2026-05-19 (вечер) — оверлеи, инфраструктура, ROSA

### Инфраструктура
| Что | Результат |
|-----|-----------|
| Git-репозиторий | Инициализирован в `lasttry desktop/`, стартовый коммит 244 файла |
| Скилл `pixel-match-design` | Создан в `~/.claude/skills/` — активный рабочий процесс верстки |
| `ui-ux-pro-max` | Подключён как вспомогательный инструмент на этапе реализации |
| Локальный сервер | `python3 -m http.server 8080` → `http://localhost:8080/` (запускать вручную) |
| ROSA | Service Manager активирована, записывает лог |

### Оверлеи — исправлено
| Файл | Что было | Что стало |
|------|----------|-----------|
| `site.css` — `.strip-bg` | `brightness(0.45) blur(2px)` | `brightness(0.62)`, blur убран |
| `site.css` — `.strip-bg::after` | `background: transparent` (мёртвое правило) | Правило удалено |
| `space.html` — `.atmos .a-bg` | `brightness(0.45)` + `::after` с градиентом `rgba(12,31,26,0.85→0.4)` | `brightness(0.58)`, градиент убран |
| `index.html` — `.hero-v2-h1` | `text-shadow: 0 2px 30px rgba(0,0,0,0.4)` | Убран |
| `index.html` — `.hero-v2-sub` | `text-shadow: 0 1px 12px rgba(0,0,0,0.3)` | Убран |

Коммит: `4c48ac4` — «fix: remove overlay layers, lift brightness on strip and atmos sections»

### Навигация
| Страница | Статус |
|----------|--------|
| `index.html` | 🔧 в работе — hero готов, оверлеи убраны |
| `space.html` | 🔧 частично — оверлеи убраны, hero не переделан |
| `programs.html` | ⏳ не начата |
| `signup.html` | ⏳ не начата |

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

---

## Сессия 2026-05-22 — диагностика Wispr Flow + наполнение index.html

### Контекст сессии
Перед правками провели полный аудит сайта Wispr Flow (8 страниц) по диагностическому фреймворку landing page. Цель — понять что брать как образец и как наполнять Executive Minds.

### Аудит Wispr Flow — ключевые выводы
| Страница | Сильное | Слабое |
|----------|---------|--------|
| Homepage | Hero H1, social proof (Reid Hoffman, Clay $3M ROI), 4x/220wpm | Нет Problem/Pain блока, pricing скрыт |
| /features | Детальные фичи с benefit-формулировками | Нет testimonials |
| /leaders | Compliance badges, цифры | Hero слабый, нет FAQ |
| /developers | Чёткий ICP + конкретика (camelCase, Cursor) | Нет developer testimonials |
| /business | Pricing виден | Один testimonial — мало для B2B |
| /case-study/clay | Лучший контент: $3.08M savings, 52% faster, 20% more calls | Спрятан в 3 клика от главной |
| /media-kit | "72% символов через Flow после 6 месяцев" | Эта цифра нигде не используется на сайте |

**Системные пробелы Wispr Flow (применимо как анти-паттерн):**
- Problem/Pain отсутствует везде
- FAQ/Objections = ноль
- Risk reversal не рядом с CTA
- Urgency отсутствует
- Лучший контент (кейс Clay) спрятан глубоко

### Изображения — добавлены в assets/img
| Файл | Откуда | Использование |
|------|--------|---------------|
| `laptop-hands.webp` | `Картинки/квадратик комп руки.webp` | Strip "Отчёт за полчаса" |
| `office-blur.webp` | `Картинки/квадратик офис столы.webp` | Strip "Новая суперсила" (среда) |
| `final-bg.png` | `Картинки/фон девушка с телефоном.png` | Финальный CTA (opacity 22%) |
| `person-host.webp` | `Картинки/квадратик парень.webp` | Блок ведущего |
| `person-quote.webp` | `Картинки/квадратик девушка.webp` | Зарезервировано под цитаты |
| `two-people.avif` | `Картинки/фон двое.avif` | Зарезервировано |

**Не используются как фоны** (это скриншоты-референсы, не изображения):
- `плашка - отчет за полчаса.png` — референс дизайна из Wispr Flow /features с русским текстом
- `плашка - суперсила с кнопкой.png` — то же
- `плашка - чат.png` — то же

### Изменения index.html (сессия 2026-05-22)

| Секция | Было | Стало |
|--------|------|-------|
| Hero H1 | "Инструменты глубинного анализа Hogan" | "Видеть в Hogan больше, чем привычные 20%" |
| Hero sub | "Практический курс для специалистов..." | "Не ещё одно обучение по шкалам. Место, где ваш опыт, интуиция и Hogan начинают работать вместе — на качество решений, а не на отчёт." |
| Value-секция body | Placeholder-текст | Реальный текст: 80/20, рамка, без перегрузки |
| Value pull-quote | Placeholder | "Когда цена ошибки в людях высока, важна не просто интерпретация, а качество решения, которое выдерживает время" |
| Strip фон | `people-wall.avif` | `laptop-hands.webp` |
| Strip текст | Placeholder | Почищен |
| Новая секция | — | "Новая суперсила" — среда/сообщество, фон `office-blur.webp` |
| Финальный CTA h2 | "Начните со встречи-знакомства 30 мая" | "Интересно стать частью следующего потока?" |
| Финальный CTA подзаголовок | Про даты потока | "Интуиция не отменяется. Она становится точнее." |
| Финальный CTA фон | Просто `--forest` цвет | + `final-bg.png` overlay (opacity 22%) |
| Блок ведущего | Только текст | + фото `person-host.webp` |

### Источники текстов
Все тексты взяты из картотеки:
`/Users/yegorovandrei/claude/mini/executiveminds/образцы/плохие/executive-minds-kartoteka - отредактировать.html`

Ключевые формулировки из картотеки использованные:
- "80% компаний и экспертов используют около 20% возможностей Hogan"
- "Когда цена ошибки в людях высока..."
- "Не ещё одно обучение по шкалам. Место, где ваш опыт, интуиция и Hogan начинают работать вместе"
- "Интуиция не отменяется. Она становится точнее."
- "Таких мест на рынке мало: где одновременно встречаются заказчики, клиенты, более опытные и менее опытные"

### Вдохновение дизайна (замечено в сессии)
| Элемент | Источник | Применено |
|---------|---------|-----------|
| Двухцветный hero заголовок | Wispr Flow /privacy ("Privacy first. Security always.") | Пока нет — кандидат для будущей итерации |
| "Interested in becoming an ambassador?" | Wispr Flow /students — последний фрейм | Адаптировано в "Интересно стать частью следующего потока?" |
| Editable HTML (contenteditable) | `wisprflow-real-editable-v4.html` на рабочем столе | Референс, не используется напрямую |

### Статус страниц после сессии
| Страница | Статус |
|----------|--------|
| `index.html` | ✅ Контент заполнен, визуал обновлён. Осталось: цена, даты, цитаты участников |
| `space.html` | ⏳ не начата |
| `programs.html` | ⏳ не начата |
| `signup.html` | ⏳ не начата |

### Что осталось заполнить (нужен Андрей)
- [ ] Цена курса и варианты оплаты
- [ ] Финальные даты потока (сейчас 30 мая / 13 или 20 июня)
- [ ] Цитаты от реальных участников (для `person-quote.webp`)
- [ ] Финальные формулировки модулей I–V
- [ ] Количество feedback-сессий и потоков для trust-strip
