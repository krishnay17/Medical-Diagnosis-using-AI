import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Set up page configuration
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Hide Streamlit default UI elements
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Add Background Image
background_image_url = "https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg"

st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url({background_image_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stAppViewContainer"]::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7);
    }}
    
    /* Enhanced Button Styling */
    .get-started-btn {{
        background: linear-gradient(45deg, #3498db, #1abc9c);
        color: white;
        padding: 12px 30px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 30px;
        border: none;
        cursor: pointer;
        margin: 20px auto;
        display: block;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        animation: pulse 1.5s infinite;
        width: 220px;
        text-align: center;
    }}
    
    .get-started-btn:hover {{
        transform: translateY(-5px);
        box-shadow: 0 7px 20px rgba(0, 0, 0, 0.3);
        background: linear-gradient(45deg, #2980b9, #16a085);
    }}
    
    /* Home Button Styling */
    .home-btn {{
        background: linear-gradient(45deg, #e74c3c, #f39c12);
        color: white;
        padding: 8px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 30px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        text-align: center;
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
    }}
    
    .home-btn:hover {{
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        background: linear-gradient(45deg, #c0392b, #e67e22);
    }}
    
    /* Custom styling for Streamlit buttons */
    div[data-testid="stButton"] > button:first-child {{
        background: linear-gradient(45deg, #3498db, #1abc9c);
        color: white;
        padding: 12px 30px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 30px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        animation: pulse 1.5s infinite;
        width: 220px;
        text-align: center;
    }}
    
    div[data-testid="stButton"] > button:first-child:hover {{
        transform: translateY(-5px);
        box-shadow: 0 7px 20px rgba(0, 0, 0, 0.3);
        background: linear-gradient(45deg, #2980b9, #16a085);
    }}
    
    /* Custom styling for home button */
    .home-button-container button {{
        background: linear-gradient(45deg, #e74c3c, #f39c12);
        color: white;
        padding: 8px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 30px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }}
    
    .home-button-container button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        background: linear-gradient(45deg, #c0392b, #e67e22);
    }}
    
    @keyframes pulse {{
        0% {{
            box-shadow: 0 0 0 0 rgba(52, 152, 219, 0.7);
        }}
        70% {{
            box-shadow: 0 0 0 15px rgba(52, 152, 219, 0);
        }}
        100% {{
            box-shadow: 0 0 0 0 rgba(52, 152, 219, 0);
        }}
    }}
    </style>
    """, unsafe_allow_html=True)

# Load trained models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Manage page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

# Page navigation functions
def navigate_to_main():
    st.session_state.page = 'main'
    
def navigate_to_welcome():
    st.session_state.page = 'welcome'

# Function for inputs
def display_input(label, tooltip, key, type="number"):
    return st.number_input(label, key=key, help=tooltip, step=1)

def display_title_with_info(title, info_text, key):
    st.subheader(title)
    if st.button('Disease Info', key=key):
        st.info(info_text)

# Welcome Page
if st.session_state.page == 'welcome':
    st.markdown("""
        <div style="text-align: center; color: white; padding: 50px;">
            <h1>Welcome to AI-based Medical Diagnosis System</h1>
            <p>An advanced tool for predicting various diseases using machine learning</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Single button with custom styling
        if st.button('Get Started →', on_click=navigate_to_main, key='get_started'):
            pass  # The on_click handler takes care of navigation

# Main Application Page
elif st.session_state.page == 'main':
    # Add home button in top right
    col_home = st.container()
    with col_home:
        st.markdown('<div class="home-button-container" style="position: fixed; top: 20px; right: 20px; z-index: 1000;">', unsafe_allow_html=True)
        if st.button('← Home', on_click=navigate_to_welcome, key='home_button'):
            pass  # The on_click handler takes care of navigation
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center; color: white; margin-bottom: 20px; padding-top: 30px;">
            <h1>AI-based Medical Diagnosis System</h1>
        </div>
    """, unsafe_allow_html=True)
    
    selected = st.selectbox(
        'Select a Disease to Predict',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Lung Cancer Prediction', 'Hypo-Thyroid Prediction']
    )

    # Diabetes Prediction
    if selected == 'Diabetes Prediction':
        display_title_with_info('Diabetes Prediction', "Diabetes causes high blood sugar levels due to insulin resistance or deficiency.", 'diabetes_info')

        Pregnancies = display_input('Number of Pregnancies', 'Number of times pregnant', 'Pregnancies')
        Glucose = display_input('Glucose Level', 'Blood glucose level', 'Glucose')
        BloodPressure = display_input('Blood Pressure', 'Diastolic blood pressure', 'BloodPressure')
        SkinThickness = display_input('Skin Thickness', 'Skin fold thickness', 'SkinThickness')
        Insulin = display_input('Insulin Level', 'Serum insulin level', 'Insulin')
        BMI = display_input('BMI', 'Body Mass Index', 'BMI')
        DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function', 'Genetic risk factor', 'DiabetesPedigreeFunction')
        Age = display_input('Age', 'Age in years', 'Age')

        if st.button('Check Diabetes'):
            prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            result = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
            st.success(result)

    # Heart Disease Prediction
    if selected == 'Heart Disease Prediction':
        display_title_with_info('Heart Disease Prediction', "Heart disease includes conditions like coronary artery disease, arrhythmia, and more.", 'heart_info')

        age = display_input('Age', 'Age in years', 'age')
        sex = display_input('Sex (1=Male, 0=Female)', 'Gender input', 'sex')
        cp = display_input('Chest Pain Type (0-3)', 'Type of chest pain', 'cp')
        trestbps = display_input('Resting Blood Pressure', 'Blood pressure at rest', 'trestbps')
        chol = display_input('Serum Cholesterol', 'Cholesterol in mg/dl', 'chol')
        fbs = display_input('Fasting Blood Sugar (>120 mg/dl: 1, else 0)', 'Fasting blood sugar', 'fbs')
        restecg = display_input('Resting ECG Results (0-2)', 'ECG results', 'restecg')
        thalach = display_input('Max Heart Rate Achieved', 'Maximum heart rate', 'thalach')
        exang = display_input('Exercise-Induced Angina (1=Yes, 0=No)', 'Pain due to exercise', 'exang')
        oldpeak = display_input('ST Depression Induced by Exercise', 'ST segment depression', 'oldpeak')
        slope = display_input('Slope of ST Segment (0-2)', 'ST segment slope', 'slope')
        ca = display_input('Number of Major Vessels Colored by Fluoroscopy (0-3)', 'Number of major vessels', 'ca')
        thal = display_input('Thalassemia Type (0-2)', 'Thalassemia input', 'thal')

        if st.button('Check Heart Disease'):
            prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            result = 'The person has heart disease' if prediction[0] == 1 else 'The person does not have heart disease'
            st.success(result)

    # Parkinson's Prediction
    if selected == 'Parkinsons Prediction':
        display_title_with_info('Parkinson\'s Prediction', "A neurodegenerative disorder affecting movement and speech.", 'parkinsons_info')

        # Using specific parameter names for Parkinson's
        fo = display_input('MDVP:Fo(Hz)', 'Average vocal fundamental frequency', 'fo')
        fhi = display_input('MDVP:Fhi(Hz)', 'Maximum vocal fundamental frequency', 'fhi')
        flo = display_input('MDVP:Flo(Hz)', 'Minimum vocal fundamental frequency', 'flo')
        Jitter_percent = display_input('MDVP:Jitter(%)', 'Variation in fundamental frequency - percent', 'Jitter_percent')
        Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Variation in fundamental frequency - absolute', 'Jitter_Abs')
        RAP = display_input('MDVP:RAP', 'Relative amplitude perturbation', 'RAP')
        PPQ = display_input('MDVP:PPQ', 'Five-point period perturbation quotient', 'PPQ')
        DDP = display_input('Jitter:DDP', 'Average absolute difference of differences', 'DDP')
        Shimmer = display_input('MDVP:Shimmer', 'Amplitude variation', 'Shimmer')
        Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Amplitude variation in decibels', 'Shimmer_dB')
        APQ3 = display_input('Shimmer:APQ3', 'Three-point amplitude perturbation quotient', 'APQ3')
        APQ5 = display_input('Shimmer:APQ5', 'Five-point amplitude perturbation quotient', 'APQ5')
        APQ = display_input('MDVP:APQ', 'Amplitude perturbation quotient', 'APQ')
        DDA = display_input('Shimmer:DDA', 'Average absolute differences amplitude perturbation', 'DDA')
        NHR = display_input('NHR', 'Noise to harmonics ratio', 'NHR')
        HNR = display_input('HNR', 'Harmonics to noise ratio', 'HNR')
        RPDE = display_input('RPDE', 'Recurrence period density entropy', 'RPDE')
        DFA = display_input('DFA', 'Detrended fluctuation analysis', 'DFA')
        spread1 = display_input('Spread1', 'Nonlinear measure of fundamental frequency variation', 'spread1')
        spread2 = display_input('Spread2', 'Nonlinear measure of fundamental frequency variation', 'spread2')
        D2 = display_input('D2', 'Correlation dimension', 'D2')
        PPE = display_input('PPE', 'Pitch period entropy', 'PPE')

        if st.button("Check Parkinson's"):
            features = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            prediction = models['parkinsons'].predict([features])
            result = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(result)

    # Lung Cancer Prediction
    if selected == 'Lung Cancer Prediction':
        display_title_with_info('Lung Cancer Prediction', "Lung cancer is the leading cause of cancer deaths worldwide.", 'lung_info')

        # Using specific symptom names for Lung Cancer
        GENDER = display_input('Gender (1=Male, 0=Female)', 'Gender of the person', 'GENDER')
        AGE = display_input('Age', 'Age of the person', 'AGE')
        SMOKING = display_input('Smoking (1=Yes, 0=No)', 'Does the person smoke', 'SMOKING')
        YELLOW_FINGERS = display_input('Yellow Fingers (1=Yes, 0=No)', 'Presence of yellow fingers', 'YELLOW_FINGERS')
        ANXIETY = display_input('Anxiety (1=Yes, 0=No)', 'Does the person have anxiety', 'ANXIETY')
        PEER_PRESSURE = display_input('Peer Pressure (1=Yes, 0=No)', 'Is the person under peer pressure', 'PEER_PRESSURE')
        CHRONIC_DISEASE = display_input('Chronic Disease (1=Yes, 0=No)', 'Does the person have chronic disease', 'CHRONIC_DISEASE')
        FATIGUE = display_input('Fatigue (1=Yes, 0=No)', 'Does the person experience fatigue', 'FATIGUE')
        ALLERGY = display_input('Allergy (1=Yes, 0=No)', 'Does the person have allergies', 'ALLERGY')
        WHEEZING = display_input('Wheezing (1=Yes, 0=No)', 'Does the person experience wheezing', 'WHEEZING')
        ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1=Yes, 0=No)', 'Does the person consume alcohol', 'ALCOHOL_CONSUMING')
        COUGHING = display_input('Coughing (1=Yes, 0=No)', 'Does the person experience coughing', 'COUGHING')
        SHORTNESS_OF_BREATH = display_input('Shortness of Breath (1=Yes, 0=No)', 'Does the person experience shortness of breath', 'SHORTNESS_OF_BREATH')
        SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1=Yes, 0=No)', 'Does the person have difficulty swallowing', 'SWALLOWING_DIFFICULTY')
        CHEST_PAIN = display_input('Chest Pain (1=Yes, 0=No)', 'Does the person experience chest pain', 'CHEST_PAIN')

        if st.button('Check Lung Cancer'):
            symptoms = [GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]
            prediction = models['lung_cancer'].predict([symptoms])
            result = 'The person has lung cancer' if prediction[0] == 1 else 'The person does not have lung cancer'
            st.success(result)

    # Thyroid Prediction
    if selected == 'Hypo-Thyroid Prediction':
        display_title_with_info('Thyroid Prediction', "Thyroid disorders affect metabolism and energy levels.", 'thyroid_info')

        # Using specific parameter names for Thyroid
        age = display_input('Age', 'Age of the person', 'thyroid_age')
        sex = display_input('Sex (1=Male, 0=Female)', 'Gender of the person', 'thyroid_sex')
        on_thyroxine = display_input('On Thyroxine (1=Yes, 0=No)', 'Is the person on thyroxine medication', 'on_thyroxine')
        tsh = display_input('TSH Level', 'Thyroid Stimulating Hormone level', 'tsh')
        t3_measured = display_input('T3 Measured (1=Yes, 0=No)', 'Has T3 been measured', 't3_measured')
        t3 = display_input('T3 Level', 'Triiodothyronine level', 't3')
        tt4 = display_input('TT4 Level', 'Total Thyroxine level', 'tt4')

        if st.button('Check Thyroid'):
            thyroid_features = [age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]
            prediction = models['thyroid'].predict([thyroid_features])
            result = 'The person has hypothyroidism' if prediction[0] == 1 else 'The person does not have hypothyroidism'
            st.success(result)
