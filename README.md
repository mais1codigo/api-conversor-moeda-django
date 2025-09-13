# API Conversor de Moedas com Django

Este é um projeto estuantil e feito como pratica individual para meu conhecimento full-stack que consiste em uma API RESTful construída com Django para conversão de moedas e um frontend simples em HTML, CSS e JavaScript para consumir essa API.

## ✨ Features

- Backend robusto construído com Django.
- API para conversão de valores entre diferentes moedas (BRL, USD, EUR).
- Frontend interativo para consumir a API de forma amigável.
- Configuração de CORS para permitir a comunicação segura entre o frontend e o backend em domínios diferentes.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript (puro)

## 📋 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/) (geralmente já vem com o Python)
- [Git](https://git-scm.com/downloads)

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar o projeto localmente.

### 1. Clonar o Repositório

```bash
git clone https://github.com/mais1codigo/api-conversor-moeda-django.git
cd api-conversor-moeda-django```

### 2. Configurar o Backend

```bash
# Crie e ative um ambiente virtual
# No Windows:
python -m venv venv
.\venv\Scripts\activate

# No macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Instale as dependências do projeto
pip install -r requirements.txt

# Aplique as migrações do banco de dados
python manage.py migrate

# Crie um superusuário para acessar o Admin do Django (opcional)
python manage.py createsuperuser
```

### 3. Executar o Projeto

Você precisará de **dois terminais** abertos para rodar o backend e o frontend simultaneamente.

**Terminal 1 - Rodando o Backend (API):**
```bash
python manage.py runserver
```
O servidor Django estará rodando em `http://127.0.0.1:8000`.

**Terminal 2 - Rodando o Frontend:**

Para o frontend, a forma mais simples é usar a extensão **Live Server** no Visual Studio Code.
1. Abra a pasta do projeto no VS Code.
2. Navegue até o arquivo `conversor_front/index.html`.
3. Clique com o botão direito sobre o arquivo e selecione **"Open with Live Server"**.

Isso abrirá o frontend no seu navegador, geralmente no endereço `http://127.0.0.1:5500`. Agora você pode usar o conversor!

## 🔗 Uso da API

O endpoint principal para a conversão é:

`GET /api/converter/`

**Parâmetros:**
- `valor` (float): O valor a ser convertido.
- `de` (string): A sigla da moeda de origem (ex: `USD`).
- `para` (string): A sigla da moeda de destino (ex: `BRL`).

**Exemplo de requisição:**
```
http://127.0.0.1:8000/api/converter/?valor=50&de=BRL&para=USD
```

**Exemplo de resposta de sucesso:**
```json
{
    "valor_original": 50.0,
    "moeda_origem": "BRL",
    "moeda_destino": "USD",
    "taxa_utilizada": 0.185488,
    "resultado_conversao": 9.27
}
```