## Electricity Load Simulation using pyomo

import pandas as pd
import numpy as np

df = pd.read_excel('data.xlsx')


#converting instate production into MW
In_state = 50.7*1000
#Total consumption in a state
Total_consumption = 109.44*1000
National_grid_sum = (df['Outside State (MW)'].sum())/4
#Total_consumption = In_state + National_grid_sum
Typical_curve_area = (df['Typical Day (MW)'].sum())/4

df['Adjusted_curve'] =  (Total_consumption/Typical_curve_area)*df['Typical Day (MW)']


national_grid = dict(df['Outside State (MW)'])
adjusted_curve = dict(df['Adjusted_curve'])

N = list(range(96))
