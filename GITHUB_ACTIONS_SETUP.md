# Настройка GitHub Actions для автоматической публикации

## 🚀 Автоматическая публикация через GitHub Actions

Ваш Python SDK настроен для автоматической публикации через GitHub Actions с использованием OpenID Connect (OIDC) для безопасной аутентификации с PyPI.

## 📋 Настройка GitHub Environment

### 1. Создайте GitHub Environment

1. Перейдите в ваш репозиторий на GitHub
2. Нажмите **Settings** → **Environments**
3. Нажмите **New environment**
4. Введите имя: `pypi`
5. Нажмите **Configure environment**

### 2. Настройте Protection Rules (рекомендуется)

- ✅ **Required reviewers**: Добавьте себя как reviewer
- ✅ **Wait timer**: 0 минут (или по желанию)
- ✅ **Deployment branches**: Ограничьте только `main` веткой

### 3. Настройте Environment Secrets

В разделе **Environment secrets** добавьте:

- `TEST_PYPI_API_TOKEN` - API токен для Test PyPI (для тестирования)

## 🔧 Настройка PyPI Trusted Publishing

### 1. Перейдите в настройки PyPI

1. Войдите в [PyPI](https://pypi.org)
2. Перейдите в **Account settings** → **Publishing**
3. Нажмите **Add a new pending publisher**

### 2. Заполните форму

```
PyPI Project Name: contentgem-python
Owner: GemContent
Repository name: GemContent
Workflow name: workflow.yml
Environment name: pypi
```

### 3. Подтвердите настройки

- Нажмите **Add pending publisher**
- GitHub автоматически создаст pull request для подтверждения

## 🎯 Способы запуска публикации

### 1. Автоматическая публикация при релизе

```bash
# Создайте и опубликуйте релиз
git tag v1.0.0
git push origin v1.0.0

# Создайте релиз на GitHub через веб-интерфейс
# Workflow автоматически запустится и опубликует пакет
```

### 2. Ручной запуск через GitHub Actions

1. Перейдите в **Actions** → **Publish Python Package to PyPI**
2. Нажмите **Run workflow**
3. Выберите ветку и опции:
   - `test_pypi: false` - публикация на основной PyPI
   - `test_pypi: true` - публикация на Test PyPI

### 3. Ручной запуск через GitHub CLI

```bash
# Публикация на основной PyPI
gh workflow run "Publish Python Package to PyPI" --ref main

# Публикация на Test PyPI
gh workflow run "Publish Python Package to PyPI" --ref main -f test_pypi=true
```

## 🔍 Мониторинг и отладка

### 1. Просмотр логов

- Перейдите в **Actions** → выберите workflow run
- Просмотрите логи каждого шага

### 2. Частые проблемы

**Ошибка аутентификации:**

- Проверьте, что PyPI Trusted Publisher настроен правильно
- Убедитесь, что Environment `pypi` существует

**Ошибка сборки:**

- Проверьте, что все зависимости указаны в `setup.py`
- Убедитесь, что код проходит все тесты

**Ошибка публикации:**

- Проверьте, что версия пакета уникальна
- Убедитесь, что пакет не существует на PyPI

## 📦 Структура workflow

### Основной workflow (`workflow.yml`)

- ✅ **Триггеры**: релизы и ручной запуск
- ✅ **Сборка**: автоматическая сборка пакета
- ✅ **Проверка**: валидация пакета
- ✅ **Публикация**: на PyPI или Test PyPI
- ✅ **Верификация**: проверка установки

### Тестовый workflow (`test.yml`)

- ✅ **Тестирование**: на Python 3.8-3.12
- ✅ **Качество кода**: black, flake8, mypy
- ✅ **Сборка**: проверка сборки пакета
- ✅ **Установка**: тест локальной установки

## 🎉 Готово!

После настройки:

1. **Создайте релиз** на GitHub
2. **Workflow автоматически запустится**
3. **Пакет будет опубликован** на PyPI
4. **Пользователи смогут установить** через `pip install contentgem-python`

## 🔄 Обновление версии

Для обновления версии:

1. Обновите версию в `contentgem/__init__.py`
2. Обновите версию в `setup.py`
3. Создайте новый релиз на GitHub
4. Workflow автоматически опубликует новую версию

## 📚 Полезные ссылки

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishing/)
- [OpenID Connect](https://docs.github.com/en/actions/deployment/security/hardening-your-deployments/about-security-hardening-with-openid-connect)
