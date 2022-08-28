from fastapi import FastAPI
from loguru import logger
from starlette_prometheus import metrics, PrometheusMiddleware

from app.core.config import get_settings
from app.core.logging import configure_logger
from app.routes.api import router as api_router


def create_app():
    """
    Application factory
    """
    try:
        # initialization
        settings = get_settings()
        configure_logger(settings)
        logger.info("Dependencies initialization completed")
    except Exception as e:
        # don't continue if initialization fails
        logger.error(f"Error initializing app, Exception: {e}")
        exit(1)

    # create app and include routes
    app = FastAPI()
    app.add_middleware(PrometheusMiddleware)
    app.add_route("/metrics", metrics)
    app.include_router(api_router)

    return app
