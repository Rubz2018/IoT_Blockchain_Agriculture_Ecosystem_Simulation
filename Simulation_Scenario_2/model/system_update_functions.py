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


def p_cwp_reward(params, substep, state_history, previous_state):
    reward = params['param_reward']
    return {'reward': reward}


def p_cwp_penalty(params, substep, state_history, previous_state):
    penalty = params['param_penalty']
    return {'penalty': penalty}


def s_ph(params, substep, state_history, previous_state, policy_input):

    ph = previous_state['ph'] + policy_input['delta_ph']
    return 'ph', round(ph, 3)


def s_soil_moisture(params, substep, state_history, previous_state, policy_input):

    soil_moisture = previous_state['soil_moisture'] + \
        policy_input['delta_soil_moisture']
    return 'soil_moisture', round(soil_moisture, 3)


def s_ph_wt(params, substep, state_history, previous_state, policy_input):
    ph = previous_state['ph']
    ph_wt = previous_state['ph_wt']
    ph_wt = 0
    if 2 < ph < 3:
        ph_wt = policy_input['reward']
    else:
        ph_wt = -policy_input['penalty']
    return 'ph_wt', ph_wt


def s_soil_moisture_wt(params, substep, state_history, previous_state, policy_input):

    soil_moisture = previous_state['soil_moisture']
    soil_moisture_wt = previous_state['soil_moisture_wt']
    soil_moisture_wt = 0
    if 35 < soil_moisture < 40:
        soil_moisture_wt = policy_input['reward']
    else:
        soil_moisture_wt = -policy_input['penalty']
    return 'soil_moisture_wt', soil_moisture_wt


def s_cwp(params, substep, state_history, previous_state, policy_input):
    cwp = previous_state['cwp']
    ph = previous_state['ph']
    ph_wt = previous_state['ph_wt']
    ph_wt = 0
    if 2 < ph < 3:
        ph_wt = policy_input['reward']
    else:
        ph_wt = -policy_input['penalty']

    soil_moisture = previous_state['soil_moisture']
    soil_moisture_wt = previous_state['soil_moisture_wt']
    soil_moisture_wt = 0
    if 35 < soil_moisture < 40:
        soil_moisture_wt = policy_input['reward']
    else:
        soil_moisture_wt = -policy_input['penalty']

    total_weight = ph_wt + soil_moisture_wt
    if total_weight > 0:
        cwp += total_weight
    else:
        cwp -= total_weight
    return 'cwp', cwp


def s_node(params, substep, state_history, previous_state, policy_input):
    node = random.randint(1, 100)
    return 'node', node
