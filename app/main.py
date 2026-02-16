# main.py
from fastapi import FastAPI
from app.controllers.extractor_controller import router as extractor_router
from dotenv import load_dotenv

load_dotenv() # Carrega chaves do arquivo .env

app = FastAPI(title="LangChain MVC API")

# Inclui as rotas do controlador
app.include_router(extractor_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)