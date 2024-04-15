
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

#--------------------------------------------------------------------------------------------------------------

@app.get("/api/v1/deploy_Obesity/predict_single", tags=["Deploy Obesity"])
async def predict_single(
    Age: float,
    Height: float,
    Weight: float,
    NCP: float,
    CH2O: float,
    FAF: float,
    TUE: float,
    NObeyesdad: str,
    Gender_Female: int,
    Gender_Male: int,
    CALC_no: int,
    MTRANS_Automobile: int,
    MTRANS_Bike: int,
    MTRANS_Motorbike: int,
    MTRANS_Public_Transportation: int,
    MTRANS_Walking: int,
    FAVC_no: int,
    FAVC_yes: int,
    family_history_with_overweight_no: int,
    family_history_with_overweight_yes: int
):
    try:

        data = {
            'Age': [Age],
            'Height': [Height],
            'Weight': [Weight],
            'NCP': [NCP],
            'CH2O': [CH2O],
            'FAF': [FAF],
            'TUE': [TUE],
            'NObeyesdad': [NObeyesdad],
            'Gender_Female': [Gender_Female],
            'Gender_Male': [Gender_Male],
            'CALC_no': [CALC_no],
            'MTRANS_Automobile': [MTRANS_Automobile],
            'MTRANS_Bike': [MTRANS_Bike],
            'MTRANS_Motorbike': [MTRANS_Motorbike],
            'MTRANS_Public_Transportation': [MTRANS_Public_Transportation],
            'MTRANS_Walking': [MTRANS_Walking],
            'FAVC_no': [FAVC_no],
            'FAVC_yes': [FAVC_yes],
            'family_history_with_overweight_no': [family_history_with_overweight_no],
            'family_history_with_overweight_yes': [family_history_with_overweight_yes]
        }
        df = pd.DataFrame(data)


        prediction = model.predict(df)

        return JSONResponse(
            content=prediction.tolist(),
            status_code=status.HTTP_200_OK
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e))





