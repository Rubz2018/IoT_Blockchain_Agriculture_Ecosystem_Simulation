from .system_update_functions import s_ph_wt, s_soil_moisture_wt, s_cwp, p_cwp_penalty, p_cwp_reward, s_node, p_ph_delta, p_soil_moisture_delta, s_ph, s_soil_moisture

# partial_state_update_block = [
#     # Run first
#     {
#         'policies': {}, # Ignore for now
#         # State variables
#         'variables': {
#             'population': s_population
#         }
#     },
#     # Run second
#     {
#         'policies': {}, # Ignore for now
#         # State variables
#         'variables': {
#             'food': s_food
#         }
#     }
# ]

partial_state_update_block = [
    {
        'policies': {
            'delta_ph': p_ph_delta,
            'delta_soil_moisture': p_soil_moisture_delta,
            'reward': p_cwp_reward,
            'penalty': p_cwp_penalty

        },
        'variables': {
            'ph': s_ph,
            # Receives policy_input of soil_moisture increase or decrease
            'soil_moisture': s_soil_moisture,
            'node': s_node,
            'cwp': s_cwp,
            'ph_wt': s_ph_wt,
            'soil_moisture_wt': s_soil_moisture_wt

        }
    }
]
