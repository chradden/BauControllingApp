
from fastapi import FastAPI
from .api.routes.health import router as health_router

app = FastAPI(title="Bau-Controlling API", version="0.1.0")

app.include_router(health_router, prefix="")

# TODO: include routers for projects, contracts, invoices, users
