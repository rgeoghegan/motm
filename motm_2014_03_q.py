print """########################################\n#\n#       Module of the Month:\n#       --------------------\n#                q\n#\n########################################"""
import q

def f():
    import datetime
    now = datetime.datetime.now()
    q(now)
    return now

@q
def f2(year):
    import datetime
    now = datetime.datetime.now()
    return now.replace(year=year)
    return "world"
