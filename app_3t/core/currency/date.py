import datetime

def date ():
    result = input('Inpput required date in format YYYYMMDD, in case you need current date just input - now ')
    if result.lower() == 'now':
        result = datetime.datetime.now().strftime('%Y%m%d')
    try:
        try_date = datetime.datetime.strptime(result, '%Y%m%d')
    except: print("Invalid date format, please try again "); return date()
    if int(result[0:4]) < 2012:
        print("3T app Taras Kravchuk addition supports exchange rates only beginning from 2012-th yaer, please try again")
        return date()
    else: return result

def date_input ():
    result = input('Inpput required date in format %Y%m%d%H%M, in case you need current date just input - now ')
    if result.lower() == 'now':
        result = datetime.datetime.now().strftime('%Y%m%d%H%M')
    try:
        try_date = datetime.datetime.strptime(result, '%Y%m%d%H%M')
    except: print("Invalid date format, please try again "); return date_input()
    else: return result

