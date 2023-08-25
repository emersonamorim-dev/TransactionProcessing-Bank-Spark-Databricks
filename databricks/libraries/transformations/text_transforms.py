def normalize_value(value, min_value, max_value):

    return (value - min_value) / (max_value - min_value)

def calculate_percentage(part, whole):

    return 100 * float(part) / float(whole)

def round_to_nearest_int(value):

    return round(value)
