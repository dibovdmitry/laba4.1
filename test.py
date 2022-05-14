#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Time для работы со временем в формате «час:минута:секунда». Класс
должен включать в себя не менее четырех функций инициализации: числами, строкой
(пример «23:59:59»), секундами и временем. Обязательными операциями являются:
вычисление разницы между двумя моментами времени в секундах, сложение времени и
заданного количества секунд, вычитание из времени заданного количества секунд,
сравнение моментов времени, перевод в секунды, перевод в минуты (с округлением
до целой минуты)
"""

from datetime import datetime, time, date, timedelta
from time import gmtime


class Time:

    def __init__(self, hour=None, minute=None, second=None, time_str=None, minutes=None, seconds=None):
        self.time2 = None

        if hour is not None:
            self.time1 = time(hour, minute, second)
        elif time_str is not None:
            self.time1 = datetime.strptime(time_str, "%H:%M:%S").time()
        elif minutes is not None:
            h1 = int(minutes // 60 % 24)
            m1 = minutes % 60
            s1 = int(m1 % 1 * 60)
            self.time1 = time(h1, int(m1), s1)
        elif seconds is not None:
            time_obj = gmtime(seconds)
            self.time1 = time(time_obj.tm_hour, time_obj.tm_min, time_obj.tm_sec)
        else:
            self.time1 = None

    def read(self):
        hour_1 = int(input("Для получения доп. времени:\n"
                           "Введите час: "))
        minute_1 = int(input("Введите минуту: "))
        second_1 = int(input("Введите секунду: "))
        self.time2 = time(hour_1, minute_1, second_1)

    def display(self):
        print(f"Вы ввели время: {self.time1}, {self.time2}")

    def delta(self):
        if self.time1 > self.time2:
            time_interval = (
                    datetime.combine(date.today(), self.time1) -
                    datetime.combine(date.today(), self.time2)
            )
        else:
            time_interval = (
                    datetime.combine(date.today(), self.time2) -
                    datetime.combine(date.today(), self.time1)
            )

        return time_interval.seconds

    def add_sec(self, sec):
        time_delta1 = timedelta(
            hours=self.time1.hour,
            minutes=self.time1.minute,
            seconds=self.time1.second
        )
        time_delta2 = timedelta(seconds=sec)

        return time_delta1 + time_delta2

    def subtract_sec(self, sec):
        time_delta1 = timedelta(
            hours=self.time1.hour,
            minutes=self.time1.minute,
            seconds=self.time1.second
        )
        time_delta2 = timedelta(seconds=sec)

        return time_delta1 - time_delta2

    def compare(self):
        return self.time1 > self.time2

    def to_seconds(self):
        sec = self.time1.hour * 3600 + self.time1.minute * 60 + self.time1.second
        return sec

    def to_minutes(self):
        minutes = self.time1.hour * 60 + self.time1.minute
        if self.time1.second > 30:
            minutes += 1

        return minutes


if __name__ == '__main__':
    t1 = Time(hour=10, minute=20, second=45)
    t1.read()
    t1.display()
    print(f"Разница составляет: {t1.delta()} секунд")
    s = int(input("Введите количество секунд: "))
    print(f"Сумма: {t1.add_sec(s)}")
    print(f"Разница: {t1.subtract_sec(s)}")
    print(f"Первое время больше второго: {t1.compare()}")
    print(f"Время в секундах: {t1.to_seconds()}")
    print(f"Время в минутах: {t1.to_minutes()}")
