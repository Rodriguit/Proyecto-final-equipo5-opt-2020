import numpy as np
import cvxpy as cp 
import pickle 
from sklearn import datasets



# pickle_in = open("matriz_imagenes","rb")
# X= pickle.load(pickle_in)


iris = datasets.load_iris()
X = iris.data



### Primer intento
### Usando CVXPY

### http://alexhwilliams.info/itsneuronalblog/2016/03/27/pca/
n,p=X.shape
r=4

C = cp.Variable((p,r))
I=np.identity(r)

fo = cp.norm(X-X@C@C.T,"fro")
 
constraint=[C.T@C==I]
obj=cp.Minimize(fo)

prob = cp.Problem(obj,constraint)
prob.solve(dcp=False,solver='ECOS')

### No funciona

### Intento 2 Regularizacion cuadratica

## https://arxiv.org/pdf/1410.0342.pdf



iris = datasets.load_iris()
A = iris.data
m,n=A.shape
k=4



X = cp.Variable((m,k))
Y = cp.Variable((k,n))

lambda1=2
lambda2=2


fo = cp.norm(A-X@Y,"fro")+lambda1*p.norm(X,"fro")+lambda1*p.norm(Y,"fro")
 

obj=cp.Minimize(fo)

prob = cp.Problem(obj,constraint)
prob.solve(dcp=False,)






