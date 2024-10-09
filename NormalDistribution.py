# Normal Distribution
import math
import numpy as np
import matplotlib.pyplot as plt

""""

    The constant probability distribution having Probability Density Function(PDF)  
    f(x) = (1/ σ √2. pi) * e^ (-(x - μ)^2 / 2. σ^2)
    where x in (-ↀ , ↀ), μ in (-ↀ , ↀ), σ>0  is known as Normal Distribution function.
    
"""


# Function to calculate normal distribution probability
def calc(mean, sigma, x):
    # Normal distribution formula: (1 / (sigma * sqrt(2 * pi))) * exp(-0.5 * ((x - mu) / sigma) ** 2)
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = math.exp(-0.5 * ((x - mean) / sigma) ** 2)
    return coefficient * exponent


try:
    # Getting input for Mean and Standard Variance
    mean = float(input("Enter the mean (μ): "))
    sigma = float(input("Enter sigma value:"))

    # Getting input for lower and upper limit values
    lower = float(input("Enter the lower limit for x: "))  # lower limit
    higher = float(input("Enter the higher limit for x (0 if infinity): "))  # upper limit

    if sigma <= 0:
        print("σ must be positive.")
    else:
        # Using appropriate formula for the given values.
        if higher == 0 and lower != 0:
            probability = 1 - calc(mean, sigma, lower)
            higher = "ↀ"
        elif higher != 0 and lower == 0:
            probability = calc(mean, sigma, higher)
        elif higher != 0 and lower != 0:
            probability = calc(mean, sigma, higher) - calc(mean, sigma, lower)
        else:
            raise ValueError

        # Calculate the probability at the input x value
        if higher == "ↀ":
            print(f"The probability for x > {lower} is: {probability*100:.4f}%")
            higher = mean + 4 * sigma
        else:
            print(f"The probability for {lower} < x < {higher} is: {probability*100:.4f}%")
        # print(f"The probability density for x belongs to ({lower} , {higher}) is: {probability:.4f}")

        # Generating  x and y values for the graph
        x_values = np.linspace(lower-25, higher+25, 500)  # Plot within 4 standard deviations
        y_values = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_values - mean) / sigma) ** 2)

        # Plotting the normal distribution graph
        plt.figure(figsize=(4, 3))
        plt.plot(x_values, y_values, label=f'Normal Distribution (μ = {mean}, σ = {sigma})')
        plt.axvline(mean, color='red', linestyle='--', label=f'Mean (μ) = {mean}')
        plt.axvline(lower, color='green', linestyle='--', label=f'Lower Limit = {lower}')
        if higher != mean + 4 * sigma:
            plt.axvline(higher, color='green', linestyle='--', label=f'Upper Limit = {higher}')

        # Generate x-values for the shaded area between lower and upper limits
        x_fill = np.linspace(lower, higher, 500)
        y_fill = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_fill - mean) / sigma) ** 2)

        # Fill the area under the curve between the limits
        plt.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5, label=f'Area between {lower} and {higher}')

        plt.title('Normal Distribution Function')
        plt.xlabel('x')
        plt.ylabel('Probability Density')
        # plt.legend()
        plt.grid(True)
        plt.show()

except ValueError as e:
    print(f'Error: {e}')







"""
Scenario: A company records the time employees take to complete a task. The times follow 
a normal distribution with a mean of 30 minutes and a standard deviation of 5 minutes.

Question: What is the probability that a randomly selected employee completes the task between 
25 minutes and 35 minutes?

Given:
    Mean (μ): 30
    Standard Deviation (σ): 5
    Lower Limit (x): 25
    Upper Limit (x): 35




Scenario: A university has recorded the heights of male students, which are normally 
distributed with a mean height of 70 inches and a standard deviation of 3 inches.

Question: What is the probability that a randomly selected student is between 
67 inches and 73 inches tall?

Given:
    Mean (μ): 70
    Standard Deviation (σ): 3
    Lower Limit (x): 67
    Upper Limit (x): 73
"""