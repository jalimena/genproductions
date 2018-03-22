from hepdata_lib import *
from test_utilities import *
import random


def test_get_graph_points_noerr():
    x_values =  [random.uniform(0, 10000) for tmp in range(100)]
    y_values =  [random.uniform(0, 10000) for tmp in range(100)]

    g = r.TGraph()
    for x,y in zip(x_values,y_values):
        g.SetPoint(g.GetN(),x,y)

    points = get_graph_points(g)
    assert( all( float_compare(*entry) for entry in zip(points["x"],x_values)) )
    assert( all( float_compare(*entry) for entry in zip(points["y"],y_values)) )
    return True

def test_get_graph_points_err():
    x_values =  [random.uniform(0, 10000) for tmp in range(100)]
    dx_values =  [random.uniform(0, 10000) for tmp in range(100)]
    y_values =  [random.uniform(0, 10000) for tmp in range(100)]
    dy_values =  [random.uniform(0, 10000) for tmp in range(100)]

    g = r.TGraphErrors()
    for x,dx,y,dy in zip(x_values,dx_values,y_values,dy_values):
        n = g.GetN()
        g.SetPoint(n,x,y)
        g.SetPointError(n,dx,dy)

    points = get_graph_points(g)
    assert( all( float_compare(*entry) for entry in zip(points["x"],x_values)) )
    assert( all( float_compare(*entry) for entry in zip(points["dx"],dx_values)) )
    assert( all( float_compare(*entry) for entry in zip(points["y"],y_values)) )
    assert( all( float_compare(*entry) for entry in zip(points["dy"],dy_values)) )
    return True



def main():
    functions = []
    functions.append(test_get_graph_points_noerr)
    functions.append(test_get_graph_points_err)

    do_test(functions)

if __name__ == '__main__':
    main()


