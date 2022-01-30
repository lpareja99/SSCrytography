from lcg import prng

sample_size = 12000
bins = 30

# let us split the sampled random numbers into equal bins
sample = [prng()//(2**64//bins) for _ in range(sample_size)]

def get_frequencies():
    """return the list of frequencies for successive bins"""
    frequencies = dict()
    for bin_ in sample:
        frequencies[bin_] = frequencies.get(bin_, 0) + 1
    return list(frequencies.values())

print(*get_frequencies())