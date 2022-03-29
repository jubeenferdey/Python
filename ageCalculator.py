from datetime import date

class Time:
    def __init__(self, date):
        self.time = date

    def age(self):
        today = date.today()
        date_this_year = date(today.year, self.time.month, self.time.day)
        return today.year - self.time.year - (date_this_year > today)

time = Time(date(2002,3,18))
print(time.age())