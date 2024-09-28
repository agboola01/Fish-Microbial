import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler

# Load the trained model
@st.cache(allow_output_mutation=True)
def load_model():
    with open('microbial_modelreg.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Load the scaler (for feature scaling)
@st.cache(allow_output_mutation=True)
def load_scaler():
    with open('scalers.pkl', 'rb') as file:
        scaler = pickle.load(file)
    return scaler

# Load the model and scaler
model = load_model()
scaler = load_scaler()

# Streamlit app layout
st.title("Microbial Organisms Prediction App")

st.header("Input Predicting Variables")
# Collecting input values for all feature columns
fish_sample = st.text_input("Fish Sample", "")
colour = st.text_input("Colour", "")
odour = st.text_input("Odour", "")
texture = st.text_input("Texture", "")
flavour = st.text_input("Flavour", "")
appearance = st.text_input("Appearance", "")
insect_invasion = st.text_input("Insect Invasion", "")
overall_acceptability = st.text_input("Overall Acceptability", "")
market = st.text_input("Market", "")
state = st.text_input("State", "")
tba = st.text_input("TBA", "")
pbc = st.text_input("PBC", "")
tfc = st.text_input("TFC", "")
pigmentation = st.text_input("Pigmentation1", "")
elevation = st.text_input("Elevation1", "")
texture_1 = st.text_input("Texture1", "")
margin = st.text_input("Margin1", "")
shape = st.text_input("Shape1", "")
optical_density = st.text_input("Optical Density1", "")
pigmentation_1 = st.text_input("Pigmentation2", "")
elevation_1 = st.text_input("Elevation2", "")
texture_2 = st.text_input("Texture2", "")
margin_1 = st.text_input("Margin2", "")
shape_1 = st.text_input("Shape2", "")
optical_density_1 = st.text_input("Optical Density2", "")
pigmentation_2 = st.text_input("Pigmentation3", "")
elevation_2 = st.text_input("Elevation3", "")
texture_3 = st.text_input("Texture3", "")
margin_2 = st.text_input("Margin3", "")
shape_2 = st.text_input("Shape3", "")
optical_density_2 = st.text_input("Optical Density3", "")
ph = st.number_input("pH", min_value=0.0)
lipid_oxidation = st.number_input("Lipid Oxidation", min_value=0.0)
moisture_content = st.number_input("Moisture Content", min_value=0.0)
protein = st.number_input("Protein", min_value=0.0)
fat = st.number_input("Fat", min_value=0.0)
ash = st.number_input("Ash", min_value=0.0)
# Combine input data into a DataFrame
input_data = pd.DataFrame({
    'Fish sample': [fish_sample],
    'Colour': [colour],
    'Odour': [odour],
    'Texture': [texture],
    'Flavour': [flavour],
    'Appearance': [appearance],
    'Insect Invasion': [insect_invasion],
    'Overall Acceptability': [overall_acceptability],
    'Market': [market],
    'State': [state],
    'TBA': [tba],
    'PBC': [pbc],
    'TFC': [tfc],
    'Pigmentation': [pigmentation],
    'Elevation': [elevation],
    'Texture.1': [texture_1],
    'Margin': [margin],
    'Shape': [shape],
    'Optical Density': [optical_density],
    'Pigmentation.1': [pigmentation_1],
    'Elevation.1': [elevation_1],
    'Texture.2': [texture_2],
    'Margin.1': [margin_1],
    'Shape.1': [shape_1],
    'Optical Density.1': [optical_density_1],
    'Pigmentation.2': [pigmentation_2],
    'Elevation.2': [elevation_2],
    'Texture.3': [texture_3],
    'Margin.2': [margin_2],
    'Shape.2': [shape_2],
    'Optical Density.2': [optical_density_2],
    'pH': [ph],
    'Lipid oxidation': [lipid_oxidation],
    'Moisture Content': [moisture_content],
    'Protein': [protein],
    'Fat': [fat],
    'Ash': [ash]
})
if st.button("Predict"):
    try:
        # Preprocess the input data
        input_data_encoded = input_data.copy()
        # Encode categorical features if necessary
        # For example, if 'Fish sample' is a categorical feature:
        # input_data_encoded['Fish sample'] = label_encoder.transform(input_data_encoded['Fish sample'])

        # Scale numeric features
        numeric_columns = input_data_encoded.select_dtypes(include=np.number).columns
        input_data_encoded[numeric_columns] = scaler.transform(input_data_encoded[numeric_columns])

        # Make predictions with the preprocessed data
        prediction = model.predict(input_data_encoded)

        # Display the prediction
        st.subheader("Predicted Values:")
        st.write(prediction)

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

# Footer
st.write("This application uses a regression model to predict microbial organisms based on input features.")
