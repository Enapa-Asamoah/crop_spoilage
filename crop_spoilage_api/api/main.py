from fastapi import FastAPI
from routers import predict

app = FastAPI()

# Register router
app.include_router(predict.router)

# Optional: root endpoint
@app.get("/")
def read_root():
    return {"message": "Crop Spoilage Prediction API is running"}
