from fastapi import FastAPI
from app.controllers import usuarios_controller
from app.database.db import Base, engine

import uvicorn

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuarios_controller.router)

@app.get("/")
def read_root():

    return {"Hello": "World"}

def main():

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)



if __name__ == "__main__":

    main()