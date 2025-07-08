#Fabio Leandro Lapuinka 08/07/2025
#Moc Estados Brasileiros

print('http://localhost:8000/api/ibge/uf/v1/')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="API Mock IBGE Estados",
    description="Mock da API de Estados Brasileiros do IBGE",
    version="1.0.0"
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos Pydantic
class Regiao(BaseModel):
    id: int
    sigla: str
    nome: str

class Estado(BaseModel):
    id: int
    sigla: str
    nome: str
    regiao: Regiao

# Dados mockados
estados_data = [
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
    },
    {
        "id": 13,
        "sigla": "AM",
        "nome": "Amazonas",
        "regiao": {
            "id": 1,
            "sigla": "N",
            "nome": "Norte"
        }
    },
    {
        "id": 14,
        "sigla": "RR",
        "nome": "Roraima",
        "regiao": {
            "id": 1,
            "sigla": "N",
            "nome": "Norte"
        }
    },
    {
        "id": 15,
        "sigla": "PA",
        "nome": "Pará",
        "regiao": {
            "id": 1,
            "sigla": "N",
            "nome": "Norte"
        }
    }
]

@app.get("/api/ibge/uf/v1/", response_model=List[Estado])
async def listar_estados():
    """Retorna todos os estados brasileiros"""
    return estados_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)