import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
##%matplotlib inline     
sns.set(color_codes=True)

print("Debug")

df = pd.read_csv("data.csv")
# To display the top 5 rows 
df.head(5)     

print(df.head(5))
print(df.tail(5))          
