from fastapi import FastAPI

from fastapi_ddd_sample.container import Container
from fastapi_ddd_sample.api import router

app = FastAPI()

container = Container()
container.wire(modules=[router])
app.container = container

app.include_router(router.router)
