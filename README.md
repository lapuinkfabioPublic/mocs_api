API mock para simular o endpoint /api/ibge/uf/v1/ da BrasilAPI, retornando dados de estados brasileiros com suas regiões.

🚀 Começando
📋 Pré-requisitos
Python 3.8+

pip

Virtualenv (recomendado)

🔧 Instalação
Clone o repositório:

bash
git clone https://github.com/seu-usuario/api-mock-ibge.git
cd api-mock-ibge
Configure o ambiente virtual:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
ou venv\Scripts\activate no Windows
Instale as dependências:

bash
pip install -r requirements.txt
🏃‍♂️ Execução
Modo Desenvolvimento (com reload automático):
bash
uvicorn main:app --reload
Modo Produção:
bash
python main.py
A API estará disponível em: http://localhost:8000

📚 Documentação da API
Endpoints
GET /api/ibge/uf/v1/
Retorna a lista completa de estados brasileiros com suas respectivas regiões.

Exemplo de Resposta:

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
Execute os testes com:

bash
pytest -v
Para ver a cobertura de testes:

bash
pytest --cov=.
🌐 Documentação Interativa
Acesse nossa documentação automática:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

⚙️ Configuração
Configure sua aplicação através do arquivo .env:

ini
DEBUG=true
PORT=8000
ALLOWED_ORIGINS=http://localhost:4200
🛠 Stack Tecnológica
FastAPI - Framework web moderno

Uvicorn - Servidor ASGI de alta performance

Pydantic - Validação de dados e modelagem

Pytest - Framework de testes

Python-dotenv - Gerenciamento de variáveis de ambiente

🤝 Como Contribuir
Faça um fork do projeto

Crie sua branch (git checkout -b feature/nova-feature)

Commit suas alterações (git commit -m 'Adiciona nova feature')

Push para a branch (git push origin feature/nova-feature)

Abra um Pull Request
