import numpy as np


def normal_loglikelihood(params,data):
    mu = params[0]
    sigma = params[1]
    x = data
    n=len(data)
    
    loglikelihood=-(n/2)*np.log(2*np.pi)-(n/2)*np.log(sigma**2)-(1/(2*sigma**2))*np.sum((x-mu)**2)
    
    return -1*loglikelihood

def gradient_normal_loglike(params,data):
    mu = params[0]
    sigma = params[1]
    x=data
    n=len(data)
    dmu= (1/(sigma**2))*np.sum(x-mu)
    dsigma=-(n/2)*((2*sigma)/sigma**2)+(1/sigma**3)*np.sum((x-mu)**2)
    return -1*np.array([dmu,dsigma])


def gradient_descent(x,gradient,data,tol=.0001,maxiter=10000,step_size=.0001):
    x_old=x+10
    i=0
    points=list()
    while ((np.linalg.norm(x-x_old)>=tol)):
        if i==1000:
            break
        points.append(x)
        x_old=x
        x=x-step_size*gradient(x,data)
        i+=1
    return x


mean_analytic_normal=lambda x: sum(x)/len(x)

def std_analytic_normal(data, ddof=0):
     n = len(data)
     mean = sum(data) / n
     return np.sqrt(sum((x - mean) ** 2 for x in data) / (n - ddof))
    
    