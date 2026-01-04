"""Mathematical Foundations of Probability and Statistics."""

# ## Mathematical Foundations of Probability and Statistics (summary of book "Essential Math for Data Science")

# +
import math
from collections import defaultdict
from math import sqrt
from typing import Callable

import numpy as np
from scipy.stats import beta, binom, norm
from sympy import diff, integrate, limit, log, oo, symbols
from sympy.plotting import plot, plot3d


# -

# ### Chapter 1

# #### Key terms, concepts and samples

# *Functions* are expressions that define relationships between two or more
# variables. More specifically, a function takes input variables (also called
# domain variables or independent variables), plugs them into an
# expression, and then results in an output variable (also called dependent
# variable).
#
# Let's take a look on some examples:

# +
def func_example_1() -> None:
    """Demo example 1."""
    x_var = symbols("x_var")
    f_var = 2 * x_var + 1
    plot(f_var)


func_example_1()


# +
def func_example_2() -> None:
    """Demo example 2."""
    x_var = symbols("xvar")
    f_var = x_var**2 + 1
    plot(f_var)


func_example_2()


# +
def func_example_3() -> None:
    """Demo example 3."""
    x_var, y_var = symbols("x_var y_var")
    f_var = 2 * x_var + 3 * y_var
    plot3d(f_var)


func_example_3()


# -

# #### Elements of Calculus

# +
def example_summation() -> None:
    """Demonstrate summation of a simple sequence."""
    summation = sum(2 * ind for ind in range(1, 6))
    print(summation)


example_summation()


# +
def example_exponentiation() -> None:
    """Demonstrate exponentiation (power function)."""
    print(5**2)


example_exponentiation()


# +
def example_logarithm() -> None:
    """Compute a logarithm with a given base."""
    x_var = log(8, 2)
    print(x_var)


example_logarithm()


# +
def example_limit() -> None:
    """Evaluate a limit expression."""
    n_var = symbols("n")
    f_var = (1 + (1 / n_var)) ** n_var
    result = limit(f_var, n_var, oo)
    print(result)
    print(result.evalf())


example_limit()


# +
def example_derivative() -> None:
    """Differentiate a simple function."""
    x_var = symbols("x_var")
    f_var = x_var**2
    dx_f = diff(f_var)
    print(dx_f)


example_derivative()


# +
def example_partial_derivatives() -> None:
    """Compute partial derivatives of a multivariable function."""
    x_var, y_var = symbols("x_var y_var")
    f_var = 2 * x_var**3 + 3 * y_var**3
    dx_f = diff(f_var, x_var)
    dy_f = diff(f_var, y_var)
    print(dx_f)
    print(dy_f)
    plot3d(f_var)


example_partial_derivatives()


# +
def example_chain_rule() -> None:
    """Apply the chain rule in differentiation."""
    x_var, y_var = symbols("x_var y_var")
    _y_var = x_var**2 + 1
    dy_dx = diff(_y_var)
    z_var = y_var**3 - 2
    dz_dy = diff(z_var)
    dz_dx_chain = (dy_dx * dz_dy).subs(y_var, _y_var)
    dz_dx_no_chain = diff(z_var.subs(y_var, _y_var))
    print(dz_dx_chain)
    print(dz_dx_no_chain)


example_chain_rule()


# +
# fmt: off
def example_approximate_integral(
    a_var: float,
    b_var: float,
    n_var: int,
    f_var: Callable[[float], float],
) -> float:
    """Approximate an integral using the midpoint rule."""
    delta_x: float = (b_var - a_var) / n_var
    total_sum: float = 0.0

    for i_var in range(1, n_var + 1):
        midpoint: float = 0.5 * (2 * a_var + delta_x * (2 * i_var - 1))
        total_sum += f_var(midpoint)

    return total_sum * delta_x


def test_function_for_integral(x_var: float) -> float:
    """Sample function to integrate (x_var^2 + 1)."""
    return x_var**2 + 1


area_var: float = example_approximate_integral(
    a_var=0.0, b_var=1.0, n_var=5, f_var=test_function_for_integral
)
print(area_var)
# fmt: on

# +
def example_definite_integral() -> None:
    """Evaluate a definite integral symbolically."""
    x_var = symbols("x_var")
    f_var = x_var**2 + 1
    area = integrate(f_var, (x_var, 0, 1))
    print(area)


example_definite_integral()


# -

# #### Tasks

# 1. 62.6738 is rational because it’s a terminating decimal.
# 2. 100
# 3. 9
# 4. 125
# 5. Using compound interest (monthly compounding):
#
# $$
# A = 1000 \cdot \left(1 + \frac{0.05}{12}\right)^{12 \cdot 3} \approx 1161.60
# $$
#
# 6. Using continuous compounding:
#
# $$
# A = 1000 \cdot e^{0.05 \cdot 3} \approx 1161.83
# $$
#
# 7. 18
# 8. 10

# ### Chapter 2 

# #### Key terms, concepts and samples

# *Probability* is the level of confidence that an event will happen, often expressed as a percentage.
# Likelihood is similar to probability and often confused with it. In everyday language, they can be used as synonyms.
# The distinction is the following: probability is about quantifying predictions of future events, 
# whereas likelihood is measuring the frequency of events, that alady occured. 
# In statistics and machine learning, likelihood (based on past data) is used 
# to predict probabilities (about the future).
#
#
# *The probability of two independent events happening simultaneously* (joint probability) 
# can be calculated by multiplying the probability of each event. 
#
# For *mutually exclusive events* (that cannot occur simultaneously), the probability
# of event A or B happening is calculated by summing up their individual probabilities.
#
# *Conditional probability* is the chance of an event happening given that another event 
# has already occured. Bayes' formula allows us to flip conditional 
# probabilities in order to update our beliefs based on new data.

# +
def example_bayes_theorem() -> None:
    """Demonstrate Bayes' theorem with conditional probability."""
    p_coffee_drinker = 0.65
    p_cancer = 0.005
    p_coffee_drinker_given_cancer = 0.85
    p_cancer_given_coffee_drinker = (
        p_coffee_drinker_given_cancer * p_cancer / p_coffee_drinker
    )
    print(p_cancer_given_coffee_drinker)


example_bayes_theorem()


# -

# *Binomial distribution* describes the likelihood of getting exactly k successes in n trials, with a success probability of p in each trial.

# +
def example_binomial_distribution() -> None:
    """Compute probabilities for a binomial distribution."""
    n_trials = 10
    success_prob = 0.9
    for k_successes in range(n_trials + 1):
        probability = binom.pmf(k_successes, n_trials, success_prob)
        print(f"{k_successes} - {probability}")


example_binomial_distribution()


# -

# *The Beta distribution models* the likelihood of a probability value given 
# 𝑎 a successes and 𝑏 b failures. It allows to estimate the true probability of
# success based on observed outcomes. The Beta distribution is a type of probability distribution,
# meaning the area under its curve equals 1 (or 100%).
# To find the probability of a certain range, we need to calculate the area
# under the curve for that interval.

# +
def example_beta_distribution() -> None:
    """Evaluate cumulative probability for a Beta distribution."""
    alpha_param = 8
    beta_param = 2
    probability = beta.cdf(0.90, alpha_param, beta_param)
    print(probability)


example_beta_distribution()
# -

# #### Tasks
#
# 1. 12%
# 2. 82%
# 3. 6%

# +
# 4


def example_binomial_tail_probability() -> None:
    """Compute probability of 50 or more no-shows using the binomial distribution."""
    n_trials = 137
    success_prob = 0.40
    probability_sum = 0.0
    for x_successes in range(50, n_trials + 1):
        probability_sum += binom.pmf(x_successes, n_trials, success_prob)

    print(probability_sum)


example_binomial_tail_probability()

# +
# 5


def example_beta_coin_bias() -> None:
    """Evaluate posterior probability that a coin is biased (p > 0.5)."""
    heads_count = 8
    tails_count = 2
    probability = 1 - beta.cdf(0.5, heads_count, tails_count)
    print(probability)


example_beta_coin_bias()


# -

# ### Chapter 3

# #### Key terms, concepts and samples

# Descriptive statistics allows to summarize data (like averages and graphs).
# Inferential statistics uses samples to make conclusions about a bigger group (population).
# A population (or universe) is the entire group you want to study, like
# all people over 65 in North America or all golden retrievers in Scotland.
# Populations can be broad or narrow. A sample is a subst of the population, ideally 
# random and unbiased, used to make conclusions about the whole population. Working with 
# samples is often more practical, especially for large populations.
#
# ![](data:image/png;base64,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)

# +
def example_mean() -> None:
    """Compute the arithmetic mean of a sample."""
    sample = [1, 3, 2, 5, 7, 0, 2, 3]
    mean_value = sum(sample) / len(sample)
    print(mean_value)


example_mean()


# -

# The arithmetic mean is a type of average where the sum of all values is divided
# by the number of values. It’s a specific case of
# the weighted mean, where all values have equal weight.
#
# ![](data:image/png;base64,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)

# +
def example_weighted_mean() -> None:
    """Compute the weighted mean of a sample with given weights."""
    sample = [90, 80, 63, 87]
    weights = [0.2, 0.2, 0.2, 0.4]
    weighted_mean_value = sum(s * w for s, w in zip(sample, weights)) / sum(weights)
    print(weighted_mean_value)


example_weighted_mean()


# -

# The median is the central value in an ordered set of numbers.
# When the numbers are arranged in ascending order,
# the median is the middle value of the sequence.

# +
def median(values: list[int]) -> float:
    """Return the median of a numeric dataset."""
    ordered: list[int] = sorted(values)
    n_var: int = len(ordered)
    mid: int = int(n_var / 2) - 1 if n_var % 2 == 0 else int(n_var / 2)

    if n_var % 2 == 0:
        return (ordered[mid] + ordered[mid + 1]) / 2.0
    return ordered[mid]


def calc_median_example_1() -> None:
    """Print the median of a sample dataset."""
    sample: list[int] = [0, 1, 5, 7, 9, 10, 14]
    print(median(sample))


calc_median_example_1()


# -

# The mode is the value that occurs most frequently in a data set.
# It’s particularly useful for identifying which values occur most often when there are repeated values.

# +
def mode(values: list[int]) -> list[int]:
    """Mode of a numeric dataset."""
    counts: defaultdict[int, int] = defaultdict(int)

    for s_var in values:
        counts[s_var] += 1

    max_count_var: int = max(counts.values())
    return [v for v in set(values) if counts[v] == max_count_var]


def calc_mode_example_1() -> None:
    """Print the mode(s) of a sample dataset."""
    sample: list[int] = [1, 3, 2, 5, 7, 0, 2, 3]
    print(mode(sample))


calc_mode_example_1()


# -

# Variance is a measure of how far a set of numbers are spread out from their mean.
# It’s calculated as the average of the squared differences from the mean.
#
# ![](data:image/png;base64,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)

# +
def variance(values: list[int]) -> float:
    """Return the variance of a numeric dataset."""
    mean_1: float = sum(values) / len(values)
    return sum((v_var - mean_1) ** 2 for v_var in values) / len(values)


def calc_variance_example_1() -> None:
    """Print the variance of a sample dataset."""
    data: list[int] = [0, 1, 5, 7, 9, 10, 14]
    print(variance(data))


calc_variance_example_1()


# -

# Taking the square root is the inverse operation of squaring,
# so we take the square root of the variance to get
# the standard deviation (also called the root mean square deviation). 
#
# ![](data:image/png;base64,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)
#
# ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAR4AAADLCAYAAAC4Tfz+AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAABF1SURBVHhe7Z3Nkdw4FgbHLdkhJ2SDXJAFskAOyAAZoPucddd1zr2b2v5iEZxiFfiHAlCZEQi2qvgHEi/xALJbf72JiDRG8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPiDRH8YhIcxSPSIf8/Pnz7cuXL2+fP39++/79+9s///zz/s0cKB6Rzvj27dvbX3/99WeJfPiZ8vv37/c1xkfxiHQEmQ2SIeMJERHZzywoHpGO+PXr1x/JfPz48f2Tt7e///77z2cfPnx4/2R8FM8E/Pjx40+vyFzAWcuyx90CPTbbzzQsOAvuU811ZT0EFCKeT58+vX8yPopnAsp5AAopeW2hZy23TdnTuyIdgoMy22ToGSAUri3LLXz9+vXPdgh9FhTPBBDkiCLS2JOt0Kumge/dDyLjPJTOOmSUXFuudw0Zes0mc8UzCUnHKQR/mapvIVkL+0EktaQ33ztEeyXIMmsEzfesO2MGqXgmIr0ppZyc3EPkU9PgWeeMY47C2rzYo2VAzlyv8rMlXFPuAVlo7gH7mQXFMxkRBoVGuxcaO71yTQZDQHC8rXMXo1LOkW0pJY+yHr4v7x8ZLPd2FhTPZNBAadCRz5GhD9vWyIQg4VhrQST/JvNpt65vviulxTVeymtkFM+EZL6FUjOXcAQem3OcmXrjFmTSmCeSJeVc3bLcG5qNhuKZFHrHNNgre0qCgWPUDOsQYrKjDOOQYvbBd3snxZ/BkfqwHutQXhHFMyk07AQF5areMvM7j/aPmBKcGUpQ+IxsKT095zwCZ9SHdVnnFV+2VDwTk3Q+5YpsIpPZ995LSRCWxy+lSOAlQ7uVnSHRmrmmVhytT8g6967drCieyUnaTyE4COIzSfDckxrzGMuhWISVR8SIhc9unR/HIDvoJTM4Wp+geGRq0sApy8nMo9RkPEipDEB+zvkwVHkE22+RDvWlcG5blzViPlqfwDEfXbtZUTwvAIGR+YQtgVFDgudexrOEbCCBWhPoW2H/ZB5ke1uXe9hbH8UjfwKSbIDGQAO8IiCeBVKggS+HB2dAlrA1eDIZy7b3YJ/cky1Sewa19VmieF4cejsaAEsaOj9TZnjaQB3Ids4eYoWa4EHiZTaRidilCDnHZGRsw3rcE87/7EztCHvqcwvF88LQiLj5ZQOJiGgYI5PgrZ272EMp7TWSETAkSfa1vOYEH58lu2Eb9plhTE/i2VOfW2S7q+5Nz7y8eNJwCNCQRkNPOzKI8+qnQQQb12rZ24dcX86D65penhIhss4yK+OziJPvegnOvfVZwnpsU7a7V8Kh1n9JzxUinq1j9p6g0VOHsl5bYdtH2yM1jkOgrcF15HsKgcb15edsx/JWkHJsvluT2rPYW5+SCPvRerOieG6QVHrvU45nk+EJyyMQRDX7IBA53lpmlSyAAA18RvAtpV+SYRzb8fMjCbZib31K0sbKfbwSimcBjYYGkbR5NGjInP+9OZcaEhg1w7SI7mxRM4wpM4oR78ctqAfX61WHWaB4CmgQNIZRpYM0CdCj6Xukw3Wohet2thyoT/Z7NHvriWRyM9VpK4rnHQKGQCPoEjxHs4aW5PwJ1L3Bz1CB7QmKrYFxVqa1hIyrZugyCtwbRLpF6jOieN4h4JBOoLGP1Dg41wQ+hWFPzZLhTPlkpixbn4axP7Z71XmLGshGEc/Wazsbiue/ZGiRIMzcAssRSMCfWaj/HgysdXKfZsrg9jK9eAiAiCUBRW8fMkS4Vcr1eoaGTKEuZy2PiIN97B3uzQzXVCH/j6nFw02m96Uwf0FARUIEx5lwrLUgrlnaIOWVmFo8kQzSCZk8LT87gzKr2lNGGdaJnMHU4iHTIagZWyf1RxCjDKFEZuUlMh4KEmLik2GNiDyX6ed4Ip5SQDPIZ1kvy+uWEZlaPIBkGGplbodyxXwKkmOieG8xE5NXYkrx5HeHGGqVZOh1hXiQG/vdW5bnKjIzU4qHQEYwy5fgeJLF504uizyXqcXDECYwFEJEzPH4zozIc5lSPMyX5FE6y/weE+JxLkXk+Uw9uZxJWydvZQt5y12uY2rxiGwB2fCuF9kxDwvkOhSPvDyIZll8AHEtikdeHiRDtlO+cGrGcy2KR6TAjKcNikekwIynDYpHTqN8jYFXGBi68FcBeCu7fL3h7D9JciYRjxnPtSgeOQ1kQ8kLnPyMaPh3+cSI0uvrDTk/M55rUTxyCoiEgCXLIVtIACObQPaTX9btNbBz3mY816J45BQIVDIcSGaz/F05YJ2eAzviMeO5FsUjp0Cmk9+BS1az/H+5ysfVtW8GM0yjZAi3ZbnnD87n/Mx4rkXxyKkQ7Ane5TxO/lwJ8z61sA3ZByLYutxDzp19yHUoHjmVe3IhE+G7nv/2UMSzV1xSh+KRU8kfWysnlaEcZuVxOkOyDM96IedoxnMtikdOJfM7y4whmRAF8kfZehWPGc+1KB45jXJ+ZymUiIfhFusx+dvLkIu5KCa7I8OcJ+ec3+GSc1E8chp5l+fWY3RkU769zDp7njpdQWSzVhx2nY/ikVNBPveEkuxCXhvFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFIyLNUTwi0hzFMzj8d8H8/96/f/9+/0SkfxTP4PD/kCMei6Wm9ILiGZzv37+/ffz48f1fImOgeAbny5cvb1+/fn3/l8gYKJ7B+fTp05+sR2QkFM/gMG7/9evX+79ExkDxDEwmlnmyJTISimdgfv786cSyDIniGRgmlZlcFhkNxTMwnz9/fvv27dv7v0TGQfEMDPM7zPOIjIbiGRSeZCEef1Xi9WBujyE2GS+vUoz4cEHxDAqN78OHD+//kleBoTUdDkvkw88jdkCKZ1BoePR48jrkF4LpdEJENFpbUDyD4sTy65HhdfkKRd7lGi37VTyDQkMre741fvz48UdQzAWctaw57i3osdneeal/w32qvZ/lm+oRD786MxKKZ0CSctf8qkQ5D0AhU6ot9Kzltil7elfOmeCgjDgZejUIhWvLcgu8y8V2CH0kFM+AJOWugSBHFJHGnmyFXjUNfO9+EBnnoXTWIaPk2ta+IpF2MKLMFc+A0EAJ5FqSjlMI/ppM6RbJWtjPluOnN987RHslyDJrBM33rDtqBql4BmTP3+BJb0o5+vtdkU9Ng2edM445CrfmxGqWATlzvfh8Da4p94A2kHtQ7mMEFM+AEMRb5wIgwqBsFVcJjZ1euSaDISA43p7zHZHMj20tJY+yHr4v7x8ZLPd2JBTPgBDItfMAJTRQGnTkc2Tow7Y1MiFIONZaEMm/yXzareub70ppcY2X8uodxTMYma/ZS+ZbKDVzCUfgsTnHGa03fjaZNF7+5YFyrm5Z7g3NekTxDAYNjB7uCPSOabBX9pScK8eoGdYhxGRHGcYhxeyD7/ZOij+DI/VhPdahzIriGQzmTI7KgoadoKBc1VtmfufR/hFTgjNDCQqfkS2lp+ecR+CM+rAu68z6sqXiGQykc4Yoks6nXJFNZDL73nxUgrA8filFAi8Z2ppwEWnNfFMLzqgPZJ17125kFM9gnNkYk/ZTCA4C+EwSPPekduvVgAgrj4iRCp+tnR/HIUPoITs4oz6geKQbkqWcKYg0cMpyMvMoNRkPdSrrw885H4YqNbCPWulQXwrntnVZc93PqA9wzEfXbmQUz0DQcOnZz4TAyHzClsCoIcFzL+NZQjaQQK0J9K2wfzIPsr2tyz3srY/ikW6g8dMgzyRZ1HJ4cAZkCVuDJ5OxbPsI9kuWtkVsrdlSnxLFI91A493b896C4QnZztlDrFATPGQBZZ0yEbsUIedYZmRsx7pkI9Th7GxtL3vrs0TxSDecGWAJ3Nq5iz0gBYKH5RrJCBiSJPuilPUk+PiszGzYjv1mKNOLePbWZ0m2u+rePBvFMwg0wEeNdQv0qIjsyidBBBvnvOztQwKT8yAY08tTIkTWuZWV8Xnkyfc9BOiR+pTkXlO3WVE8g5Be8gxo9OyLINgL2z7aHqlxHAJtDQKS7ykEGvXk52zHci1IE+hrYnsGR+oTIuxH642M4hkE5g1o1EfJ0ITlEQiimn1wzhxvLbNKFkCABj4j+DJcWSNDObbl50cibMGR+oQM18p9zIbiGQR6v3tzJTXQkGnQR/eTwKgZpkV0Z06KB4YyZVZBgI8OdeB6zTzMAsXzRLYECpnDkeClpyU4j6bvkc6W7IsgukIM1Cn7PprB9UKyuFnqs4bieRIE4RYJ0Bj3DiU4FqIgSPcGP0MFtuc8tgbGWZnWLci69l6X3uDeINEzhtS9o3ieBNkLwVhDAncvmWch8Ckcu2bJUKZ8MlOWrU/D2B/bzTxvcRQ6IsSz9dqOiOJ5AunZCMSaDITsYm8vmIA/s+ydf3ilwNpK7tMs2dsjFM8TKGVQkwEQsHvnZmjIFI5z1vKIONjH3uHezHBNX0nIU4iHG5ZJz/TIDBd6pMx2KDXnyXAHWYnMwvDiQToEMoUJUHrkSIje9RFsv9az1yy39lKIphQP5/oI1uN4IrMwvHgiGaQT8vSl/GyNMlPaU8hGakm2w3lFPo+2R26s5/BEZmJ48SSAGYokOJFJj0MtspZMzJZPi+6RF/BEZmKajIeChJiEJUvolVKOOe97wzWEuiWrguzXYumV4cVD0C4vNgLqWT5ARpbzvTd/48SyzMgUOTySITjLN2trswTEReDvLXsFx7Y513vDQiTKuiIzMax4MvfBkKUkQ5ha8WQos7csj18LQ66IZ+0dnWRzW5+cifTOsOIh6AnK5Vu0PDHi8x4nl5dkYnztreQ80RKZjeHFUw5DyAwQEQE9QpaQ36Fak8ueiWWRERhWPGQDyRhYJogRT+8TywGxRDy3zpkh2N6hnFxDXlKVYwyfx2eCN8uRyDwV5dbLjkh0y5+fkOugfdERcK98yngcJxCeCKKMeG41Zj63d30uuT9lGWH+sHcUz5NJY14+2UI4fC7PBclwL/KEkWLGcxxb9pPJu0fLJ1s0+L1/g0euIeIx4zmO4nkyeTpHKWFSee39HnkOuU9mPMdRPE9m7ckW2c5MPSt1K99bYujCS5QItnw6WfMXBZ5F7pMZz3EUz5NZe7LFv2eaWEY2lGR4/Ixo+Hf5xIjS69PJnJ8Zz3EUz5Mpn2ylJ81E5ix/gyd1pF7UMfUth5LUNfNdvQZ2ztuM5ziKpwPSoMkCgCyIIJwFAjV1S2Zzq36s03Ng5z6Z8RxH8XRAAi7BSMOe6VclyHQokKxm+WJksjxK7RCTa0Th+m1d7skmc35mPMdRPB1AMKRRA4ExY+MufyN/OY+TuS7mfWphGyTNtdq63EPOnX3IMRRPBxAIadT09r0/3dnLPblEvj3/blru0V5xyf9RPB2AZMpGzTJDk5lAKtRt+X5SOcyKcBmS9XYNco5mPMdRPB1QBh7DLJYzkvmdZcaQTCj1joh7FY8Zz3EUTyekUVOQz2yU8ztLoUQ8DLdYj/r3MuRiLorhb5mVcp6cM5/3JsdRUDydUE4wz5jK512eW4/RkQ3zPnzPknX2PHW6gtyTteKwax+KpxMy/0GhN50R5HNPKMkuZH4UTyfQc0Y8y0fNIrOheDqBnj7iEZkdW3kn5MnWjBPLIksUT0cgnp5foBM5C8XTEczzzPjGssgSxSMizVE8ItIcxSMizVE8ItIcxSMizVE8ItIcxSMizVE8ItIcxSMizVE8ItIcxSMizVE8ItIcxSMizVE8ItIcxSMizVE8ItIcxSMizVE8ItIcxSMizVE8ItIcxSMijXl7+w8wCLTtYNv2ZgAAAABJRU5ErkJggg==)

