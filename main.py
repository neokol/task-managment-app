from fastapi import FastAPI

app = FastAPI(
    title="Fast API Task Managment",
    description="Managing Tasks",
    version="0.0.1",
    contact={
        "name":"Neoklis Kollias",
        "email":"ineokol@gmail.com"
    }
)


@app.get("/")
async def root():
    return {"message": "Hello World"}