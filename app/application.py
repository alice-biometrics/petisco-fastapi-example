from petisco.extra.fastapi import FastApiApplication

from app import (
    APPLICATION_LATEST_DEPLOY,
    APPLICATION_NAME,
    APPLICATION_VERSION,
    ORGANIZATION,
)
from app.fastapi import fastapi_configurer
from app.petisco.configurers import configurers
from app.petisco.dependencies import dependencies_provider

application = FastApiApplication(
    name=APPLICATION_NAME,
    version=APPLICATION_VERSION,
    organization=ORGANIZATION,
    deployed_at=APPLICATION_LATEST_DEPLOY,
    dependencies_provider=dependencies_provider,
    configurers=configurers,
    fastapi_configurer=fastapi_configurer,
)