# +
def std_dev(values: list[int]) -> float:
    """Return the standard deviation of a numeric dataset."""
    return sqrt(variance(values))


def calc_std_example_1() -> None:
    """Print the standard deviation of a sample dataset."""
    data_2: list[int] = [0, 1, 5, 7, 9, 10, 14]
    print(std_dev(data_2))


calc_std_example_1()


# -

# The most well-known probability distribution is the normal distribution 
# (also called the Gaussian distribution). It has a bell-shaped, 
# symmetric curve centered around the mean, with the spread determined by the standard deviation. 
# The further from the mean, the thinner the tails of the curve become.
# The probability density function (PDF) that defines the normal distribution is as follows:
#
# ![](data:image/png;base64,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)

# +
def normal_pdf(x_var: float, mean_1: float, std_dev_init: float) -> float:
    """Return the probability density for a normal distribution at x."""
    return (1.0 / (math.sqrt(2.0 * math.pi) * std_dev_init)) * math.exp(
        -((x_var - mean_1) ** 2) / (2.0 * std_dev_init**2)
    )


def calc_normal_cdf_value_example_1() -> None:
    """Print an example of a CDF value for a normal distribution."""
    mean_2: float = 64.43
    std_dev_sec: float = 2.99
    x_var: float = norm.cdf(64.43, mean_2, std_dev_sec)
    print(x_var)


calc_normal_cdf_value_example_1()


def calc_normal_ppf_value_example_1() -> None:
    """Print an example of a quantile (PPF) value for a normal distribution."""
    x_var: float = norm.ppf(0.95, loc=64.43, scale=2.99)
    print(x_var)


calc_normal_ppf_value_example_1()


# -

# Z-scores
#
# The normal distribution is often rescaled so that the mean is 0 
# and the standard deviation is 1. This results in the standard normal distribution.
#
# This transformation makes it easy to compare 
# variability across different normal distributions, 
# even if they have different means and variances.
#
# An important feature of the standard normal 
# distribution is that it expresses all values of 𝑥
# x in terms of standard deviations from the mean. 
# These transformed values are called Z-scores, or standardized scores.
#
# To convert a value 𝑥 to a Z-score, we use the simple scaling formula:
#
# ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJUAAABPCAYAAADiB4cGAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAQwSURBVHhe7ZvBUeNAEEWdFnGQBDGQAhEQAQkQgAPwnTN3rpy19Vz8rd6psRd5eiSN/F9Vl23Ziwz93N0z8h4mY5KxVCYdS2XSsVQmHUtl0rFUJh1LZdKxVCYdS2XSsVQmHUtl0rFUJh1LZdKxVCYdS2XSsVQmHUtl0rFUJh1LZdKxVCYdS5XE19fX9Pb2Nr28vEzH4/Hn6HS+//z8PJ1Op58j/fj4+Jje399/Hv0Lzy2FpUoAYQ6Hw/T6+jo9PT2d7yPS4+Pj+TGicaynWEjNOYgSROP4JeGysVSNUAFImKrT5+fn9PDw8DfB39/fZ7l6J5Xzcw4kLtH5YwXtiaVqhOpERCQUlYkKgmRUq56oGpbvBan1fri/BJaqET79MVlUKiURoYDbWkKZwahec29r85GqUdli1ZoReyksVTIkniSS5GsgGdWF2WtulOLEaiSRBZWL470rZcRSJUPSSWLZhnqieaomshYOS81TYKkaoUooYbFixCSqKvVC1ejaPEVbJpC+N5aqESUUiTS/ELEN0RL/1w5b0GqT80TUigngvS7RBi1VAxrKSSr31WoIBmpQayrnoCyQV+eMVUirQQKheR3vc4k2aKka4dNPsggN0aocJLN3ImN11Dl1XsQmOM7jntUyYqkSoArEZT6PEYljsQ32QO2XysQMhWScl/uifH+9sVSDQ/VBqiXa2m9plkorG5V8WkD8lACzRu3ygWmDCsTfnOhdEefQJBXyxOFUwadHg6kGxl6D6j2jRQAf6C3RJFVcYdRCpZnXzUVDpi5NZN2WVXRkJBW/15a4WSqSwy9EpWI5rWNUJBIooXh+biJjWc+OJQfWJdDffks0ScUnpNbL+UW1hN1TZTC/o3lQL5FQt1Qosw9SpaLH77lC1drpHiKbtJ+ooXHPFapMxl4im5SfKKG0q2vum2aptK1Qfu0iMndjjtdrMzU7trha2htNUkmoa/tQ+tLaHKh2/DuCdpp5u6Wd571ys1TsRSELybrU8vSaWzY/zbjcJFX5dQtC2wjsXdEKtflJuOXcF7OloiohEIFcBDJFwWIwxJv7YrZUzCXIEquPZqAok6Qz98dsqWhvl9oZ19WYo5DJWwv3y82DujGXsFQbgy0PKj7VXl/XibcjLHos1UZAlnIurcW1TeatYKk2AELpCgIrafb14oqax6pUI2zeWqqViZekytWyKtdoXyy0VCuj/2JVa2t6jgo1EpZqZZCGqA3gqlS0vpGwVCuCSJKqhtriaFclLNWK6HtoVKQS5iieQ6zRNpIt1YpIHFZ6JaO2PrBUK0MlIjRTIZqEGmFPqoalWhntUSnU8kasUMJSbQBmJl2aGW1PqoalMulYKpOOpTLpWCqTjqUy6Vgqk46lMulYKpOOpTLpWCqTjqUy6Vgqk46lMulYKpOOpTLpWCqTjqUyyUzTH13kfBGSs9unAAAAAElFTkSuQmCC)

# +
def z_score(x_var: float, mean_3: float, std_var_: float) -> float:
    """Return the z-score for a given observation x."""
    return (x_var - mean_3) / std_var_


def z_to_x(z_var: float, mean_4: float, std_var: float) -> float:
    """Convert a z-score back to the original x value."""
    return (z_var * std_var) + mean_4


def calc_to_z_scored_values_example_1() -> None:
    """Print an example of z-score calculation and back-conversion."""
    mean_5: float = 140_000
    std_dev_1: float = 3_000
    x_var: float = 150_000
    z_var: float = z_score(x_var, mean_5, std_dev_1)
    back_to_x: float = z_to_x(z_var, mean_5, std_dev_1)
    print(f"Z-score: {z_var}")
    print(f"Back-converted x_var: {back_to_x}")


calc_to_z_scored_values_example_1()


# -

# The coefficient of variation (CV) is a useful 
# tool for measuring relative spread. It allows you to compare 
# variability across different distributions, even if their means differ.
#
# ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAL4AAABjCAYAAAAl1LpsAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAAAT+SURBVHhe7ZzBUeNAEEWdFWmQBCmQAgkQAQEQAAFw5sydI2cfvfVV1VSjatkydnnV89/hlXatsYx3X/e0ekbs9vv9AcANxAdLEB8sQXywBPHBEsQHSxAfLEF8sATxwRLEB0sQHyxBfLAE8cESxAdLEB8sQXywBPHBEsQHSxAfLEF8sATxwRLEB0sQH37x+fl5eH19Pby8vBweHh4Oj4+Pi0dRXaMDiA8THx8fk9C73e4s3t7eyuttHcSHSd5K6lMoUKrrdQDxzcnS393dTSXO19fXdG4+C3TN7hWIb4zEztKrvj82pnOGn4P4xtzf3/9ILcGrMSLGKDiq8x1BfFPe399/hD6VyWOcqM53BPFNeXp6+pFZQVCNEbnU6dy+nIP4pqhsCaHjZrZCPf0Yp2CpxnQE8U0JmU/V7bmrc+w+oBuIb0rIfKx80UwQ40bq6AjENyVKnWPi61yIP1K2F4hvyvPz8yS0AuD7+3vxvBhp4SpAfFNUxkTWVxmTV2tzph9ReoH4xmilNi9iZdTBOdbt6Q7iwxQA2qOj1qV6+lXpMxqID5YgPliC+GAJ4oMliA+WID5Y0lZ8teDEaEvpcBtaia8FlbyUntHqY95XrhVH9aajP52PWpzJj9np7/Nx+pw8BsaijfgSOZbYdZSYIWpefQz5dS5eq8hSV+cFs8m4tBBfAoaMkj5Lq1XGLGvsNtTsoPcpECJgRMwMeXVSQZWvoaDRe89dwdT7IhiveXRYSb01mxdf/+k5o1ebprK01TbbXB4tPUUkyXQ+l0vnoECLz7g2zDzXZ/Pi52ysAFgaI+FFVZfrtSxSlUF1bc0MZFcPNi9+3iJbZfO15EfoVD7kc1FKaWbIr49AfOdbU/0sW2Lz4ud/TJUj1Zg1SPa4znzmiFJoxC5OfOdbU/0sW6KV+PNMfQ4qYfK1QnK9rhJntGdK4Tg2GV9UN7lxD3FJUEE/Ni9+rs0vqfGFOjZxrbiRjXuIS29q1dXJbdNrMmIJ9r/ZvPjRZhQSqxoTSL5TmTvLGXX/NW5qI4iEgvWaR32v6jPh72xe/Hl/vOrjB5JkqeUZ5JvcgD65H5sXX8yzfjX1RxlzKuPPA+nULAJj0kJ8oZvRLKuCQRIrCCS7XlNpsKZW18wQ1zoVKDAmbcQXKnPy9oWMZF57g5pXg6mfPWklfqAsr4yvbC3+0vVQaURt70tL8QEuBfHBEsQHSxAfLEF8sATxwRLEhwmtgahFvLQyHmjdQ3ubLt3U979BfJjQekgs6i2tZkt2BUYsGFZjuoD4MJG3hCw9cJ+DQ7NDNaYLiA8TkcnFUhmzJji6gPgw1fQh9LFt3TFGdN/jhPjwa9Pe0kM5a4OjC4gPv7ZpL5UwOTiWfilXJxAf7Op7gfjmrC1hcnCM8AwD4puzpkW5FByaHbouZCG+ObmEWRI/B0fU9xL+2Hu2DuKbk0uYpSfS9CxzjIlV3bjZ1XE+vgOIb0wuYUTVysy/fU7EjW3MFJQ60I7cohTK/pH1dYw2Z37AX9lf5/TnztsWEN+Y3L+vUCCotFFWz+WOWPurXLYK4hsz798rkyuLS3bNBnOx43zXuj6D+KaMtgXhXBDflDX9+5FBfFNG24JwLohvyry+r8aMDOIbkut7dWeqMaOD+IYow0fGd6zvBeKboqwvqnMOID5YgvhgCeKDJYgPliA+WIL4YAnigyWID5YgPhiyP/wDnuViYXDmBa8AAAAASUVORK5CYII=)

