from fastapi import FastAPI

app = FastAPI(
    title="PastryManager API",
    description="API para la gestión de pedidos, productos y clientes de una pastelería.",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}