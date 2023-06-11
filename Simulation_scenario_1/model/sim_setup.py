from numpy import random
MONTE_CARLO_RUNS = 3
seeds = [random.RandomState(i) for i in range(MONTE_CARLO_RUNS)]
seeds
TIMESTEPS = 1000
