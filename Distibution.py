from scipy.stats import poisson


# Assume that number of calls that some call center receives
# during one minute is Poisson random variable with parameter λ=2.
# Use Python to find probability that number of calls is larger than 5.

prob = poisson.cdf(5, 2)
print(1-prob)


# This problem continues previous one. Assume now that one operator can
# handle one call in one minute. If call is not handled, it's missed.
# How many operators should I hire to be sure that probability to miss
# a call during one minute is not larger than 0.05? Of course I want to
# minimize number of operators hired.
prob = poisson.ppf(0.95, 2)
print(prob)
