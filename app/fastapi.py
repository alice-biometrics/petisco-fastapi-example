import os

from elasticapm.contrib.starlette import ElasticAPM, make_apm_client
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app import APPLICATION_NAME, ENVIRONMENT
from app.api import checks, tasks
from app.api.openapi import FASTAPI_PREFIX, OPENAPI_TAGS


def fastapi_configurer() -> FastAPI:
    def configure_apm(app):
        apm_config = {
            "SERVICE_NAME": APPLICATION_NAME,
            "SERVER_URL": os.environ.get("ELASTIC_APM_SERVER_HOST"),
            "SECRET_TOKEN": os.environ.get("ELASTIC_APM_SECRET_TOKEN"),
            "ENVIRONMENT": ENVIRONMENT,
        }
        apm = make_apm_client(apm_config)
        app.add_middleware(ElasticAPM, client=apm)

    docs_url = f"{FASTAPI_PREFIX}/docs"
    app = FastAPI(
        title=APPLICATION_NAME,
        openapi_tags=OPENAPI_TAGS,
        docs_url=docs_url,
        openapi_url=f"{FASTAPI_PREFIX}/openapi.json",
    )
    app.include_router(checks.router, prefix=FASTAPI_PREFIX)
    app.include_router(tasks.router, prefix=FASTAPI_PREFIX)

    app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
    )
    apm_enabled = ENVIRONMENT in ["production", "staging"]
    if apm_enabled:
        configure_apm(app)

    return app
