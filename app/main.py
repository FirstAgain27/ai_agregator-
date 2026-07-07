from fastapi import FastAPI

app = FastAPI(title="LLM Agregator")

@app.get("/health")
def health():
    return {"Health status is alive)"}


