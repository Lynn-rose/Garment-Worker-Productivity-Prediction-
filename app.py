from fastapi import FastAPI, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/images", StaticFiles(directory="app/static/images"), name="images")
templates = Jinja2Templates(directory="app/templates")

# Load the pre-trained model (Random Forest)
with open('productivity.pkl', 'rb') as file:
    model = pickle.load(file)

@app.post("/predict/")
def predict(quarter: float = Form(...), 
            department: float = Form(...), 
            team: float = Form(...),
            targeted_productivity: float = Form(...),
            smv: float = Form(...),
            wip: float = Form(...),
            over_time: float = Form(...),
            incentive: float = Form(...),
            idle_time: float = Form(...),
            idle_men: float = Form(...),
            no_of_style_change: float = Form(...),
            no_of_workers: float = Form(...)):
    try:
        productivity = {
            "quarter": quarter,
            "department": department,
            "team": team,
            "targeted_productivity": targeted_productivity,
            "smv": smv,
            "wip": wip,
            "over_time": over_time,
            "incentive": incentive,
            "idle_time": idle_time,
            "idle_men": idle_men,
            "no_of_style_change": no_of_style_change,
            "no_of_workers": no_of_workers
        }

        results = {}
        df = pd.DataFrame([productivity])
        results["production"] = (round(predict_los(df).item()))
        print(results)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error: " + str(e))

def predict_los(production_data):
    production_data_transformed = los_preprocessor.transform(production_data)
    return model.predict(production_data_transformed)[0]