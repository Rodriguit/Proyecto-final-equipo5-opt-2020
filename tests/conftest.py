
import pytest
import numpy as np



@pytest.fixture
def data_normal():
    np.random.seed(0)
    x=np.random.rand(0,1,10)
    return x

@pytest.fixture
def data_poisson():   
    np.random.seed(0)
    x=np.random.poisson(5,10)
    return x