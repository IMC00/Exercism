from datetime import datetime, timedelta


def add(moment : datetime):
    return moment + timedelta(seconds=1e9)


