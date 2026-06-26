"""Routes Package"""

from app.routes.animals import router as animals_router
from app.routes.hatchery import router as hatchery_router
from app.routes.medicines import router as medicines_router
from app.routes.costs import router as costs_router

__all__ = ["animals_router", "hatchery_router", "medicines_router", "costs_router"]
