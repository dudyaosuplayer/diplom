from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from backend.utils.fastapi.router import add_routers

app = FastAPI(
    title='Project Managing API',
    description='',
    version='1.0.0'
)
add_routers(app)

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Run the FastAPI application
if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8080, reload=True)