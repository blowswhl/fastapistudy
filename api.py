from fastapi import FastAPI
from todo    import todo_router,todo_list

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
        "message": "Hello World" 
    }

app.include_router(todo_router)

app.get("/todo")
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }