import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


np.random.seed(40)
n = np.random.random(size=4)
print('Random Number: ', n)

j = np.random.random_integers(1, 6, size=6)
print('Integers: ', j)

sns.set()
_ = plt.hist(np.random.random(size=1000))
plt.show()

""""
The np.random module and Bernoulli trials:
You can think of a Bernoulli trial as a flip of a possibly biased coin. Specifically, each coin flip has a probability p
of landing heads (success) and probability 1-p of landing tails (failure). We will write a function to perform n 
Bernoulli trials, which returns the number of successes out of n Bernoulli trials,
perform_bernoulli_trials(n, p), each of which has probability p of success. To perform each Bernoulli trial, 
use the np.random.random() function, which returns a random number between zero and one.
"""

def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number= np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number<p:
            n_success += 1

    return n_success

# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)
# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100, 0.05)


# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed=True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')

# Show the plot

plt.show()

# Above is an example of PMF - Probability Mass Function: a set of probabilities of discrete outcome
# Binomial distribution: The number of success (r) in (n) Bernoulli trial with probability of success (p) is said to be
# binomially distributed. Coin flip is an ex of Bernoulli trial which gives discrete outcome.

v_Binomial = np.random.binomial(5, 0.1, size=100)
print(v_Binomial)
_ = plt.plot(v_Binomial, marker='.', linestyle='none')
plt.show()

""""Poisson Distribution
the Poisson distribution is a limit of the Binomial distribution for rare events. This makes sense if you think about 
the stories. Say we do a Bernoulli trial every minute for an hour, each with a success probability of 0.1. We would do 
60 trials, and the number of successes is Binomially distributed, and we would expect to get about 6 successes.
"""
# Draw 10,000 samples out of Poisson distribution: samples_poisson
samples_poisson = np.random.poisson(10, size=10000)

# Print the mean and standard deviation
print('Poisson:     ', np.mean(samples_poisson),
                       np.std(samples_poisson))

""""Exponential Distribution
If the wait time between one event and another is not related, then it is called exponential distribution.
syntax: np.random.exponential(n, size)
"""

""""Hacker Statictics Part II
"""

# Creating a dummy dataset - The number of games played between each no-hitter in the modern era (1901-2015) of Major
# League Baseball is stored in the array nohitter_times.

nohitter_times = np.random.random_integers(0, 6540, size=10000)

print(np.max(nohitter_times), np.min(nohitter_times), nohitter_times.shape)

# Seed random number generator
np.random.seed(42)

# Compute mean no-hitter time: tau
tau = np.mean(nohitter_times)
print('tau:{}'.format(tau))
# Draw out of an exponential distribution with parameter tau: inter_nohitter_time
inter_nohitter_time = np.random.exponential(tau, 100000)

# Plot the PDF and label axes
_ = plt.hist(inter_nohitter_time, bins=50, normed=True, histtype='step')
_ = plt.xlabel('Games between no-hitters')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()

def ecdf(data):
    # Number of data points: n
    n = len(data)
    # x-data for the ECDF: x
    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n
    return x, y


# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)

# Overlay the plots
plt.plot(x_theor, y_theor)
plt.plot(x, y, marker='.', linestyle='none')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Show the plot
plt.show()

# Pearson Correlation Coefficients
def pearson_r(x, y):
    """Compute Pearson correlation coefficient between two arrays."""
    # the Pearson correlation coefficient is the ratio of the covariance to the geometric mean of the variances
    # of the two data sets
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x, y)

    # Return entry [0,1]
    return corr_mat[0, 1]

""""
# Specify slopes to consider: a_vals
a_vals = np.linspace(0, 0.1, 200)

# Initialize sum of square of residuals: rss
rss = np.empty_like(a_vals)

# Compute sum of square of residuals for each value of a_vals
for i, a in enumerate(a_vals):
    rss[i] = np.sum((fertility - a*illiteracy - b)**2)

# Plot the RSS
plt.plot(a_vals, rss, '-')
plt.xlabel('slope (children per woman / percent illiterate)')
plt.ylabel('sum of square of residuals')

plt.show()

"""

#  If we have a data set with n repeated measurements, a bootstrap sample is an array of length n
# that was drawn from the original data with replacement

