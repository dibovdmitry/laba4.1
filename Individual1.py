#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — целое положительное число, числитель; поле second — целое положительное
число, знаменатель. Реализовать метод ipart() — выделение целой части дроби
first/second. Метод должен проверять неравенство знаменателя нулю.
"""


class IntegerPart:

    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Введите целое, положительное число, числитель: "))
        self.second = int(input("Введите целое, положительное число, знаменатель: "))

    def display(self):
        print(f"Целая часть дроби {self.first} / {self.second}:")

    def ipart(self):
        if self.second == 0:
            return 0
        else:
            return self.first // self.second


def make_ipart(first, second):
    if type(first) and type(second) != int:
        raise ValueError()
    else:
        return IntegerPart(first, second)


if __name__ == "__main__":
    integer_part = IntegerPart()
    f = make_ipart(0, 0)
    f.read()
    f.display()
    print(f.ipart())
