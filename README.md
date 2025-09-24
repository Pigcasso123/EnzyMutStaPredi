# EnzyMutStaPredi
A web-based tool for predicting the stability change (ΔΔG) of enzyme mutations using machine learning. This application leverages the AutoGluon framework to provide rapid stability predictions based on mutation type and cavity volume features.
# Requirement
1. Pandas
2. FoldX
3. PyMOL
4. AlphaFold
5. CASTp
# Usage
## Running the Web Application
1. Clone this repository
2. Run the model:
`python model.py`
3. Run the application:
`python gradio.py`
4. Open your web browser and navigate to the local URL displayed in the terminal (typically http://localhost:7860)
## Using the Predictor
1. Select Mutation Site: Choose from the dropdown menu of available mutation sites
2. Adjust Cavity Volume: Use the slider to set the cavity volume in cubic Ångströms (Å³) between 0.5 and 5.0
3. Get Prediction: Click submit to receive the predicted ΔΔG value
## Interpreting Results
1. Negative ΔΔG values (e.g., -1.2 kcal/mol): Indicate stabilizing mutations that may improve enzyme thermostability
2. Positive ΔΔG values (e.g., 0.7 kcal/mol): Indicate destabilizing mutations that may decrease enzyme stability
3. Magnitude matters: Larger absolute values indicate stronger effects on stability
## Code Structure
1. `gradio.py`: Main application file containing the Gradio interface and prediction logic
2. Training data includes mutation identifiers, cavity volumes, and corresponding ΔΔG values
3. The model is trained using AutoGluon's TabularPredictor for automated machine learning
