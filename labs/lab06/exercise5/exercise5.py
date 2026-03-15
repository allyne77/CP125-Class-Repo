def audit_zero_trust(baseline_set, current_log_list):
<<<<<<<<< Temporary merge branch 1
    current_set = set(current_log_list)
    authorized = baseline_set & current_set
    alerts = current_set - baseline_set
    inactive = baseline_set - current_set

    return authorized, alerts, inactive

=========
   pass
>>>>>>>>> Temporary merge branch 2
