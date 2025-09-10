import pandas as pd
import ast

# Parse predictions.log
data = []
try:
    with open('predictions.log', 'r') as f:
        for line in f:
            if 'Input:' in line:
                input_str = line.split('Input: ')[1].split(', Prediction:')[0]
                input_dict = ast.literal_eval(input_str)
                row = {k: v[0] for k, v in input_dict.items()}
                data.append(row)
    pd.DataFrame(data).to_csv('current_inputs.csv', index=False)
    print("Generated current_inputs.csv")
except FileNotFoundError:
    print("predictions.log not found")