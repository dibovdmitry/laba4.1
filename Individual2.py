#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Money для работы с денежными суммами. Число должно быть представлено
# двумя полями: типа int для рублей и копеек. Дробная часть (копейки) при выводе на экран
# должна быть отделена от целой части запятой. Реализовать сложение, вычитание, деление
# сумм, деление суммы на дробное число, умножение на дробное число и операции сравнения.


class Money:

    def __init__(self, ruble=0, kopey=0):
        self.ruble = ruble
        self.kopey = kopey

    def read(self):
        self.ruble = int(input("Рубли: "))
        self.kopey = int(input("Копейки: "))
        if kopey >= 100

    def display(self):
        print(f"Ваш счёт: {self.ruble}, {self.kopey} ")


if __name__ == '__main__':
    m = Money(4, 5)
