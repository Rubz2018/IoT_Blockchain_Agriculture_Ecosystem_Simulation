import math
import random

# from .state_variables import initial_state
# from .sys_params import params


def p_ph_delta(params, substep, state_history, previous_state):
    delta_ph = params['random_variation1'] * previous_state['ph']
    return {'delta_ph': delta_ph}


def p_soil_moisture_delta(params, substep, state_history, previous_state):
    delta_soil_moisture = params['random_variation2'] *\
        previous_state['soil_moisture']
    return {'delta_soil_moisture': delta_soil_moisture}


def p_node(params, substep, state_history, previous_state):
    next_node = params['next_node']
    return {'next_node': next_node}


def s_ph(params, substep, state_history, previous_state, policy_input):
    ph = previous_state['ph'] + policy_input['delta_ph']
    return 'ph', round(ph, 3)


def s_soil_moisture(params, substep, state_history, previous_state, policy_input):
    soil_moisture = previous_state['soil_moisture'] + \
        policy_input['delta_soil_moisture']
    return 'soil_moisture', round(soil_moisture, 3)


def s_node(params, substep, state_history, previous_state, policy_input):
    node = random.randint(1, 100)
    return 'node', node
