from datetime import datetime

def string_to_date(date_string, format_str="%Y-%m-%d"):

    return datetime.strptime(date_string, format_str)

def date_to_string(date_obj, format_str="%Y-%m-%d"):

    return date_obj.strftime(format_str)

def get_month(date_obj):

    return date_obj.month
