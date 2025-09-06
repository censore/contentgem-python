# 🚀 Автоматизация публикации ContentGem Python SDK

## ✅ Что настроено

Ваш Python SDK полностью настроен для автоматической публикации через GitHub Actions с использованием PyPI Trusted Publishing (OpenID Connect).

### 📁 Созданные файлы

#### GitHub Actions Workflows

- **`.github/workflows/workflow.yml`** - основной workflow для публикации на PyPI
- **`.github/workflows/test.yml`** - workflow для тестирования и проверки качества кода

#### Документация

- **`GITHUB_ACTIONS_SETUP.md`** - подробные инструкции по настройке GitHub Actions
- **`REPOSITORY_SETUP.md`** - инструкции по настройке PyPI Trusted Publisher
- **`QUICK_START.md`** - быстрый старт для локальной разработки
- **`PUBLISHING.md`** - ручная публикация (альтернативный способ)

## 🔧 Настройка PyPI Trusted Publisher

Используйте эти данные для настройки:

```
PyPI Project Name: contentgem-python
Owner: GemContent
Repository name: GemContent
Workflow name: workflow.yml
Environment name: pypi
```

## 🎯 Способы публикации

### 1. Автоматическая публикация при релизе

```bash
# Создайте тег
git tag v1.0.0
git push origin v1.0.0

# Создайте релиз на GitHub
# Workflow автоматически запустится и опубликует пакет
```

### 2. Ручной запуск через GitHub Actions

- Перейдите в **Actions** → **Publish Python Package to PyPI**
- Нажмите **Run workflow**
- Выберите опции публикации

### 3. Ручной запуск через GitHub CLI

```bash
# Публикация на основной PyPI
gh workflow run "Publish Python Package to PyPI" --ref main

# Публикация на Test PyPI
gh workflow run "Publish Python Package to PyPI" --ref main -f test_pypi=true
```

## 🔍 Что происходит при публикации

1. **Сборка пакета** - автоматическая сборка wheel и source distribution
2. **Проверка пакета** - валидация с помощью twine
3. **Публикация** - загрузка на PyPI или Test PyPI
4. **Верификация** - проверка установки опубликованного пакета

## 🧪 Тестирование

Workflow `test.yml` автоматически:

- Запускает тесты на Python 3.8-3.12
- Проверяет качество кода (black, flake8, mypy)
- Тестирует сборку пакета
- Проверяет локальную установку

## 📦 Результат

После настройки пользователи смогут:

```bash
# Установить пакет
pip install contentgem-python

# Использовать в коде
from contentgem import ContentGemClient
client = ContentGemClient(api_key="your-key")

# Использовать CLI
contentgem --api-key your-key health
contentgem --api-key your-key generate "Write about AI"
```

## 🔄 Обновление версии

Для обновления версии:

1. Обновите версию в `contentgem/__init__.py`
2. Обновите версию в `setup.py`
3. Создайте новый релиз на GitHub
4. Workflow автоматически опубликует новую версию

## 🎉 Готово!

Ваш Python SDK полностью готов к автоматической публикации! Следуйте инструкциям в `GITHUB_ACTIONS_SETUP.md` для завершения настройки.
