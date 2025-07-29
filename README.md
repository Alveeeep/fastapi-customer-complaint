## Для ChatGPT:

- В файле utils/ai_api.py убрать строчку base_url, если используется ключ напрямую от OpenAi
- В .env файл добавить OPENAI_TOKEN= ваш ключ

## Для анализа тональности:

- В .env файл добавить SENTIMENT_TOKEN= ваш ключ

## Пример .env файла:
```
OPENAI_TOKEN=
SENTIMENT_TOKEN=
PROXY_URL=http://login:pass@127.0.0.1:8000 # добавляется при необходимости, но в коде используется промежуточый сервис между openai
```

## Настройка n8n
- Создать .env файл в папке n8n-compose и изменить параметры для себя
- [Полная документация по разворачиванию локального n8n](https://docs.n8n.io/hosting/installation/server-setups/docker-compose)
```
# DOMAIN_NAME and SUBDOMAIN together determine where n8n will be reachable from
# The top level domain to serve from
DOMAIN_NAME=example.com

# The subdomain to serve from
SUBDOMAIN=n8n

# The above example serve n8n at: https://n8n.example.com

# Optional timezone to set which gets used by Cron and other scheduling nodes
# New York is the default value if not set
GENERIC_TIMEZONE=Europe/Berlin

# The email address to use for the TLS/SSL certificate creation
SSL_EMAIL=user@example.com
```
- Создать директорию на сервере или локальном компьютере в папке n8n-compose
```shell
mkdir local-files
```

# Запуск

## Запуск n8n
```shell
sudo docker compose -f n8n-compose.yaml -d
```

## Запуск основного приложения
```shell
sudo docker compose up -d --build
```
