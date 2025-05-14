from fastapi import FastAPI
from app.api import api_router


app = FastAPI(
    title="Image Processing API",
    description="API to process images: convert to black and white, remove background"
)

@app.get('/')
def start_up():
     return ({'I AM':'Alive'})
#test
app.include_router(api_router,prefix='/api')