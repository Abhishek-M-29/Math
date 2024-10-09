# Exponential Distribution
import math                         # mathematical operations
import matplotlib.pyplot as plt     # graphs
import numpy as np                  # array processing for matplotlib

'''
    The continuous probability distribution having the PDF(Probability Density Function)
    f(x) = { ɑ.e^-ɑn -> x>0 
            o -> otherwise , ɑ>0
    is known as the Exponential Distribution

    Mean(μ) = 1/ɑ || Variance(σ^2) = 1/ɑ^2 || Standard Deviation(σ) = 1/ɑ
'''


def calc(val, x):
    # Exponential distribution formula: f(x) = ɑ * exp(-ɑx)
    return val * math.exp(-val * x)


try:
    # The given value will be either Mean or the Rate parameter.
    c = int(input("Enter 1 for ALPHA(rate) & 2 for MEAN -> "))
    if c == 1:
        alpha = float(input("Enter the rate parameter/ alpha (ɑ): "))
        mean = 1/alpha
    elif c == 2:
        mean = float(input("Enter the Mean: "))
        alpha = 1/mean
    else:
        raise ValueError

    # Getting input for lower and upper limit values
    lower = float(input("Enter the lower limit for x: "))  # lower limit
    higher = float(input("Enter the higher limit for x (0 if infinity): "))  # upper limit

    # Authenticating if the given values are not absurd
    if alpha <= 0 or lower < 0 or 0 < higher < lower:
        print("ɑ must be positive, lower limit must be non-negative and \
        higher limit must be greater than lower limit.")
    else:
        # Using appropriate formula for the given values.
        if higher == 0 and lower != 0:      # (lower, infinity)
            probability = 1 - calc(alpha, lower)
            higher = "ↀ"
        elif higher != 0 and lower == 0:    # (0, higher)
            probability = calc(alpha, higher)
        elif higher != 0 and lower != 0:    # (lower, higher)
            probability = calc(alpha, higher) - calc(alpha, lower)
        else:
            raise ValueError

        # Displaying the value.
        if higher == "ↀ":
            print(f"The value for exponential distribution function when x > {lower} is: {probability:.4f}")
        else:
            print(f"The value for exponential distribution function when {lower} < x < {higher} is: {probability:.4f}")

        # print(f"The probability density for x belongs to ({lower}, {higher}) is: {probability:.4f}")

        if higher == "ↀ":
            higher = lower + (mean - lower) + 50
        # Generate x and y values for plotting the graph
        x_values = np.linspace(0, higher + 5, 500)
        y_values = alpha * np.exp(-alpha * x_values)

        # Plotting the exponential distribution graph
        plt.figure(figsize=(4, 3))
        plt.plot(x_values, y_values, label=f'Exponential Distribution (λ = {alpha})')
        plt.axvline(mean, color='r', linestyle='--', label=f'x = {mean}')
        plt.fill_between(x_values, y_values, where=(x_values >= lower) & (x_values <= float(higher)
                                                                          if higher != "ↀ" else higher),
                         color='skyblue', alpha=0.4)
        plt.axvline(lower, color='green', linestyle='--', label=f'Lower Limit = {lower}')
        if higher != lower + (mean - lower) + 50:
            plt.axvline(higher, color='green', linestyle='--', label=f'Upper Limit = {higher}')

        plt.title('Exponential Distribution Function')
        plt.xlabel('x')
        plt.ylabel('Probability Density')
        plt.legend(['Exponential Distribution', f'Mean (μ = {mean})', f'α = {alpha}'])
        # plt.legend()
        plt.grid(True)
        plt.show()


except ValueError as e:
    if e == "":
        print("Enter Valid Inputs!")
    else:
        print(f'Error: {e}')












"""
1.    Buses arrive at a particular stop at an average rate of 4 buses per hour. Assume the waiting time 
    for a bus follows an exponential distribution.
    What is the probability that the next bus will arrive in less than 10 minutes? 
    
    Given:  α (rate): 4
            Lower Limit: 0 (start waiting)
            Upper Limit: 1/6 = 0.1667 (10 minutes = 1/6 of an hour)
    P(0<x<10) = ?
"""

"""
    In a certain region, earthquakes occur at an average rate of once every 50 years. The time between 
    consecutive earthquakes follows an exponential distribution.
    Problem Statement: What is the probability that the next earthquake will occur in the next 30 years? 
    
    Given:  μ (mean): 50
            Lower Limit: 0 (now)
            Upper Limit: 30 (next 30 years)
    P(0<x<30) = ?
"""