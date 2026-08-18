from fastapi import FastAPI, Request 
from fastapi.responses import JSONResponse
from core.exceptions import AppException
from api.v1.auth import router as auth_router

app = FastAPI(title="LLM Agregator")

app.include_router(auth_router)

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
