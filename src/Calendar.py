import time

DAYS = ('sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
MONTHS = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')

def format_date(date_list): # dmyyyy to yyyymmdd
    return '0'*(4-len(date_list[2])) + date_list[2] + '0'*(2-len(date_list[1])) + date_list[1] + '0'*(2-len(date_list[0])) + date_list[0] 

class Calendar:
    FORMATTED_DATE = ("year", "month","day","weekday","time")
    def __init__(self):
        '''
        Current local date formatted as such:
            year (full)
            month - (01, ..., 12)
            day of month - (01, ..., 31)
            weekday - 0:sunday 6:saturday
            time - hour:minute:second | 24-hour Clock
        '''
        self.now_str = time.strftime("%Y %m %d %w %H:%M:%S",time.localtime())
        self.now_f = dict(zip(Calendar.FORMATTED_DATE,self.now_str.split()))

    def print_now(self):
        print(self.now_str)
        print(
            f'''
            year: {self.now_f["year"]}
            month: {MONTHS[int(self.now_f["month"])]}
            day: {self.now_f["day"]}
            day of week: {DAYS[int(self.now_f["weekday"])]}
            time: {self.now_f["time"]}
            '''
        )


class Reminder:
    def __init__(self, reminder_title: str, sub_reminders: list, year=0, month=1, day=1,): # reminders = [name, time]
         self.day = day
         self.month = month
         self.year = year

         self.reminders = reminders
         self.keypad = Keypad(reminders)


