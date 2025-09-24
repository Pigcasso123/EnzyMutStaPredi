import pandas as pd
from autogluon.tabular import TabularPredictor
data = {
    'mutation': ['A88C', 'N92C', 'N92D','N92E','A139F','A139L'], 
    'cavity_volume': [0.917, 3.356, 3.16,3.128,3.071,3.071],
    'ddG': [0.8414, -0.6225, 0.474,0.3548,-0.8529,-1.3258]  # FoldX计算的ΔΔG
}
df = pd.DataFrame(data)
predictor = TabularPredictor(label='ddG').fit(
    train_data=df,
    time_limit=120)