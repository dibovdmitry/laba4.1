#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Money для работы с денежными суммами. Число должно быть представлено
двумя полями: типа int для рублей и копеек. Дробная часть (копейки) при выводе на экран
должна быть отделена от целой части запятой. Реализовать сложение, вычитание, деление
сумм, деление суммы на дробное число, умножение на дробное число и операции сравнения.
"""


class Money:
    def __init__(self, rubles, copei):
        self.rubles = rubles
        self.copei = copei

    def read(self):
        self.rubles = int(input("Введите рубли: "))
        self.copei = int(input("Введите копейки: "))

    def display(self):
        print(f"Вы ввели денежную сумму: {self.rubles}, {self.copei}")

    def first(self):
        print(f"Денежная сумма по умолчнию: {self.rubles}, {self.copei}")

    def sub(self, other):
        return Money(self.rubles - other.rubles, self.copei - other.copei)

    def sub_checker(self):
        if self.copei < 0:
            self.rubles -= 1
            self.copei = 100 + self.copei
            return self.rubles, self.copei

    def sub_display(self):
        print(f"Вычитание денежных сумм: {self.rubles}, {self.copei}")

    def add(self, other):
        return Money(self.rubles + other.rubles, self.copei + other.copei)

    def add_checker(self):
        if self.copei >= 100:
            self.rubles += 1
            self.copei -= 100
            return self.rubles, self.copei

    def add_display(self):
        print(f"Сумма: {self.rubles}, {self.copei}")

    def mul(self, other):
        return Money(self.rubles * other.rubles, self.copei * other.copei)

    def mul_checker(self):
        while self.copei >= 100:
            self.rubles += 1
            self.copei -= 100
        return self.rubles, self.copei

    def mul_display(self):
        print(f"Умножение сумм: {self.rubles}, {self.copei}")

    def div(self, other):
        return Money(self.rubles // other.rubles, self.copei // other.copei)

    def div_checker(self):
        while self.copei >= 100:
            self.rubles += 1
            self.copei -= 100
        return self.rubles, self.copei

    def div_display(self):
        print(f"Деление сумм: {self.rubles}, {self.copei}")

    def mul_by_fraction(self, fraction):
        return Money(self.rubles * fraction, self.copei * fraction)

    def mul_by_fraction_checker(self):
        while self.copei >= 100:
            self.rubles += 1
            self.copei -= 100
        return self.rubles, self.copei

    def mul_by_fraction_display(self):
        print(f"Умножение суммы на дробное число: {'{:0.0f}'.format(self.rubles)}, {'{:0.0f}'.format(self.copei)}")

    def div_by_fraction(self, fraction):
        return Money(self.rubles / fraction, self.copei / fraction)

    def div_by_fraction_checker(self):
        while self.copei >= 100:
            self.rubles += 1
            self.copei -= 100
        return self.rubles, self.copei

    def div_by_fraction_display(self):
        print(f"Деление суммы на дробное число: {'{:0.0f}'.format(self.rubles)}, {'{:0.0f}'.format(self.copei)}")

    def comparison(self, other):
        if self.rubles < other.rubles:
            print(f"Сумма {self.rubles} меньше {other.rubles}")
        elif self.rubles > other.rubles:
            print(f"Сумма {self.rubles} больше {other.rubles}")
        else:
            print(f"Суммы равны")
            return self.rubles


if __name__ == "__main__":
    s1 = Money(40, 20)
    s1.first()

    s2 = Money(0, 0)
    s2.read()
    s2.display()

    s3 = s1.add(s2)
    s3.add_checker()
    s3.add_display()

    s4 = s1.sub(s2)
    s4.sub_checker()
    s4.sub_display()

    s5 = s1.mul(s2)
    s5.mul_checker()
    s5.mul_display()

    s6 = s1.div(s2)
    s6.div_checker()
    s6.div_display()

    s7 = s2.div_by_fraction(17.52)
    s7.div_by_fraction_checker()
    s7.div_by_fraction_display()

    s8 = s2.mul_by_fraction(20.1)
    s8.mul_by_fraction_checker()
    s8.mul_by_fraction_display()

    s9 = s1.comparison(s2)
