def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not target_time:
        return None
    online_users = 0

    for start_time, output_time in permanence_period:

        if not start_time or not output_time:
            return None

        if start_time <= target_time <= output_time:
            online_users += 1

    return online_users
