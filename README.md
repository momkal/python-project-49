# Игры разума (Python)

[![hexlet-check](https://github.com/momkal/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/momkal/python-project-49/actions)

Погрузитесь в экосистему Python и научитесь настраивать рабочее окружение. Подружитесь с менеджером зависимостей и линтером. Поймете, чем git отличается от GitHub, поработаете с внешними репозиториями. Получите опыт построения архитектуры полноценного приложения и написания чистого кода.

Учебный проект Хекслета: https://ru.hexlet.io/programs/python
Как это должно работать: https://asciinema.org/a/l40Lrk3midkLmNEOmgZErGnY7

## Минимальные требования

- Python 3.14.9+
- uv

## Стек

- Python

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/momkal/python-project-49.git
cd python-project-49
```

Соберите и установите приложение:

```bash
uv build
uv tool install dist/*.whl
```
После установки команды игры будут доступны напрямую.

## Использование

### BRAIN EVEN

Определите, является ли число чётным.

Запуск:

```bash
brain-even
```

Демонстрация:

[![asciicast](https://asciinema.org/a/LcAYt21NjttbKznl.svg)](https://asciinema.org/a/LcAYt21NjttbKznl)

### BRAIN CALC

Вычислите результат математического выражения.

Запуск:

```bash
brain-calc
```

Демонстрация:

[![asciicast](https://asciinema.org/a/KUdcc4rPLONdySqm.svg)](https://asciinema.org/a/KUdcc4rPLONdySqm)

### BRAIN GCD

Найдите наибольший общий делитель двух чисел.

Запуск:

```bash
brain-gcd
```

Демонстрация:

[![asciicast](https://asciinema.org/a/gC1qRUGD7qdaUu16.svg)](https://asciinema.org/a/gC1qRUGD7qdaUu16)

### BRAIN PROGRESSION

Найдите пропущенное число в арифметической прогрессии.

Запуск:

```bash
brain-progression
```

Демонстрация:

[![asciicast](https://asciinema.org/a/u3n2UfyDb7qn9Ctc.svg)](https://asciinema.org/a/u3n2UfyDb7qn9Ctc)

### BRAIN PRIME

Определите, является ли число простым.

Запуск:

```bash
brain-prime
```

Демонстрация:

[![asciicast](https://asciinema.org/a/2xtGVXiGoYh2c2W4.svg)](https://asciinema.org/a/2xtGVXiGoYh2c2W4)

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
