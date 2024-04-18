import numpy as np
import sys


def print_hi(name):
    print(f'Hi, {name}')


def f(x):
    result = (-1 / 10) * x + (1 / 50) * x * x + 13
    return result


def first_forward_derivation_f(x, h):
    result = (f(x+h) - f(x))/h
    return result


if __name__ == '__main__':
    borders = np.array([-50., 50.])
    doLookForMinimum = True
    tolerance = 1000000*sys.float_info.epsilon
    while (True):
        c = (borders[0] + borders[1]) / 2
        f_c = first_forward_derivation_f(c,tolerance/50)
        if (doLookForMinimum):
            if (f_c < -tolerance):
                borders[0] = c
            else:
                if (f_c > tolerance):
                    borders[1] = c
                else:
                    if (f_c >= -tolerance and f_c <= tolerance):
                        break
        else:
            if (f_c > -tolerance):
                borders[0] = c
            else:
                if (f_c < tolerance):
                    borders[1] = c
                else:
                    if (f_c >= -tolerance and f_c <= tolerance):
                        break

    print("The extrem is at x = ", c)
    # 2.5 is right