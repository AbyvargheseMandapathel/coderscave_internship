import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


dataset = 'Hackathon_Ideal_Data.csv'

df = pd.read_csv(dataset)
print(df.info())