"""" Bootstrap sample from rainfall dataset
for i in range(50):
    # Generate bootstrap sample: bs_sample
    bs_sample = np.random.choice(rainfall, size=len(rainfall))

    # Compute and plot ECDF from bootstrap sample
    x, y = ecdf(bs_sample)
    _ = plt.plot(x, y, marker='.', linestyle='none',
                 color='gray', alpha=0.1)

"""

# here we get a function like np.mean for e.g. calculated over a bootstrap dataset from data.
def bootstrap_replicate_1d(data, func):
    return func(np.random.choice(data, size=len(data)))

# another function to take multiple bootstrap samples
def draw_bs_reps(data, func, size=1):
    # Draw bootstrap replicates.

    # Initialize array of replicates: bs_replicates
    bs_replicates = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_replicates[i] = bootstrap_replicate_1d(data, func)

    return bs_replicates


# Confidence intervals of rainfall data
# A confidence interval gives bounds on the range of parameter values you might expect to get if we repeated our
# measurements. For named distributions, you can compute them analytically or look them up, but one of the many
# beautiful properties of the bootstrap method is that you can just take percentiles of your bootstrap replicates to
# get your confidence interval. Conveniently, you can use the np.percentile() function.

def draw_bs_pairs_linreg(x, y, size=1):
    # Perform pairs bootstrap for linear regression.

    # Set up array of indices to sample from: inds
    inds = np.arange(len(x))

    # Initialize replicates: bs_slope_reps, bs_intercept_reps
    bs_slope_reps = np.empty(size)
    bs_intercept_reps = np.empty(size)

    # Generate replicates
    for i in range(size):
        bs_inds = np.random.choice(inds, size=len(inds))
        bs_x, bs_y = x[bs_inds], y[bs_inds]
        bs_slope_reps[i], bs_intercept_reps[i] = np.polyfit(bs_x, bs_y, 1)

    return bs_slope_reps, bs_intercept_reps

# Hypothesis
# Permutation sampling is a great way to simulate the hypothesis that two variables have identical probability
# distributions. A permutation sample of two arrays having respectively n1 and n2 entries is constructed by
# concatenating the arrays together, scrambling the contents of the concatenated array, and then taking the first n1
# entries as the permutation sample of the first array and the last n2 entries as the permutation sample of the second
# array.

def permutation_sample(data1, data2):
    # Generate a permutation sample from two data sets.

    # Concatenate the data sets: data
    data = np.concatenate((data1, data2))

    # Permute the concatenated array: permuted_data
    permuted_data = np.random.permutation(data)

    # Split the permuted array into two: perm_sample_1, perm_sample_2
    perm_sample_1 = permuted_data[: len(data1)]
    perm_sample_2 = permuted_data[len(data1):]

    return perm_sample_1, perm_sample_2

# when we plot the actual datasets and the permutation datasets above, if these two overlap then it would mean that Null
# hypothesis is valid, else that would mean that the distribution of data into two dataset is not similar.

# Hypothesis testing is assessment of how reasonable the observed data are assuming a hypothesis is true.

# p-value: the probability of obtaining a value of your test statistics that is at least as extreme as what was
# observed, under the assumption that null hypothesis is true.

def draw_perm_reps(data_1, data_2, func, size=1):
    #Generate multiple permutation replicates.

    # Initialize array of replicates: perm_replicates
    perm_replicates = np.empty(size)

    for i in range(size):
        # Generate permutation sample
        perm_sample_1, perm_sample_2 = permutation_sample(data_1, data_2)

        # Compute the test statistic
        perm_replicates[i] = func(perm_sample_1, perm_sample_2)

    return perm_replicates

""" p-value example
def diff_of_means(data_1, data_2):
    # Difference in means of two arrays.

    # The difference of means of data_1, data_2: diff
    diff = np.mean(data_1) - np.mean(data_2)

    return diff

# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = diff_of_means(force_a, force_b)

# Draw 10,000 permutation replicates: perm_replicates
perm_replicates = draw_perm_reps(force_a, force_b,
                                 diff_of_means, size=10000)

# Compute p-value: p
p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates)

# Print the result
print('p-value =', p)
"""

# Steps for hypothesis testing:
# Clearly state the Null Hypothesis
# Define your test statistics
# Generate many sets of simulated data assuming the null hypothesis is true
# Compute the test statistic for each simulated data set
# The p-value is the fraction of your simulated data sets for which the test statistic is at least as extreme as for
# the real data.