# Central Limit Theorem (CLT) states:
#
# If you take a sufficiently large sample from any distribution with a 
# finite mean and variance, the distribution of the sample means will tend 
# to follow a normal distribution, regardless of the original distribution’s shape.
#
# A confidence interval is a statistical tool that shows 
# how confident we are that a sample estimate (like the mean) 
# is close to the true population value.

# +
def critical_z_value(p_var: float) -> tuple[float, float]:
    """Return the critical z-values (lower, upper) for a given confidence level p."""
    norm_dist = norm(loc=0.0, scale=1.0)
    left_tail_area: float = (1.0 - p_var) / 2.0
    upper_area: float = 1.0 - ((1.0 - p_var) / 2.0)
    return norm_dist.ppf(left_tail_area), norm_dist.ppf(upper_area)


print(critical_z_value(p_var=0.95))


# -

# Using the Central Limit Theorem, we can estimate the margin of error (E) — 
# the range around the sample mean where the true population mean is 
# likely to fall, given a certain confidence level.
#
# ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQcAAADICAYAAADlYiRyAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAFiUAABYlAUlSJPAAABI4SURBVHhe7Z3NkeQ2s0XlluyQE7JhXJAFskAOyAAZoL3W2murdX9x5um+ycEkWUD9dKOmzonIYJEFgiAr8yIBsps/vImINCgOItKiOIhIi+IgIi2Kg4i0KA4i0qI4iEiL4iAiLYqDiLQoDiLSojiISIviICItioOItCgOItKiOIhIi+IgIi2Kg4i0KA4i0qI4iEiL4iAiLYqDiLQoDiLSojjIU/HXX3+9/fLLL2+fPn36bKzLY1Ac5Gn4/fff33744Ye333777e3PP/98+/nnnz+v//PPP/+VkHuiOMjT8NNPP33OFgLi8OOPPyoOD0JxkKfg77///pwlYGQN//7779sff/zx+bM8BsVBngYyhwgE9uuvv/73jTwCxUGeBrKEUSCYf5DHoDjIU8AQgqEEMMTIZGSdg5D7ojjI9jB8QAi4WxEyB+HQ4nEoDrI93JHAkjlABMM7FY9DcZDtYa4BIUAgGE4w78Bn71Q8FsVhEpwRB501nHhHeLrwGSFD4GlIhhM+Ffk+KA6TxCkT/ARZdVaWTJqxne93nSijbSIz6CkLZBIMO0tpSXt3nShTHGQWPWWBPNuP1cmxEbKGOrO+E4qDzKKnLJAhwzifQBZRx/KIw66TZYqDzKKnLJBJyXHIgFjUTKE+sLMbq+LARCDni/gxrALOra7L94niMEmdb0AImIREBMgS2LY6g57Z91W79b7+ijggAuNdGkQB2/VujNwPxWEShKAGyWirEFxdPZdsJigJXkSrM+rotscqnDPiwN8v8BlRZB0za/j+URwmIXAILO5EVAjWMag+GgK3yzowzqHbjo0BT+ZQh0cRC4XhNVAcJkl6Pf4VIMJQt9G77iYWFc7hGu4hDBx7N5NjvDoTEBBxpvEuBEFT5wG6MjtxTUAwTDFjeD0UhwnIBiIOZ3chyCAIohkyTFm1W7MS6liBOxUMnep583lnAZT7oDhMQM9JUJ1NBtKrIgyz/3yE8t24/5Ld2nuviEMyhlEYuA58V6Ft9TrdeldFPh7F4QQCMUGP0+P8Ceq6zJ8PY7sHxaw41GwJYyKWrCXXgvMODK3Yxj6IB2V2fXxc5lEcDojDr9guAUHP3bXvkiUzQuAIcMSQYE9GgLGdaxMoy/ZkEpTnOtRsQ54TxUG+gcCumQGwjo1BHxEli3pPaEsEa9VkDq+U3ARzLATcew+nGOIkW5HHoDjITSRziDhkWPHIIVayht3nd54dxUFuAjFgroIJy9zKzcTkoyBrcMLz8SgOchfozZl3eKQoQCZAzRoej+IgTwUZg3MN74PiIE8DWQlZA1mKPB7FQZ4GMoZbHx+XeRQHeQoy19A9T0EmgXAwIZo5D/72AyHJ5KXZxjqKgzwFBHie4BzJo92IB0ZZtnGblSXbWMoaioNsz9lcAxlCAj+PjbNMBpF9MVnDKyYfCgFPcJ/dmiQTOJprqMOJiMBYl+JwHV4x+TDo9RO4R7cnCXoerLr0txt8Tz3j0ONou1xGcZAPIX8SjiiwRAAyFKhQbma+gOyCelhWUv+4XS6jOMiHgBDEEAYCGCGo5LuZ/zqV+YYxw0jdDDWwSxmIfEFxkA8nvTtWYS5h9i5D9q/ZR4YtGVKQPRwNX+RbFAf5cAjoBHf+kUyyhvqPZY44mlfI0AVRYOKTzz7vMI/iIFuQOYNkCrNzDZA/Gx+HJXlwCpGZFRr5guIgW5DeH+Pz7FxDOMsIqM+MYR3FQbYhk4rYbNYgj0NxkG3IvAA2DhHk/VEcZCvIGBhS1LsO8jEoDrIVzA9g8vEoDiLSojiISIviICItioOItCgOItKiOIhIi+IgIi2Kg4i0KA4i0qI4iEiL4iAiLYqDiLQoDiLSojiISIviICItioOItCgOItKiOIhIi+IgIi2Kg4i0KA7yUvDWq0+fPn023sV5j5fd8A9xeQcndebVex2U4UU9+c/aLFnf9f2dioO8BARiXppDENcX6CAS15L3cfIv9fPiX9a7t3XleKON7/jcBcVBXoK8i7P+2/sENnbNezSpi33Hnh/x4d0bvKuzkmNVQ1B2fUeH4iAvAYFIwI4pf3p6AnoV9mHfMUuI6IyiwTa+ow0Iy+4v7lEc5CXIMKLr5dmOrZL9xpfwJKMY3/fZld0ZxUFeAnpphhZjbx1xWB335/X+Z+KAVVKWfVneYzL0kSgO8rIgFAw1CNrVOYcqAGfiUAWA9Qxj6nJXkVAc5GXJ3EA3eXgJApp9sTEbORMHMpWUZ66Cbbu+OFhxkJckwd1NUs5QBeBMHGpWgRiNZTOsueV26qNQHOTlIEtAFK4VBqiZQxUAqOJwKSPJLdYdn3VQHOSloOdmnE8wJnDZNgb4JWbFIVC+DilCfdZiNxQHeRkITEQBq0FKMI+3HWdIUB+JQ62TLIVtZAqVZA7XHP/RKA7yMvCMA0HKRCABHKNHxyrcvegega5QH4F99BBUFQKCHxszB4SqE40dUBzkKSHILgVvJT30kdUJwfT8GJ+PSLkqLLQLEUCE6nwDgjFmLBmajGV3QXGQpyS98+yEYoL9yMbnHMgKxmDuYL/UgQAR6NjYrioaiEmyjq7sLmwnDlysXOwZ4wfcjfER3VnoCe91S4teDWfFEVkeOSBt5bgJApasH53DbL2wUhZy7JQfe232RxQgvTZL9mP7RwVZ2sVvR/vPsgDEpJbNdd+R7cSBC50fHsNJWc92llzgKC+OtBu0awYcg/PBUTL2vMf5EFjURU9F3RFcnHGE7Z11ortS70pZSHnOn+BhyTq/ecg22kY9+T7Xjjrkfmw5rCBg+LGxI2cCHG9Hh6DdM0QEcXrOhc+3ZkIEVuoMCSQCdOzV2D4awTz2aCv1rraB4/FdzVYiFtQVaFMVmhjrXZvlNrYUhzgXdvaD43zVeXaBdq/SBdQ1JHAIlkqCbdzONo6dzOzoeq/Uu1IWoWAb+9RjU5ZttGuk+gdlzjoQuZ4txSFDhrEXxQlq70Ig7egYtH0VAqY75xVqxlXTcUhAjfV3ZUdW6l1tQwSD5ciYYVBfhKdmWlm/dB6yxpbiEAcYHQZHwMECcw87ppK0fZUEzi2Zw1lgRnzGtqUsgciy66lX6l1tQ35rvkPoWXItunZESPI9n1mmXpZyP7YTh+pcOAEOhggQNGwbHe6MOPyqjT3WKrRzlTj42LOvMF67SsRnbBvr6YXrsgbnSr0rZTOkwJIBZDjBZ373kfw2mcPg95LHsJ044BBxmM5WiMOt2kyAMrxBsDqjjm57rCOBc/T9LLUnrlBvzq+SYyYDS9BRT83KVuqdLVuFpB6PZcpWkaogCmffy+1sJw5xCnqvCgHLd7uAU9Zsoxrt77ZjR858j8wBEtz1WtUgxCqI0jg0y29Qg3ul3tmyXI+sj0PIiOXoB5Wx3SOp+xltB7YTh7Nep27Dearz7cQ1P+69MgeI0FBX0vSaRV0iY/tRqFbqnSlbBWP8vbN/ysr7s9WVr85C71NhuFHnAroyu3CNQycYbs0cAteSOhEdPkd8av1sJ3jHHjhlu/OYqTfMlM1xxt/yrA3yPmx15atDnKWMOBw90SVw/NS3Yux3C9SxSs791mMDgTiSa8G1C8nSxpQ+mcOY0s/WC7NlMwk67s862zH5GLa68kfPN1RwOpx6dKYOyo5j/hnrHHuFaxw6wXB27mRPl7KlTOjWgEdouWZYzb4ITGwUYtow1rFS70rZnPf4e0Ysax3yvmwhDgRjgh6HQCQS2HWJo/A9Vh1sN2jfDARMzi/CSLDmfOs5si3nzucjco0SVNSRYCdoKwQg31Vx4LiUHYN4pd6VsnzHsapIsY31sQ3yvny4OKSXWbE43UcSZ1819gs14DsjeCsIyBjMI6mTcqTxEdyxLqCeBCFlI1CsIxKVlXpXygI+QBmstmG3OaUI+auw1bBC7gO9LWk6wcjyUu9LcKYsAXkkPiv1rraB71OW9pwJ4EeROZNH2k4oDiITZLh1SeS+JxQHkQnIGnYYzr4nioPIBcgWXi1rAMVB5AJkDEyUdjA/wnfJLMaJ3A7mdZhb2R3FQeQEJkbJGsagZ3smKBEHhCF3ZbqybEMQuINDGfbdHcVB5IRkBSPcWSHIyRwCAsE2RKIKRG7tUg+3jvmMSOyO4iByQOYaumcbyAIiBLntmiwDOxo2RFTMHESeGDKBox4eISALqA9qJUPAEIGOiIqZg8iTkixgZoIxJCsgmzi6s2HmILIxBDy9/tmtSbKGmQBGRMgYmHuIMNR5iBEzB5FNYRhAcGJHtycJeIJ85u8oEuyxo7mGYOYgsiEJTESBZZ1MrFCOzGKV1Mu+Xb1g5iCyIQRsDGEgSBGCSr679i9CU+9RZmDmILI56eWxCj37bNbQTVYS9F29wcxBZHPIEBLEmUBM1nA2oRgiLmPZS+Jg5iDyBOSJxmQKs3MNZAwRgHECkv3ZfpQZmDmIPAH1oSU+r8w1IAKUr7dDkxVgdS6DjARB4Rh10pJ1tu/6156Kg7w09OAJ6JmsIRDUiAPGEKHWM2YTVYQ6q0KyE4qDvDR1iLAapGQEzDmwH4LA512zgGtQHOTlyRCBYJcvKA7y8pD2Y/I1ioOItCgOItKiOIhIi+IgIi2Kg4i0KA4i0qI4iEiL4iAiLYqDiLQoDiLSojiISIviICItioOItCgOItKiOIhIi+IgIi2Kg4i0KA4i0qI4iEiL4iAiLYqDiLQoDgX+PXl92cgl2/WVZrxVaYW8iYmXs/CKON7lcC15DwTvcMh/dR6t1k85jovx7oeZY/NWqvHFMR38q3nK5rw49iV47wR+sOuLZt4TxaGAY+JACX4CJs6cJc6cV5rhdDtC22YhCCjPuxsIOJasX/sK+tR3Zlw3AjdviWL97I1ReZ0c2+s+Z+Q9mJSjTSxZvyQQKac4KA7fgBPiHNhZgBBEOOCO0PYZIoRjpkGA0Hte8/amGXHguiZ4a7DWfRHhkHbSrojXWdaGiFCmnleOdxb09fgzmcn3juIwUB3k7A1I6ZF2hLbPkF5yFMFcg1E0ZqDObj+uJYITQaV+1hHjSoKfejrStqPvEbTUXX8/jtsdL2Q4gbH/rr/te6I4DGTIMPZMBFB1epzz2tT70dD+GSiHjal2emoCdRX26a4L16vWl+HBKCSUS7s6khUcZQ7JECJClbNMiPpoS9pl5qA4fEN6jtG5cJram5D2nmUWH8lRYFXSw2JH4jBTzwj7jteFazX25HzmGo9lIw5HwX8pc8jvR3AjUizZ5yhjAL5P+3J8MwfF4SvqfAPOgaNnNp1tYxBdggBkn1U76+FmoK2X4Dg5Vz5X6ndnQTVD0vWZYCM4E9x1zqFyljlUwUsGkOHEUZ1pX7IdM4cvKA4FnCfO1dkqcbRVO+o1K6TAiFZn1NFtj0EVwrH3vqc4cDyCbwYEhGNS/kggUybnUannRB05r5oRjOdTrwmknJmD4vAVcYxxrE2wVgfaAZycIO6Mc+i2YwkOPlMOOxMHPl9LevJxXqEjgU1QjwFcOcscarvHYWFEpf62ZAujEJk5fEFxKOAonWMgDHUbjrabWFQ4h0skGLFRAGqQHfXgMxCg1HE0RAhJ7S8JA8xmDuNvGFHBIEOYsW3pIMwcFIf/pzrWONuOA9Ug6crsRALgjFlxuAV66a7+CkFKOXrsXGO2He2TID8aeqXd4+8TUcGg1oMgZJkytIn1S8L2PaM4/Ed1njHNruBU9DgzVGdbMfa7BeqYIcc7EodxeLVCFZ+jbIDrTFBi9Zpz/KNjn2UOEEG6lDnQJrZRX11mf+pn/ajtr4Di8B+Mi3GKox4JcBSEAaeZgfI4+qrd6pAJgEvknI962XHcTi86mzFxHtSB8bmD43M9qbOeP4F5FPxce+o8+p3y/fgbHZ3TCPV2+78iLy8OBGKCHqfAYRPUdZnxM3bLOPw9oI0zcG6UrYGYNJ/rUc8zZTE+XyJBinH9Rur17KwGJ23KbxFBo435bWo7+Uzb+T7ZCNu6c6qk/mQOtI/1o/KvwEuLAz1hdcgZu9TzvBfp4VZt7HHrNeDcCCCsC2gCk/3rEOAIAiv1duS7I6tj/VpXZ2QFFfbNeURM+HyW9Yx1xl45g3j5zEH+r9fMmJsAuldvmZ79I+Acck6IxYygydcoDiLSojiISIviICItioOItCgOItKiOIhIi+IgIi2Kg4i0KA4i0qI4iEiL4iAiLYqDiLQoDiLSojiISIviICItioOItCgOItKiOIhIi+IgIi2Kg4i0KA4i0vD29j9iZSDo+S/9mQAAAABJRU5ErkJggg==)

