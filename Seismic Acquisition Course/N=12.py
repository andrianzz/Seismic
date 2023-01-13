import numpy as np
import matplotlib.pyplot as plt

d = 20
k = np.arange(0,0.05001,0.0001)
N = 11
db = []
for i in range (len(k)):
    if i==0 :
        db.append(0)
    else :
        db.append(20*np.log(abs(np.sin(np.pi*d*k[i]*N)/(N*np.sin(np.pi*d*k[i])))))

plt.plot(k,db)
plt.title("Response Curve Geophone, N =11")
plt.xlabel("Wave Number k")
plt.ylabel("dB (Amplitude Response)")
plt.ylim((-100,0))
plt.show()