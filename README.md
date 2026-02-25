# 🚀 API-test  
### Backend REST em Produção com PostgreSQL e Deploy no Google Cloud Run

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Cloud Run](https://img.shields.io/badge/Deploy-Google%20Cloud%20Run-lightgrey)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![Auth](https://img.shields.io/badge/Auth-Basic%20%7C%20OAuth-orange)

---

## 📖 Sobre o Projeto

A **API-test** é uma API backend desenvolvida em Python conectada a um banco PostgreSQL, implantada em ambiente serverless no Google Cloud Run.

O projeto demonstra:

- Desenvolvimento de API real conectada a banco relacional
- Implementação de autenticação (Basic e OAuth)
- Containerização com Docker
- Deploy em ambiente cloud produtivo
- Integração com banco gerenciado

---

## 🎯 Objetivo

Criar uma API backend funcional conectada a banco PostgreSQL, preparada para ambiente de produção e estruturada para escalabilidade em nuvem.

---

## 🏗️ Arquitetura
Cliente / API Consumer
↓
API-test (Python Backend)
↓
Cloud Run (Serverless Container)
↓
Cloud SQL / PostgreSQL


### Características da Arquitetura

- Deploy serverless
- Escalonamento automático
- Banco relacional gerenciado
- Containerização padronizada
- Separação clara entre aplicação e infraestrutura

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia |
|--------|------------|
| Linguagem | Python |
| Backend | Framework Web Python |
| Banco de Dados | PostgreSQL |
| Cloud | Google Cloud Run |
| Containerização | Docker |
| Autenticação | HTTP Basic + OAuth |
| Versionamento | GitHub |

---

## 🔐 Autenticação

A API suporta dois métodos:

### 1️⃣ HTTP Basic Auth
- Autenticação simples via header Authorization
- Base64 encoding (username:password)

### 2️⃣ OAuth
- Fluxo baseado em token
- Proteção de endpoints via validação de credencial

Isso demonstra controle de acesso e proteção de recursos da API.

---

## 🗄️ Banco de Dados

Banco: **PostgreSQL**

Características:

- Conexão via variáveis de ambiente
- Persistência relacional
- Estrutura preparada para ambiente cloud
- Compatível com Cloud SQL

---

## ⚙️ Execução Local

### 1️⃣ Clonar repositório

bash
git clone https://github.com/EricDiasLemos/API-test.git
cd API-test


### Características da Arquitetura

- Deploy serverless
- Escalonamento automático
- Banco relacional gerenciado
- Containerização padronizada
- Separação clara entre aplicação e infraestrutura

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia |
|--------|------------|
| Linguagem | Python |
| Backend | Framework Web Python |
| Banco de Dados | PostgreSQL |
| Cloud | Google Cloud Run |
| Containerização | Docker |
| Autenticação | HTTP Basic + OAuth |
| Versionamento | GitHub |

---

## 🔐 Autenticação

A API suporta dois métodos:

### 1️⃣ HTTP Basic Auth
- Autenticação simples via header Authorization
- Base64 encoding (username:password)

### 2️⃣ OAuth
- Fluxo baseado em token
- Proteção de endpoints via validação de credencial

Isso demonstra controle de acesso e proteção de recursos da API.

---

## 🗄️ Banco de Dados

Banco: **PostgreSQL**

Características:

- Conexão via variáveis de ambiente
- Persistência relacional
- Estrutura preparada para ambiente cloud
- Compatível com Cloud SQL

---

## ⚙️ Execução Local

### 1️⃣ Clonar repositório

bash
git clone https://github.com/EricDiasLemos/API-test.git
cd API-test

2️⃣ Criar ambiente virtual
python -m venv venv
venv\Scripts\activate
3️⃣ Instalar dependências
pip install -r requirements.txt
4️⃣ Executar aplicação
python app.py
🐳 Execução com Docker
Build da imagem
docker build -t api-test .
Run do container
docker run -p 8080:8080 api-test
☁️ Deploy no Cloud Run

A aplicação está publicada em ambiente serverless no Google Cloud Run.

Características do deploy:

Container Docker

Build via source ou imagem

Escalonamento automático

Integração com PostgreSQL (Cloud SQL)

Revisões versionadas

🌐 Ambiente de Produção

Executando em Cloud Run

Banco PostgreSQL gerenciado

Acesso protegido por autenticação

Pronta para integração com outros serviços

📈 Pontos Técnicos Relevantes

Integração backend + banco relacional

Deploy real em nuvem

Configuração via variáveis de ambiente

Separação entre ambiente local e produção

Estrutura pronta para CI/CD futuro

🔮 Possíveis Evoluções

Implementação de pipeline CI/CD

Logs estruturados

Monitoramento com métricas

Rate limiting

Documentação OpenAPI/Swagger

Testes automatizados

🧠 Competências Demonstradas

Backend Engineering

Integração com PostgreSQL

Segurança e autenticação

Containerização

Deploy serverless

Arquitetura cloud

👤 Autor

Eric Dias
Cloud & DevOps Engineer
GitHub: https://github.com/EricDiasLemos
