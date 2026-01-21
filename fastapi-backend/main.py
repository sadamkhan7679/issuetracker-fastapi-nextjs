from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Import Routers
from app.routes.issues import router as issues_router

# Import Middleware
from app.middleware.timer import timer_middleware

# Create FastAPI instance
app = FastAPI()
# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Middleware
app.middleware("http")(timer_middleware)


# Define a root endpoint
# @app.get("/root")
# async def read_root():
#     return {"Hello": "World"}


# Include Routers
app.include_router(issues_router)



# Define a sample endpoint
# @app.get("/items/{item_id}")
# async def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}
#
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)