# +
# fmt: off
def confidence_interval(
    p_var: float, 
    sample_mean: float, 
    sample_std: float, 
    n_var: int
) -> tuple[float, float]:
    """Return the confidence interval for a sample mean given confidence level p."""
    lower_var, upper_var = critical_z_value(p_var)
    lower_ci_var: float = lower_var * (sample_std / sqrt(n_var))
    upper_ci_var: float = upper_var * (sample_std / sqrt(n_var))
    return sample_mean + lower_ci_var, sample_mean + upper_ci_var


print(confidence_interval(p_var=0.95, sample_mean=64.408, sample_std=2.05, n_var=31))
# Based on a sample of 31 golden retrievers with an average body weight of 64.
# 408 pounds and a standard deviation of 2.05, I am 95% confident that the
# population mean lies between 63.686 and 65.1296.
# fmt: on
# -

# The p-value helps us test whether an observed effect is statistically significant.
#
# We start by stating a null hypothesis (H₀):
#
# - The variable being studied has no real effect, and any positive results are due to random chance.
#
# Then we define an alternative hypothesis (H₁):
#
# - The observed effect is real and caused by the variable being studied — also called the treatment or independent variable.
#
# If the p-value is small enough (usually less than 0.05), 
# we say the result is statistically significant and reject 
# the null hypothesis in favor of the alternative.

