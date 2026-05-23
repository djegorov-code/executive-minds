# COMMANDS — Executive Minds

Всё, что нужно запускать вручную при работе над сайтом.

---

## Перед сессией — обязательно

### 1. Playwright MCP — чтобы агент видел экран
Установить один раз:
```bash
claude mcp add playwright npx @playwright/mcp@latest
```
После установки перезапустить Claude Code.

**Зачем:** без этого агент не может сделать скриншот браузера и сравнить верстку с образцом. Именно это было пропущено в сессии 2026-05-19 — агент работал вслепую.

### 2. Локальный сервер — чтобы сайт открывался в браузере
```bash
cd "/Users/yegorovandrei/Desktop/lasttry desktop/Executive Minds"
python3 -m http.server 8080
```
Затем открыть: **http://localhost:8080/**

**Зачем:** Chrome блокирует `file://` — локальные ресурсы (CSS, JS, шрифты) не грузятся. Через сервер всё работает, ссылки кликабельны.

---

## Навигация по сайту (localhost)

| Страница | URL |
|----------|-----|
| Главная (index) | http://localhost:8080/ |
| О пространстве | http://localhost:8080/space.html |
| Все программы | http://localhost:8080/programs.html |
| Запись | http://localhost:8080/signup.html |

---

## Git — рабочие команды

```bash
# Статус изменений
cd "/Users/yegorovandrei/Desktop/lasttry desktop"
git status

# Посмотреть историю
git log --oneline

# Создать snapshot перед изменениями
git add -A && git commit -m "snapshot: before [что делаем]"

# Закрыть задачу коммитом
git add -A && git commit -m "feat: [что сделали]"
```

---

## Скиллы Claude (вызываются в чате)

| Команда | Что делает |
|---------|-----------|
| `/pixel-match-design` | Запускает рабочий процесс верстки по образцу |
| `/superpowers:using-superpowers` | Загружает систему скиллов |

---

## Стандартный старт сессии вебдизайна

```
1. Запустить сервер:
   cd "/Users/yegorovandrei/Desktop/lasttry desktop/Executive Minds"
   python3 -m http.server 8080

2. Открыть в браузере: http://localhost:8080/

3. В Claude Code написать: /pixel-match-design

4. Показать образец (скриншот или файл из «Примеры верстки обязательные»)
   и сказать куда его поставить
```

---

## Остановить сервер

```bash
# Найти PID
lsof -ti:8080

# Убить
kill $(lsof -ti:8080)
```
