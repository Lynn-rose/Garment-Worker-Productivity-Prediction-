from fastapi import FastAPI, Form, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from enum import Enum
import pickle
import pandas as pd
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/images", StaticFiles(directory="app/static/images"), name="images")
templates = Jinja2Templates(directory="app/templates")

# Load the pre-trained model (Random Forest)
with open('productivity.pkl', 'rb') as file:
    model = pickle.load(file)
with open('preprocessor.pkl', 'rb') as file:
    production_preprocessor = pickle.load(file)

@app.get("/")
async def api_demo(request: Request):
    
    return templates.TemplateResponse("index.html", context={
        "request": request,
        "title": "Garment Worker Productivity Prediction",
        "description": "This application predicts the productivity of garment workers based on various input factors like quarter, department, team, and more."
        
    })
class QuarterEnum(str, Enum):
    Q1 = "Q1"
    Q2 = "Q2"
    Q3 = "Q3"
    Q4 = "Q4"

class DepartmentEnum(str, Enum):
    sewing = "Sewing"
    finishing = "Finishing"

class ProductivityInput(BaseModel):
    quarter: str
    department: str
    team: float
    targeted_productivity: float
    smv: float
    wip: float
    over_time: float
    incentive: float
    idle_time: float
    idle_men: float
    no_of_style_change: float
    no_of_workers: float

@app.post("/predict")
def predict(input_data: ProductivityInput):
    try:
        print("Received Input Data:", input_data)  # Logs the input data
        print("Parsed Input Dictionary:", input_data.dict())  # Logs the dictionary representation

        # Convert input to DataFrame
        productivity = pd.DataFrame([input_data.dict()])
        print("DataFrame Structure:\n", productivity)  # Logs the DataFrame
        print("Input DataFrame Columns:", productivity.columns)
        print("Input DataFrame dtypes:\n", productivity.dtypes)

        # Transform the data
        production_data_transformed = production_preprocessor.transform(productivity)
        print("Transformed Data:\n", production_data_transformed)  # Logs the transformed data
        print("Preprocessor Expected Columns:", production_preprocessor.feature_names_in_)


        # Predict the output
        prediction = model.predict(production_data_transformed)[0]
        print("Prediction Result:", prediction)  # Logs the prediction

        return {"prediction": round(prediction, 2)}
    except Exception as e:
        print("Error occurred:", str(e))  # Logs the exact error
        raise HTTPException(status_code=500, detail="Error: " + str(e))


def predict_los(production_data):
    production_data_transformed = production_preprocessor.transform(production_data)
    return model.predict(production_data_transformed)[0]

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)