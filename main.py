
import pandas as pd
from fastapi import FastAPI, status, HTTPException
import joblib
from fastapi.responses import JSONResponse

app = FastAPI(
    title="deploy_Obesity",
    version="0.0.1"
)
#-------------------------------------------------
#load model
#--------------------------------------------------
model = joblib.load("model/logistic_reg_vol1.pkl")
@app.post("/api/v1/deploy_Obesity", tags=["Deploy Obesity"])
async def predict(
    Age,
    Height,
    Weight,
    NCP,
    CH2O,
    FAF,
    TUE,
    NObeyesdad,
    Gender_Female,
    Gender_Male,
    CALC_no,
    MTRANS_Automobile,
    MTRANS_Bike,
    MTRANS_Motorbike,
    MTRANS_Public_Transportation,
    MTRANS_Walking,
    FAVC_no,
    FAVC_yes,
    family_history_with_overweight_no,
    family_history_with_overweight_yes

, srt=None):

    data = ['Age', 'Height', 'Weight', 'NCP', 'CH2O', 'FAF', 'TUE', 'NObeyesdad',
            'Gender_Female', 'Gender_Male', 'CALC_no', 'MTRANS_Automobile',
            'MTRANS_Bike', 'MTRANS_Motorbike', 'MTRANS_Public_Transportation',
            'MTRANS_Walking', 'FAVC_no', 'FAVC_yes', 'family_history_with_overweight_no',
            'family_history_with_overweight_yes'
            ]
    try:
     df = pd.DataFrame(data, index=[0])
     prediction = model.predict(df)
     return JSONResponse(
        content=prediction[1,2,3,4],
        status_code= status.HTTP_200_OK
      )

    except Exception as e:
        raise HTTPException(
         status_code=status.HTTP_400_BAD_REQUEST,
         detal= srt(e)
       )