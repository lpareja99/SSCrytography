from lcg2 import prng
from lcg2 import prng_random
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import chi2



sample_size = 12000
bins = 30

# let us split the sampled random numbers into equal bins using prng()
sample_1 = [prng()//(2**64//bins) for _ in range(sample_size)]

# let us split the sampled random numbers into equal bins using the prng_random()
sample_2 = [prng_random()//(2**64//bins) for _ in range(sample_size)]

def get_frequencies(sample):
    """return the list of frequencies for successive bins"""
    frequencies = dict()
    for bin_ in sample:
        frequencies[bin_] = frequencies.get(bin_, 0) + 1
    return list(frequencies.values())

# Frequencies for our lcg
print(*get_frequencies(sample_1))

# Frequencies for the random number generator

print(*get_frequencies(sample_2))

# Now let's compare the chi squared test

def chi_squared_test():
    """Return a chi_square test."""

    #take a binned sample
    sample = [prng()//(2**64//bins) for _ in range(sample_size)]

    # get just the frequences of the occurrences for each bin
    frequencies = dict()
    for bin_ in sample:
        frequencies[bin_] = frequencies.get(bin_, 0) + 1
    frequencies = frequencies.values()

    expected_frequency = sample_size/bins

    return sum(map(lambda x: (x-expected_frequency)**2, frequencies))/expected_frequency

results = [chi_squared_test() for _ in range(5000)] # the results of 5000 chi_squared tests

def chi_squared_test_2():
    """Return a chi_square test."""

    #take a binned sample
    sample = [prng_random()//(2**64//bins) for _ in range(sample_size)]

    # get just the frequences of the occurrences for each bin
    frequencies = dict()
    for bin_ in sample:
        frequencies[bin_] = frequencies.get(bin_, 0) + 1
    frequencies = frequencies.values()

    expected_frequency = sample_size/bins

    return sum(map(lambda x: (x-expected_frequency)**2, frequencies))/expected_frequency
results_2 = [chi_squared_test() for _ in range(5000)] # the results of 5000 chi_squared tests

# plot a histogram of the results of the 5000 tests
plt.hist(results, bins = 50, density = True)
x = np.arange(0, 60, 0.001)
plt.plot(x, stats.chi2.pdf(x, df=bins-1), label="prng")
plt.legend()
plt.show()


# plot a histogram of the results of the 5000 tests
plt.hist(results_2, bins = 50, density = True)
x = np.arange(0, 60, 0.001)
plt.plot(x, stats.chi2.pdf(x, df=bins-1), label="prng_random")
plt.legend()
plt.show()

# By comparing both results we can see that our lcg does a pretty good job compared to python's random number generator.
