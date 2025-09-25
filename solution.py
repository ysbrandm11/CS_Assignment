import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('istherecorrelation.csv', sep=';')


x = df["WO [x1000]"]
y = df["NL Beer consumption [x1000 hectoliter]"]
plt.figure(figsize=(10, 10))
plt.plot(x,y)
plt.xlabel("WO [x1000]")
plt.ylabel("NL Beer consumption [x1000 hectoliter]")
plt.title("WO vs NL Beer consumption")
plt.xticks(rotation=45)
plt.show()