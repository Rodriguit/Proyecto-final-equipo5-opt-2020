import pytest
import numpy as np
import numpy.linalg
from MLE import *

def test_normal_estimation(data_normal):
    data=data_normal
    x=np.array([1,1])
    our_estimation=gradient_descent(x,gradient_normal_loglike,data,tol=.0001,maxiter=10000,step_size=.0001)
    
    mean_test=mean_analytic_normal(data_normal)
    std_test=std_analytic_normal(data_normal)
   
    norm_relerr_mean = np.linalg.norm(our_estimation[0]-mean_test)/np.linalg.norm(mean_test)
    norm_relerr_sd = np.linalg.norm(our_estimation[1]-std_test)/np.linalg.norm(std_test)
    assert norm_relerr_mean<=.0001
    assert norm_relerr_sd<=.0001