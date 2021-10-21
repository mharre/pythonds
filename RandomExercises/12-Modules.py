import random

# rng = random.Random()
# dice_throw = rng.randrange(1,7)
# delay_in_seconds = rng.random() * 5.0

def make_random_ints(num, lower_bound, upper_bound):
    """
    Generates random list of n length with lower bound and upper bound capabilities but will produce duplicates
    """
    rng = random.Random()
    result = []
    for i in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result

# print(make_random_ints(1320, 3,25))

def make_random_ints_no_dups(num, lower_bound, upper_bound):
    rng = random.Random()
    result = []
    for i in range(num):
        while True:
            canidate = rng.randrange(lower_bound, upper_bound)
            if canidate not in result:
                break
        result.append(canidate)
    return result

xs = make_random_ints_no_dups(5, 1, 10000000)
print(xs)