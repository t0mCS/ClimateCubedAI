import tensorflow as Tf
import pandas as Pd
import keras as Kf

height = Pd.read_excel("GROW DATA.xlsx",sheet_name = "Height")
time_to_germinate = Pd.read_excel("GROW DATA.xlsx", sheet_name = "Time to Germinate")
time_of_first_leaf = Pd.read_excel("GROW DATA.xlsx", sheet_name = "Time of First Leaf")
data_pods = []
data_pods_averaged = []
for n in range(20):
    data_pods.append(Pd.read_excel("CLIMATE DATA.xlsx",sheet_name = str(n+1), usecols=[0,2,3,4], header=None))
    for i in data_pods[n].index:
        el = data_pods[n][2][i]
        if type(el) is str:
            data_pods[n][2][i] = float(el[:-2])
    data_pods_averaged.append(data_pods[n].rolling(12, center = True).mean().dropna()[0::11])

print(height)
print(data_pods[14])
print(data_pods_averaged[14])