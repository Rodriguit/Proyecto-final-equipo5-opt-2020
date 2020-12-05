import numpy as np
from scipy.optimize import minimize,fsolve
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors



def normal_loglikelihood(params,**kwargs):
    mu = params[0]
    sigma = params[1]
    x = data
    n=len(data)
    
    loglikelihood=-(n/2)*np.log(2*np.pi)-(n/2)*np.log(sigma**2)-(1/(2*sigma**2))*np.sum((x-mu)**2)
    
    return -1*loglikelihood



def gradient_normal_loglike(params,**kwargs):
    mu = params[0]
    sigma = params[1]
    x=data
    n=len(data)
    dmu= (1/(sigma**2))*np.sum(x-mu)
    dsigma=-(n/2)*((2*sigma)/sigma**2)+(1/sigma**3)*np.sum((x-mu)**2)
    return np.array([dmu,dsigma])