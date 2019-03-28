from app_3t.core.task import *

def hour_():
    try:
        currency = input('Please input starting currency, only 3 currency supported: UAH, EUR and USD ')
        if currency.upper() != "EUR" and currency.upper() != "UAH" and currency.upper() != "USD":
            raise Exception
    except Exception:
        print("3T-app supports only 3 currencies: UAH, EUR and USD, please try again ")
        return hour_()
    else:
        mode = input("in case your task is estimated per hours, input 0 or hour\n"
                     "in case your task is estimated per full task, input 1 or full")
        try:
            if mode != '0' and mode != '1' and mode.lower() != 'full' and mode.lower() != 'hour':
                raise Exception
        except Exception:
            print(f"Unknown command '{mode}', only commands: hour, 0, full and 1 are accepted\nPlease try again ")
            hour_()
        if mode == '0' or mode.lower() == 'hour':
            price_hour = input('Please input price per hour ')
            try:
                price_hour = float(price_hour)
            except ValueError:
                print("Invalid price input, please use only numbers. Please try again. ")
                return hour_()
            return [mode, price_hour, currency]
        elif mode == '1' or mode.lower() == "full":
            price_full = input('Please input full price of your task ')
            try:
                price_full = float(price_full)
            except ValueError:
                print("Invalid price input, please use only numbers. Please try again. ")
                return hour_()
            return [mode, price_full, currency]
