import matplotlib.pyplot as plt
import numpy as np
x=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
Maximum_temperature=[40,42,43,39,38,40,41]
Minimum_temperature=[38,37,40,37,36,37,39]
plt.bar(x,Maximum_temperature,color='#932F67',label='Max. Temp')
plt.bar(x,Minimum_temperature,color='#D92C54',label='Min. Temp')
plt.title('Cairo temperature in Week 29')
plt.xlabel('days of week')
plt.ylabel('temperature in degrees Celsius')
plt.ylim(28,45)
plt.xticks(rotation=90)
plt.legend()
plt.show()
