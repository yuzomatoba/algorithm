def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    students_watching_class = 0
    for starting_class, ending_class in permanence_period:
        if not isinstance(starting_class, int) or not isinstance(ending_class, int):
            return None
        if starting_class <= target_time <= ending_class:
            students_watching_class += 1
            return students_watching_class
