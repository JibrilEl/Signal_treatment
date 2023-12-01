import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
size_sources =(2,1000)
sources = np.random.uniform(low=-1,high=1,size=size_sources)
A = np.array([[1,1],[0,1]])

donnees = A@sources
covar = np.cov(donnees)

vals, vecs = np.linalg.eig(covar)

inv_sqrt_vals = np.diag(1 / np.sqrt(vals))

covar_sources_inv_sqrt = vecs @ inv_sqrt_vals @ np.transpose(vecs)

Z = covar_sources_inv_sqrt@donnees

theta_values = np.linspace(0,2*np.pi,num=200)
kurtosis_list = []
for theta in theta_values :
    X_estim = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])@Z
    kurtosis = np.mean(X_estim**4)-3
    kurtosis_list.append(kurtosis)
plt.plot(theta_values,kurtosis_list)
plt.show()
theta = 0.45
X_estim = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])@Z
sns.scatterplot(x=X_estim[0],y=X_estim[1])
plt.show()