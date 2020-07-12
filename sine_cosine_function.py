#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,'--')
plt.plot(x,z)
plt.xlabel('x values from 0 to 4pi') 
plt.ylabel('sin(x) and cos(x)') 
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()


# In[ ]:




