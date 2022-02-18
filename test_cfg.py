import numpy as np
from cylp.cy import CyClpSimplex, CyCbcModel
from cylp.py.modeling.CyLPModel import CyLPArray, CyLPModel


def cylp_modelling():
    '''
    Function to return OR solution using CyLP.
    Returns: Solution to OR problem defined below.
    Derived from: https://github.com/coin-or/CyLP
    '''

    s = CyClpSimplex()

    # Add variables
    x = s.addVariable('x', 3)
    y = s.addVariable('y', 2)

    # Create coefficients and bounds
    A = np.matrix([[1., 2., 0],[1., 0, 1.]])
    B = np.matrix([[1., 0, 0], [0, 0, 1.]])
    D = np.matrix([[1., 2.],[0, 1]])
    a = CyLPArray([5, 2.5])
    b = CyLPArray([4.2, 3])
    x_u= CyLPArray([2., 3.5])

    # Add constraints
    s += A * x <= a
    s += 2 <= B * x + D * y <= b
    s += y >= 0
    s += 1.1 <= x[1:3] <= x_u

    # Set the objective function
    c = CyLPArray([1., -2., 3.])
    s.objective = c * x + 2 * y.sum()

    # Solve using primal Simplex
    s.primal()
    return s.primalVariableSolution['x']

def test_cylp():
    '''
    Function to test that CyLP is correctly installed.
    '''
    solution = np.array(cylp_modelling(), dtype=np.float32)
    expected_solution = np.array([0.2, 2, 1.1], dtype=np.float32)
    assert np.array_equal(solution, expected_solution) == True, (
        f"Solution {solution} (shape {solution.shape}) "
        f"!= {expected_solution} "
        f"(shape {expected_solution.shape})"
    )

def cbc_modelling():
    '''
    Function to return OR solution using the Cbc solver in CyLP.
    Returns: Solution to OR problem defined below.
    Derived from: http://coin-or.github.io/CyLP/modules/CyCbcModel.html
    '''
    model = CyLPModel()

    x = model.addVariable('x', 3, isInt=True)
    y = model.addVariable('y', 2)

    A = np.matrix([[1., 2., 0],[1., 0, 1.]])
    B = np.matrix([[1., 0, 0], [0, 0, 1.]])
    D = np.matrix([[1., 2.],[0, 1]])
    a = CyLPArray([5, 2.5])
    b = CyLPArray([4.2, 3])
    x_u= CyLPArray([2., 3.5])

    model += A*x <= a
    model += 2 <= B * x + D * y <= b
    model += y >= 0
    model += 1.1 <= x[1:3] <= x_u

    c = CyLPArray([1., -2., 3.])
    model.objective = c * x + 2 * y.sum()

    s = CyClpSimplex(model)

    cbcModel = s.getCbcModel()
    cbcModel.solve()
    return cbcModel.primalVariableSolution['x']

def test_cbc():
    '''
    Function to test that CyLP and cbc are correctly installed.
    '''
    solution = cbc_modelling()
    assert (abs(solution - np.array([0, 2, 2])) <= 10**-6).all()
