# Быстрый старт: Публикация ContentGem Python SDK

## ✅ Что уже готово

Ваш Python SDK полностью готов к публикации! Все необходимые файлы созданы:

- ✅ `setup.py` - конфигурация пакета
- ✅ `pyproject.toml` - современная конфигурация
- ✅ `MANIFEST.in` - файлы для включения в пакет
- ✅ `contentgem/py.typed` - поддержка type hints
- ✅ `contentgem/cli.py` - CLI интерфейс
- ✅ `build.py` - скрипт для сборки и публикации
- ✅ `PUBLISHING.md` - подробные инструкции

## 🚀 Быстрая публикация

### 1. Создайте аккаунты

- [PyPI](https://pypi.org) - основной репозиторий
- [Test PyPI](https://test.pypi.org) - тестовый репозиторий

### 2. Настройте API токены

Создайте файл `~/.pypirc`:

```ini
[distutils]
index-servers = pypi testpypi

[pypi]
username = __token__
password = pypi-your-api-token-here

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-your-test-api-token-here
```

### 3. Соберите пакет

```bash
cd client-libraries/python
python3 -m venv venv
source venv/bin/activate
pip install setuptools wheel build twine
python setup.py sdist bdist_wheel
```

### 4. Проверьте пакет

```bash
python -m twine check dist/*
```

### 5. Опубликуйте на Test PyPI

```bash
python -m twine upload --repository testpypi dist/*
```

### 6. Протестируйте установку

```bash
pip install --index-url https://test.pypi.org/simple/ contentgem-python
contentgem --help
```

### 7. Опубликуйте на PyPI

```bash
python -m twine upload dist/*
```

## 📦 Что получится

После публикации пользователи смогут:

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

## 🔧 Автоматизация

Используйте скрипт `build.py` для автоматизации:

```bash
# Полный цикл: очистка, сборка, проверка, публикация на Test PyPI
python build.py --all

# Публикация на основной PyPI
python build.py --publish
```

## 📋 Проверочный список

- [ ] Аккаунты на PyPI и Test PyPI созданы
- [ ] API токены настроены в `~/.pypirc`
- [ ] Пакет собран (`dist/` содержит `.whl` и `.tar.gz`)
- [ ] Пакет проверен (`twine check` прошел успешно)
- [ ] Тестовая публикация на Test PyPI прошла успешно
- [ ] Установка с Test PyPI работает
- [ ] Публикация на основной PyPI прошла успешно
- [ ] Установка с PyPI работает

## 🎉 Готово!

После выполнения всех шагов ваш пакет будет доступен для установки через:

```bash
pip install contentgem-python
```

И пользователи смогут использовать его в своих проектах!
