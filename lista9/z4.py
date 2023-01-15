import matplotlib.pyplot as plt
import numpy as np
jezyki=["Python","Java","C++","C#","JavaScript","PHP","C","R","Swift","Go"]
popularnosc=[56,45,40,40,38,36,34,31,30,29]
plt.bar(jezyki,popularnosc)
plt.xlabel("Jezyki")
plt.ylabel("Popularnosc")
plt.title("Popularnosc jezykow programowania")
plt.show()