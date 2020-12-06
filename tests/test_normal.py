import pytest
import numpy as np
from MLE import *

def normal_estimation(data_normal):
    data=data_normal
    our_estimation=gradient_descent(x,gradient_normal_loglike,tol=.0001,maxiter=10000,step_size=.0001)
    
    mean_test=mean_analytic_normal(data)
    std_test=std_analytic_normal(data)
    
    assert our_estimation[0]==mean_test
    assert our_estimation[2]==std_test
