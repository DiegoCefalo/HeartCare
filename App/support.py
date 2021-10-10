import streamlit as st
import streamlit.components.v1 as components
import PIL.Image as Image
import pandas as pd
import pickle


model = pickle.load(open('../model/finalized_model.sav', 'rb'))

title = Image.open('../img/Screenshot_3.png')

col1, col2 = st.columns([1, 5])

with col1:
    st.image("https://www.heartcare.life/assets/images/logo/logo-heart-care.jpg", width = 100)
with col2:
    st.image(title, width = 300)

components.html("""<div style="text-align: justify">Esta es una aplicación creada para uso médico y no para auto-diagnóstico. Si presenta alguna sintomatología o sospecha de tener alguna enfermedad cardiovascular, por favor consulte con su médico de cabecera</div>""")

age = st.number_input("Edad (años):", step=1)

sex = st.radio("Sexo:", ['Masculino', 'Femenino'])


type_pain = st.selectbox("Tipo de Dolor de Pecho:", ["Angina Típica", "Angina Atípica", "Dolor No Anginal", "Asintomático"])


restingbp = st.number_input("Presión Arterial en Reposo (mmHg):", step=1)

cholesterol = st.number_input("Colesterol (mg/dl):", step=1)

blood_sugar = st.radio("Glucemia en Ayunas:", ['Mayor a 120 mg/dl', 'Menor a 120 mg/dl'])


ecg = st.selectbox("Electrocardiograma en reposo:", ["Normal", "Anormalidad ST (Inversiones, Elevaciones o Depresiones de más de 0,05 mV)", "Hypertrofia ventricular probable o definitiva"])

maxhr = st.number_input("Máximo Ritmo Cardiaco:", step=1)

exercise_angina = st.radio("Angina por Ejercicio:", ['Yes', 'No'])


oldpeak = st.number_input("Depresión ST producto de sedentarismo:")

slope = st.selectbox("Inclinación de la pendiente ST:", ["Creciente", "Plana", "Decreciente"])
    

if st.button("Predecir"):
    
    
    if sex == 'Masculino':
        sex = 1
    else:
        sex = 0
    
    if type_pain == "Angina Atípica":
        type_pain1 = 1
    else:
        type_pain1 = 0
    if type_pain == "Dolor No Anginal":
        type_pain2 = 1
    else:
        type_pain2 = 0
    if type_pain == "Angina Típica":
        type_pain3 = 1
    else:
        type_pain3 = 0
    
    
    if  blood_sugar == 'Mayor a 120 mg/dl':
        blood_sugar = 1
    else:
        blood_sugar = 0
    
    
    if  exercise_angina ==  'Yes':
        exercise_angina = 1
    else:
        exercise_angina = 0
    
    
    if  ecg == "Normal":
        ecg1 = 1
    else:
        ecg1 = 0
    if  ecg ==  "Anormalidad ST (Inversiones, Elevaciones o Depresiones de más de 0,05 mV)":
        ecg2 = 1
    else:
        ecg2 = 0
    
    
    
    if  slope ==  "Plana":
        slope1 = 1
    else:
        slope1 = 0
    if  slope ==  "Creciente":
        slope2 = 1
    else:
        slope2 = 0
        
       
    variables = {'Age':age, 'RestingBP':restingbp, 'Cholesterol':cholesterol, 'FastingBS':blood_sugar, 'MaxHR':maxhr, 'Oldpeak':oldpeak, 'Sex_M':sex, 'ChestPainType_ATA':type_pain1, 'ChestPainType_NAP':type_pain2, 'ChestPainType_TA':type_pain3, 'RestingECG_Normal':ecg1, 'RestingECG_ST':ecg2, 'ExerciseAngina_Y':exercise_angina, 'ST_Slope_Flat':slope1, 'ST_Slope_Up':slope2}
    series = pd.Series(variables)
    feed = pd.DataFrame(series).transpose()
    prediction = model.predict_proba(feed)
    st.write(f"# Tiene un {round(prediction[0][1]*100,1)}% de probabilidad de tener alguna enfermedad cardiovascular no diagnosticada")
