
class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        if self.hours < 10 and self.minutes < 10 and self.seconds < 10:
            return f'0{self.hours}:0{self.minutes}:0{self.seconds}'
        if self.hours < 10 and self.minutes < 10:
            return f'0{self.hours}:0{self.minutes}:{self.seconds}'
        if self.hours < 10:
            return f'0{self.hours}:{self.minutes}:{self.seconds}'
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def increment(self, seconds):
        self.seconds += self.seconds

        while self.seconds >= 60:
            self.seconds -= 60
            self.minutes += 1

        while self.minutes >= 60:
            self.minutes -= 60
            self.hours += 1

    def to_seconds(self):
        """ Returns the number of seconds represented by this instance"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        return MyTime(0,0,self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0,0,self.to_seconds() - other.to_seconds())

def add_time(t1,t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0,0, secs)  

t1 = MyTime(1, 15, 42)
t2 = MyTime(3, 50, 30)
t3 = t2 - t1
print(t3)