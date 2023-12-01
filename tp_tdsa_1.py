import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal

sample_rate, audio1 = scipy.io.wavfile.read(r"C:\Users\jibri\Downloads\1st_baptist_nashville_far_wide.wav")
sample_rate, impulse_response = scipy.io.wavfile.read(r"C:\Users\jibri\Downloads\1st-baptist-nashville\1st-baptist-nashville\examples\1st_baptist_nashville_balcony.wav")
impulse_response = impulse_response.astype(np.float64)
audio1 = audio1.astype(np.float64)
#Simulation de valeurs d'un bruit blanc :
print(audio1.shape)
bruit_blanc1 = np.random.normal(size=(audio1.shape[0]))
bruit_blanc2 = np.random.normal(size=(audio1.shape[0]))
simu = scipy.signal.correlate(audio1[:,0],bruit_blanc1)
simu = simu/len(simu)
simu_bruit_blanc = scipy.signal.correlate(bruit_blanc2,bruit_blanc1)
simu_bruit_blanc = simu_bruit_blanc
plt.plot(audio1[:,0], label = "Signal original")
plt.plot(simu, label = "Corrélation avec le bruit blanc")
plt.legend()
plt.show()

plt.plot(bruit_blanc1, label = "Signal original")
plt.plot(simu_bruit_blanc, label = "Corrélation avec le bruit blanc")
plt.legend()
plt.show()

z = scipy.convolve(impulse_response[:,0],audio1[:,0])
z = z
plt.plot(audio1[:,0], label = "Signal original")
plt.plot(impulse_response[:,0], label = "Réponse impulsionnelle")
plt.plot(z, label = "Convolution avec le bruit blanc")
plt.legend()
plt.show()
