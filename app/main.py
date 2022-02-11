from loguru import logger

from app.application import application

application.configure()
app = application.get_app()


@app.on_event("startup")
async def startup_event():
    logger.info("Everything is working!!")
