import numpy as np
import matplotlib.pyplot as plt

k = np.arange(0,0.05001,0.0001)
d = 20
N = np.array([2,3,4,5,6,7,8,9,10,11,12])
db = [0 for i in range(len(k))]
def amplitude_respons(x) :
    for i in range(len(k)):
        if i == 0:
            db[i] = 0
        else:
            db[i] = 20 * np.log(abs(np.sin(np.pi * d*k[i] * x) / (x * np.sin(np.pi * d*k[i]))))
    return db

for i in range (len(N)):
    plt.plot(k,amplitude_respons(N[i]),label='N = '+str(N[i]))

plt.ylim(-100,0)
plt.xlabel("wave number k")
plt.ylabel("dB (Amplitude Response)")
plt.title("Respone Curve Geophone, N = 2 to 12")
plt.legend()
plt.show()

