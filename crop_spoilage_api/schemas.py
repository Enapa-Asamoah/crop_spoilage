from pydantic import BaseModel

class CropData(BaseModel):
    crop: str
    temperature: float
    humidity: float
    moisture: float
