import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('data.csv')


# To count pokeamon on Basis of Group(as Type1) :-
group_byType1 = df.groupby('Type1')

type1_counts = group_byType1["Type1"].count() # (or)  print(df["Type1"].value_counts())

type1_counts = type1_counts.sort_values()   #for sorting df maded by groupby()

print( type1_counts , type1_counts.index , type1_counts.values  )   #=> ( type1 + counts , type1  , counts )



# Plot the horizontal-bar chart  Type1 v/s Count of pokemon :-
groups = np.array( type1_counts.index )
counts = np.array( type1_counts.values )


plt.barh( groups ,counts , color="yellow" , edgecolor="black")


plt.title("No of Pokemon by Primary Type")


plt.ylabel("Types")
plt.xlabel("Count")

plt.grid(axis="both" , color="grey" , alpha=0.2)


plt.tight_layout()  # some spacing btw names

plt.show()
