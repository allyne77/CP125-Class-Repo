def get_legit_power_users(log_data, bot_ids, threshold):
    user_id, power_score = i

    for i in log_data : 
        if user_id in bot_ids:
            