# #### Tasks

# +
# Task 1
print(np.mean([1.78, 1.75, 1.72, 1.74, 1.77]))
print(np.std([1.78, 1.75, 1.72, 1.74, 1.77]))


# Task 2
mean_6: float = 42
std_dev_2: float = 8
x_var_2: float = norm.cdf(30, mean_6, std_dev_2) - norm.cdf(20, mean_6, std_dev_2)
print(x_var_2)


# Task 3
def critical_z_value_2(
    p_var: float, mean_7: float = 0.0, std: float = 1.0
) -> tuple[float, float]:
    """Return the lower and upper critical z-values."""
    norm_dist = norm(loc=mean_7, scale=std)
    left_area: float = (1.0 - p_var) / 2.0
    right_area: float = 1.0 - ((1.0 - p_var) / 2.0)
    return norm_dist.ppf(left_area), norm_dist.ppf(right_area)


e_var: tuple[float, float] = (
    1.715588 + critical_z_value(0.99)[0] * (0.029252 / np.sqrt(34)),
    1.715588 + critical_z_value(0.99)[1] * (0.029252 / np.sqrt(34)),
)
print(e_var)

# Task 4
mean_pr: float = 10345
std_dev_3: float = 552
p1: float = 1.0 - norm.cdf(11641, mean_pr, std_dev_3)
p2: float = p1
p_value: float = p1 + p2

print("Two-tailed p-value:", p_value)
if p_value <= 0.05:
    print("Two-tailed test passed")
else:
    print("Two-tailed test failed")
# fmt: on
