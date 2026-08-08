from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse
from app.core.exceptions import AppException

app = FastAPI(title="LLM Agregator")

@app.get("/health")
def health():
    return {"Health status is alive)"}

# Перехватывает AppException И ВСЕ ЕГО ДОЧЕРНИЕ КЛАССЫ!
@app.exception_handler(AppException)
async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
