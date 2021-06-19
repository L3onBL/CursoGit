import pandas as pd
import numpy as np


data = [1, 2, 3, 4, 5]
df = []
for i in data:
    print (i/2)
    df.append(i/4)

print(f"El df i/4 {df}")
print(f"El df i/2 {df}")

df2 = []

for i in data:
    df2.append(np.sinc(i))

print(f"El df2 i/2 {df2}")