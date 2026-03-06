🍽️ OO Sabor Express API

API desenvolvida em Python + FastAPI que consome dados de uma API pública de restaurantes e disponibiliza endpoints para consulta e busca.

O projeto começou como um exercício de Programação Orientada a Objetos e evoluiu para uma API REST funcional, aplicando conceitos de arquitetura modular e consumo de APIs externas.

📌 Objetivo do Projeto

Criar uma API que permita:

Listar restaurantes

Buscar restaurantes por categoria

Buscar restaurantes por nome

Consultar restaurante específico pelo ID

Os dados são obtidos de uma API pública externa e transformados em objetos da aplicação.

🧠 Conceitos Aplicados

Programação Orientada a Objetos (POO)

Consumo de APIs externas (requests)

Desenvolvimento de API REST

FastAPI

Estrutura modular de projeto

Separação de responsabilidades

Manipulação de listas e objetos

Busca e filtragem de dados

🧱 Estrutura do Projeto
OO-Sabor-Express
│
├── main.py                 # API FastAPI
│
├── modelos
│   └── restaurante.py      # Classe Restaurante
│
├── servicos
│   └── api_restaurantes.py # Consumo da API externa
│
├── utils
│   ├── buscas.py           # Funções de busca
│   └── formatador.py       # Exibição de dados
│
└── venv                    # Ambiente virtual
🌐 API utilizada

Os dados dos restaurantes são obtidos da API pública:

https://fakerestaurantapi.runasp.net/api/Restaurant
🚀 Endpoints disponíveis
Listar todos os restaurantes
GET /restaurantes
Buscar restaurantes por categoria
GET /restaurantes/buscar?categoria=Biryani
Buscar restaurantes por nome
GET /restaurantes/buscar-nome?nome=Paradise
Buscar restaurante por ID
GET /restaurantes/{id}

Exemplo:

GET /restaurantes/1

▶️ Como Executar o Projeto
1️⃣ Clonar o repositório
git clone https://github.com/CbrunoS/OO-Sabor-Express.git

Entrar na pasta:

cd OO-Sabor-Express
2️⃣ Criar ambiente virtual

Linux / macOS

python3 -m venv venv
source venv/bin/activate

Windows

python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependências
pip install fastapi uvicorn requests

4️⃣ Executar a API
uvicorn main:app --reload

5️⃣ Acessar documentação automática

FastAPI gera automaticamente uma interface para testar a API:

http://127.0.0.1:8000/docs

👨‍💻 Autor

Projeto desenvolvido por Bruno Cardoso
Focado em transição de carreira para Desenvolvedor Python com foco em automação.

GitHub:
https://github.com/CbrunoS