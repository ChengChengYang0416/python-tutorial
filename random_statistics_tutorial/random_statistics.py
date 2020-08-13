# random
import random

data = random.choice([2, 6, 1, 70, 34])
print(data)
data = random.sample([2, 6, 1, 70, 34], 3)
print(data)
random.shuffle(data)
print(data)
data = random.random()              # random number from 0 to 1
print(data)
data = random.uniform(0.0, 5.0)     # random number from 0 to 5
print(data)
data = random.normalvariate(100, 10)
print(data)

# statistics
import statistics as stat

data = stat.mean([2, 5, 8, 4])
print(data)
data = stat.median([2, 5, 8, 4, 300])
print(data)
data = stat.stdev([2, 5, 8, 4, 3])
print(data)