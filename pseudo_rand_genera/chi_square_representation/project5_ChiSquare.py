#The histogram and analysis above look pretty good but 
# the original sampling was always split into 30 bins. 
# Conduct the same sort of $\chi^2$ analysis but use different 
# (smallish) numbers of bins and varying (large) sample sizes.

# Lets first run our code with our parameters 

from lcg import prng
from scipy import stats

sample_size = 12000
sample_size_2 =30000
bins_1 = 30
bins_2= 20
bins_3 = 15
bins_4 = 10
bins_5 = 5

# let us split the sampled random numbers into equal bins
sample_1 = [prng()//(2**64//bins_1) for _ in range(sample_size)]
sample_2 = [prng()//(2**64//bins_2) for _ in range(sample_size)]
sample_3 = [prng()//(2**64//bins_3) for _ in range(sample_size)]
sample_4 = [prng()//(2**64//bins_4) for _ in range(sample_size)]
sample_5 = [prng()//(2**64//bins_5) for _ in range(sample_size)]
sample_6 = [prng()//(2**64//bins_1) for _ in range(sample_size_2)]
sample_7 = [prng()//(2**64//bins_2) for _ in range(sample_size_2)]
sample_8 = [prng()//(2**64//bins_3) for _ in range(sample_size_2)]
sample_9 = [prng()//(2**64//bins_4) for _ in range(sample_size_2)]
sample_10 = [prng()//(2**64//bins_5) for _ in range(sample_size_2)]



def get_frequencies(sample):
    """return the list of frequencies for successive bins"""
    frequencies = dict()
    for bin_ in sample:
        frequencies[bin_] = frequencies.get(bin_, 0) + 1
    return list(frequencies.values())

print("With 30 bins and 12000 as sample size;  ",*get_frequencies(sample_1))
print("With 20 bins and 12000 as sample  size;  ",*get_frequencies(sample_2))
print("With 15 bins and 12000 as sample  size  ",*get_frequencies(sample_3))
print("With 10 bins and 12000 as sample  size:  ",*get_frequencies(sample_4))
print("With 5 bins and 12000 as sample  size:  ",*get_frequencies(sample_5))
print("With 30 bins and 30000 as sample  size:  ",*get_frequencies(sample_6))
print("With 20 bins and 30000 as sample size:  ",*get_frequencies(sample_7))
print("With 15 bins and 30000 as sample  size: ",*get_frequencies(sample_8))
print("With 10 bins and 30000 as sample  size:  " ,*get_frequencies(sample_9))
print("With 5 bins and 30000 as sample  size;  ",*get_frequencies(sample_10))

# Let's explore more 
#  i couldn't find the connection, i think we have
#  to do the chi test or something like that







