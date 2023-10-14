import os.path
import sys

from fastapi import FastAPI
import uvicorn

from backend.utils.fastapi.router import add_routers

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

app = FastAPI(
    title='Project Managing API',
    description='',
    version='1.0.0'
)
add_routers(app)

# Run the FastAPI application
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True)
