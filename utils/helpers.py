import datetime

def format_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d, %Y")
    except:
        return date_str
