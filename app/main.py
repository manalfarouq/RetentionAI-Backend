from fastapi import FastAPI
from .routes import login_router, register_router, prediction_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


@app.get("/")
async def root():
    return {"message": "API Prediction Attrition"}


app.include_router(login_router.router)
app.include_router(register_router.router)
app.include_router(prediction_router.router)