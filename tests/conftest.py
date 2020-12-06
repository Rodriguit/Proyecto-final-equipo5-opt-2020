import pytest
import numpy as np



@pytest.fixture
def data_normal():
    data=np.loadtxt('tests/wheat_yield.txt')

    return data

@pytest.fixture
def data_poisson():   
    np.random.seed(0)
    x=np.random.poisson(5,10)
    return x