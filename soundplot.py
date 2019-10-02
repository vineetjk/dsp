import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io.wavfile import read

(fs,x)= read('doorbell_x.wav')
print(x)
print(x.size)
print(x.size/fs)

print(x.size/float(fs))

t = np.arange(x.size)/float(fs)

plt.plot(t,x)
plt.show()

