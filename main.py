import numpy as np
import sys
import matplotlib.pyplot as plt


def print_hi(name):
    print(f'Hi, {name}')

def f(x,y): # ODE
    return (1 + np.cos(x)) * y



if __name__ == '__main__':
    uRK = 1  # Runge-Kutta
    T = 50 # final time
    tA = np.linspace(0, T, num=500) # time steps for plotting
    # step size
    h = 0.1
    #exact solution
    exact = np.exp(tA + np.sin(tA))

    fig, ax = plt.subplots(figsize=(15, 4.5))
    ax.plot(tA, exact, linewidth=2)  # print

    t = 0
    while t < T:
        # Runge-Kutta 3. rad
        ax.plot(t, uRK, marker=".", color='r')
        ABS =  abs(uRK -  np.exp(t + np.sin(t)))
        ax.plot(t, ABS, marker=".", color='g')

        # computing uRK
        k1 = h*f(t, uRK)
        k2 = (h/2)*f(t + h, uRK + k1)
        k3 =  (h/2)*f(t, uRK)
        uRK = uRK + k1 + k2 - k3




        t = t + h

    ax.set_ylabel(r'$\dfrac{\mathrm{d}N}{\mathrm{d}t}$')
    ax.set_xlabel(r'$t$')


    fig.show()


