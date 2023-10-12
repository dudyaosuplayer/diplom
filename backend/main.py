from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title='Project Managing API',
    description='',
    version='1.0.0'
)
# app.include_router(router=router)


# Run the FastAPI application
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8080, reload=True)
