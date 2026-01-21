from fastapi import FastAPI;

# Import Routers
from app.routes.issues import router as issues_router

# Create FastAPI instance
app = FastAPI()


# Define a root endpoint
# @app.get("/root")
# async def read_root():
#     return {"Hello": "World"}


app.include_router(issues_router)



# Define a sample endpoint
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
