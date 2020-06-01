import datetime
import locale
import holidays

today = datetime.date.today()

def say(CONFIG):
    country_holidays = holidays.CountryHoliday(CONFIG["holidays"]["countrycode"])
    locale.setlocale(locale.LC_ALL, CONFIG["general"]["locale"])

    saystring = f"Most éppen {datetime.datetime.now().strftime('%B %d. %A %H:%M')}  "

    saystring += f",  {country_holidays.get(today)} " if today in country_holidays else ""

    saystring += "van. "

    return saystring
