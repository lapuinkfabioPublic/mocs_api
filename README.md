API Mock IBGE Estados Brasileiros
https://img.shields.io/badge/Python-3.8+-blue.svg
https://img.shields.io/badge/FastAPI-0.68.1-green.svg
https://img.shields.io/badge/License-MIT-yellow.svg

API mock para simular o endpoint /api/ibge/uf/v1/ da BrasilAPI, retornando dados de estados brasileiros com suas regiões.

📋 Pré-requisitos
Python 3.8+

pip

Virtualenv (recomendado)

🚀 Instalação
Clone o repositório:

bash
git clone https://github.com/seu-usuario/api-mock-ibge.git
cd api-mock-ibge
Crie e ative um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate no Windows
Instale as dependências:

bash
pip install -r requirements.txt
🏃 Executando a API
Modo desenvolvimento (com reload automático):
bash
uvicorn main:app --reload
Modo produção:
bash
python main.py
A API estará disponível em: http://localhost:8000

📚 Endpoints
GET /api/ibge/uf/v1/
Retorna a lista de estados brasileiros com suas respectivas regiões.

Exemplo de resposta:

json
[
  {
    "id": 11,
    "sigla": "RO",
    "nome": "Rondônia",
    "regiao": {
      "id": 1,
      "sigla": "N",
      "nome": "Norte"
    }
  },
  {
    "id": 12,
    "sigla": "AC",
    "nome": "Acre",
    "regiao": {
      "id": 1,
      "sigla": "N",
      "nome": "Norte"
    }
  }
]
🧪 Testes
Para executar os testes unitários:

bash
pytest -v
Para executar os testes com cobertura:

bash
pytest --cov=.
🌐 Documentação Interativa
A API inclui documentação automática gerada pelo Swagger UI e ReDoc:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

⚙️ Configuração
As configurações podem ser alteradas através do arquivo .env:

ini
DEBUG=true
PORT=8000
ALLOWED_ORIGINS=http://localhost:4200
🛠 Tecnologias Utilizadas
FastAPI - Framework para construção da API

Uvicorn - Servidor ASGI

Pydantic - Validação de dados

Pytest - Testes unitários

🤝 Contribuição
Contribuições são bem-vindas! Siga os passos:

Faça um fork do projeto

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

📄 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.
