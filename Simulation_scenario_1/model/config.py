'''
Definition :

'''
from cadCAD import configs
from cadCAD.configuration import Experiment
from cadCAD.configuration.utils import config_sim
from .state_variables import initial_state
from .partial_state_update_block import partial_state_update_block
from .sys_params import params
from .sim_setup import MONTE_CARLO_RUNS, TIMESTEPS

del configs[:]
sim_config = config_sim(
    {
        'N': MONTE_CARLO_RUNS,  # number of monte carlo runs
        # number of timesteps - 147439 is the length of uniswap_events
        'T': range(TIMESTEPS),
        'M': params,  # simulation parameters
    }
)

exp = Experiment()

exp.append_configs(
    sim_configs=sim_config,
    initial_state=initial_state,
    partial_state_update_blocks=partial_state_update_block
)
