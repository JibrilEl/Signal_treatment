import numpy as np
import scipy
import matplotlib.pyplot as plt
h = np.array([])
h= np.array([80 - i for i in range(50)])
signal_duration = h.shape[0]
time_step =0.5
h_log = 20*np.log10(abs(h))
time_array = np.linspace(0,signal_duration*time_step,signal_duration)

plt.plot(time_array,h_log, label = "Logarithme de la réponse impulsionelle")
plt.legend()
plt.show()

#Calcul automatique de tr60
threshold_start=0.008
threshold_end = 30
start_index=0
end_index=0
tr =0
for i in range(signal_duration-1):
    if h_log[i]-h_log[i+1] > threshold_start:
        start_index=i
        print("Start :",start_index)
        break

for i in range(signal_duration-1):
    if h_log[i] < threshold_end:
        end_index=i
        print("End :",end_index)
        break
tr = (end_index-start_index)*time_step
print("Temps de réponse : ",tr)
#Calcul de la clarté
end_time = 50*(10**-3)

bas_niveau = np.mean(h[:int((end_time/time_step)*signal_duration)]**2)
haut_niveau = np.mean(h[int((end_time/time_step)*signal_duration):]**2)

clarte = 10*np.log(bas_niveau/haut_niveau)
print("Clarté : ",clarte)
