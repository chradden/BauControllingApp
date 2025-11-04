from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from .api.routes.health import router as health_router
from .api.routes.projects import router as projects_router
from .api.routes.contracts import router as contracts_router
from .api.routes.invoices import router as invoices_router
from .api.routes.users import router as users_router

app = FastAPI(title="Bau-Controlling API", version="0.1.0")

# CORS-Konfiguration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, prefix="")
app.include_router(projects_router)
app.include_router(contracts_router)
app.include_router(invoices_router)
app.include_router(users_router)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")
