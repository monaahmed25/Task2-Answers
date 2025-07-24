

import matplotlib.pyplot as plt
import numpy as np
x=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
y=[40,42,43,39,38,40,41]
plt.plot(x,y,color='g',marker='x')
plt.title('Cairo temperature in Week 29')
plt.xlabel('days of week')
plt.ylabel('temperature in degrees Celsius')
plt.xticks(rotation=45)
plt.show()
