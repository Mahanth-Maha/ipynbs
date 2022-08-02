from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianNetwork
import pandas as pd

d2 = [['age', 'Gender', 'Family', 'diet', 'Lifestyle', 'cholestrol', 'heartdisease'],
      [0, 0, 1, 1, 3, 0, 1],
      [0, 1, 1, 1, 3, 0, 1],
      [1, 0, 0, 0, 2, 1, 1],
      [4, 0, 1, 1, 3, 2, 0],
      [3, 1, 1, 0, 0, 2, 0],
      [2, 0, 1, 1, 1, 0, 1],
      [4, 0, 1, 0, 2, 0, 1],
      [0, 0, 1, 1, 3, 0, 1],
      [3, 1, 1, 0, 0, 2, 0],
      [1, 1, 0, 0, 0, 2, 1],
      [4, 1, 0, 1, 2, 0, 1],
      [4, 0, 1, 1, 3, 2, 0],
      [2, 1, 0, 0, 0, 0, 0],
      [2, 0, 1, 1, 1, 0, 1],
      [3, 1, 1, 0, 0, 1, 0],
      [0, 0, 1, 0, 0, 2, 1],
      [1, 1, 0, 1, 2, 1, 1],
      [3, 1, 1, 1, 0, 1, 0],
      [4, 0, 1, 1, 3, 2, 0]]

pd.DataFrame(d2[1:], columns=d2[0])

heart_disease = pd.DataFrame(d2[1:], columns=d2[0])

model = BayesianNetwork([
    ('age', 'Lifestyle'),
    ('Gender', 'Lifestyle'),
    ('Family', 'heartdisease'),
    ('diet', 'cholestrol'),
    ('Lifestyle', 'diet'),
    ('cholestrol', 'heartdisease'),
    ('Lifestyle', 'cholestrol')
])

model.fit(heart_disease, estimator=MaximumLikelihoodEstimator)

HeartDisease_infer = VariableElimination(model)

k = HeartDisease_infer.query(variables=['heartdisease'], evidence={
                             'age': 3, 'Gender': 0, 'Family': 1, 'diet': 1, 'Lifestyle': 3, 'cholestrol': 2})

print(k)
