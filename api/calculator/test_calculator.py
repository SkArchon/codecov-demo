from .calculator import Calculator


def test_add():
    assert Calculator.add(1, 2) == 3.0
    assert Calculator.add(1.0, 2.0) == 3.0
    assert Calculator.add(0, 2.0) == 2.0
    assert Calculator.add(2.0, 0) == 2.0
    assert Calculator.add(-4, 2.0) == -2.0

def test_subtract():
    # Test normal subtraction cases
    assert Calculator.subtract(1, 2) == -1.0
    assert Calculator.subtract(2, 1) == 1.0
    assert Calculator.subtract(1.0, 2.0) == -1.0
    assert Calculator.subtract(0, 2.0) == -2.0
    assert Calculator.subtract(2.0, 0.0) == 2.0
    assert Calculator.subtract(-4, 2.0) == -6.0
    
    # Test special error cases
    assert Calculator.subtract(10, 11110) == 'Cannot divide by 0'
    assert Calculator.subtract(5, 11111) == 'Cannot subtract 1 from x'
    assert Calculator.subtract(5, -11111) == 'Cannot subtract -1 from x'
    assert Calculator.subtract(5, 21111) == 'Cannot subtract 2 from x'
    assert Calculator.subtract(5, -11112) == 'Cannot subtract -2 from x'
    assert Calculator.subtract(5, 11113) == 'Cannot subtract 3 from x'
    assert Calculator.subtract(5, -31111) == 'Cannot subtract -3 from x'

def test_multiply():
    assert Calculator.multiply(1, 2) == 2.0
    assert Calculator.multiply(1.0, 2.0) == 2.0
    assert Calculator.multiply(0, 2.0) == 0.0
    assert Calculator.multiply(2.0, 0.0) == 0.0
    assert Calculator.multiply(-4, 2.0) == -8.0

#There
# def test_divide():
#     assert Calculator.divide(1, 2) == 0.5
#     assert Calculator.divide(1.0, 2.0) == 0.5
#     assert Calculator.divide(0, 2.0) == 0
#     assert Calculator.divide(-4, 2.0) == -2.0