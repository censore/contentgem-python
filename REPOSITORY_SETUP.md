# Настройка репозитория для автоматической публикации

## 📋 Инструкции по настройке PyPI Trusted Publisher

Используйте следующие данные для настройки PyPI Trusted Publisher:

### PyPI Project Name

```
contentgem-python
```

### Owner

```
GemContent
```

### Repository name

```
GemContent
```

### Workflow name

```
workflow.yml
```

### Environment name

```
pypi
```

## 🔧 Пошаговая настройка

### 1. Настройка GitHub Environment

1. Перейдите в ваш репозиторий на GitHub
2. Нажмите **Settings** → **Environments**
3. Нажмите **New environment**
4. Введите имя: `pypi`
5. Нажмите **Configure environment**

### 2. Настройка PyPI Trusted Publisher

1. Войдите в [PyPI](https://pypi.org)
2. Перейдите в **Account settings** → **Publishing**
3. Нажмите **Add a new pending publisher**
4. Заполните форму с данными выше
5. Нажмите **Add pending publisher**

### 3. Подтверждение настройки

GitHub автоматически создаст pull request для подтверждения настройки. После его принятия публикация будет работать автоматически.

## 🚀 Способы запуска публикации

### Автоматическая публикация при релизе

```bash
# Создайте тег
git tag v1.0.0
git push origin v1.0.0

# Создайте релиз на GitHub через веб-интерфейс
```

### Ручной запуск

1. Перейдите в **Actions** → **Publish Python Package to PyPI**
2. Нажмите **Run workflow**
3. Выберите опции публикации

## 📁 Структура файлов

```
client-libraries/python/
├── .github/
│   └── workflows/
│       ├── workflow.yml      # Основной workflow для публикации
│       └── test.yml          # Workflow для тестирования
├── contentgem/
│   ├── __init__.py
│   ├── client.py
│   ├── types.py
│   ├── cli.py
│   └── py.typed
├── tests/
├── setup.py
├── pyproject.toml
├── MANIFEST.in
├── README.md
├── CHANGELOG.md
├── LICENSE
├── build.py
├── example.py
├── QUICK_START.md
├── PUBLISHING.md
├── GITHUB_ACTIONS_SETUP.md
└── REPOSITORY_SETUP.md
```

## ✅ Проверочный список

- [ ] GitHub Environment `pypi` создан
- [ ] PyPI Trusted Publisher настроен
- [ ] Workflow файлы загружены в репозиторий
- [ ] Тесты проходят успешно
- [ ] Пакет собирается без ошибок
- [ ] Первый релиз создан и опубликован

## 🎉 Готово!

После выполнения всех шагов ваш пакет будет автоматически публиковаться на PyPI при каждом релизе!
