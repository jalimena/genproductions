import sys

def float_compare(x, y):
    '''Helper function to check that two numbers are equal within float precision.'''
    if(y == 0):
        return x == 0
    if(abs((x - y) / y) < 1e-8):
        return True
    return False


def tuple_compare(x, y):
    '''Helper function to check that two tuples are equal within float precision.'''
    return (float_compare(x[0], y[0]) and float_compare(x[1], y[1]))


def do_test(functions):
    for f in functions:
        passed = f()
        if(passed):
            print "test_variable: Test PASSED for function '{0}'.".format(f.func_name)
        else:
            print "test_variable: Test FAILED for function '{0}'.".format(f.func_name)
            sys.exit(1)
    print "test_variable: All tests PASSED."
    sys.exit(0)
