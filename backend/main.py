from fastapi import FastAPI

from .routers import items, users, tasks

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
