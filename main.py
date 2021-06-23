import asyncio
from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, validator, StrictInt

tags_metadata = [
    {
        "name": "bmi",
        "description": "Calculate BMI Using Height + Weight data, will return a bmi score alongside with a label"
    }
]

app = FastAPI(
    title="Simple BMI Calculator",
    description="A Simple BMI Calculator REST API",
    openapi_tags=tags_metadata
)

class Human(BaseModel):
    height: StrictInt
    weight: StrictInt

    @validator('height')
    def height_must_be_greater_than_0(cls, v):
        if v <= 0:
            raise ValueError('Height must be greater than 0')
        return v

    @validator('weight')
    def weight_must_be_greater_than_0(cls, v):
        if v <= 0:
            raise ValueError('Weight must be greater than 0')
        return v

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/bmi", tags=['bmi'])
async def calculate_bmi(human: Human):
    # Rumus BMI -> KG/M^2 (Tinggi di convert dr CM ke M)
    bmi=float('{:.1f}'.format(human.weight/(human.height/100)**2))
    if bmi > 25:
        label='Overweight'
    elif bmi <  25 and bmi >= 18.5:
        label='Healthy'
    else:
        label='Underweight'
    return {'bmi': bmi, 'label': label}
