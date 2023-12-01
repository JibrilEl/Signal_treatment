import numpy as np
import matplotlib.pyplot as plt
n_micro=10
n_point_test = 300
alpha = 0.1
sigma = 1
freq_spatiale= 1/0.08
c= 300
f=1000
d=2
k = 2*np.pi*f/c
source_position = 20
Y_mat =np.tile(np.linspace(0,1/freq_spatiale*n_micro,n_micro),(n_point_test,1))
X_mat = np.tile(np.linspace(0,0.01*n_point_test,n_point_test),(n_micro,1))


delta1 = X_mat - np.transpose(Y_mat)
D = np.sqrt(delta1**2+d**2)
def g1(i,D):
    res = np.exp(-1j*k*D[i,j]/D[i,j])
    return(abs(res))
m = np.random.normal(size=(n_micro),loc=alpha*g1(source_position,D),scale=sigma)
m_2 = np.random.normal(size=(n_micro),loc=alpha*g1(source_position,D),scale=sigma)
def b(m,j,D):
    def g2(i,j,D):
        res = np.array(np.exp(-1j*k*D[i,j])/D[i,j])
        return(res)
    g_value =g2(j,D)
    scal_prod = np.dot(m,np.conjugate(g_value))
    return(scal_prod/np.linalg.norm(g_value,ord=2))

space_array = [i for i in range(n_point_test)]
b_values = [b(m,j,D) for j in range(n_point_test)]
plt.plot(space_array,b_values,label = "b(x)")
plt.legend(loc="upper left")
plt.show()