"""
Model parameters.


"""
import random
import math
params = {
    # random number generation for pH
    'random_variation1': [(random.uniform(-0.005, .001))],
    # random number genration for soil moisture
    'random_variation2': [random.uniform(-0.001, 0.001)],
    # fised reward
    'param_reward': [100],
    'param_penalty': [50]



}
