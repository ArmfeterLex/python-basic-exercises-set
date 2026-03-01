#1
a = input("Введите свои фамилию и имя - ")
print("Привет, {a}!")
family_name = a.split()
print(f"Количество символов в фамилии: {len(family_name[0])}, количество символов в имени: {len(family_name[1])}")

#2
x = 0
y = 0.0

x = int(input())
y = float(input())

print(type(x))
print(type(y))

y = float(x)
x = int(y)

s = str(y)
print(len(s))
y = float(s)

n = int(input("Ввод: "))
integer_part = int(y)
fractional_part = y - integer_part
formatted_fractional_part = "{:.{}f}".format(fractional_part, n)
print(f"Целая часть: {integer_part}")
print(f"Дробная часть: {formatted_fractional_part}")

#3
my_bool = input("Введите True или False: ").lower() == 'true'

print(f"Введенное значение: {my_bool}")

print(f"True как строка: {str(True)}, как число: {int(True)}")
print(f"False как строка: {str(False)}, как число: {int(False)}")





#З1
def sum_first_and_last(n):
    s = str(n)
    return int(s[0]) + int(s[-1])

def sum_first_and_second_to_last(n):
    s = str(n)
    return int(s[0]) + int(s[-2])

def sum_first_and_second(n):
  s = str(n)
  return int(s[0]) + int(s[1])

def product_last_and_second_to_last(n):
    s = str(n)
    return int(s[-1]) * int(s[-2])

def swap_first_and_last_digits(n):
    s = str(n)
    return int(s[-1] + s[1:-1] + s[0])

def swap_first_and_second_to_last_digits(n):
    s = str(n)
    return int(s[-2] + s[1:-2] + s[0] + s[-1])

def swap_first_and_second_digits(n):
    s = str(n)
    return int(s[1] + s[0] + s[2:])

def swap_last_and_second_to_last_digits(n):
    s = str(n)
    return int(s[:-2] + s[-1] + s[-2])

def make_number_from_parts(m, n):
    ms = str(m)
    ns = str(n)
    return int(ms[:2] + ns[-2:])
  
def make_number_from_outer_and_middle_parts(m, n):
    ms = str(m)
    ns = str(n)
    return int(ms[0] + ns[2:4] + ms[3])

#З2
import math

def expr1(x):
    return math.e**x - abs(math.sin(math.pi*x/3)) + 1.7

def expr2(x):
    return math.pow(math.sqrt(math.pow(x, 4)),1/5) + math.pow(math.sqrt(x*(x-4)),1/5) + math.log(abs(x-20.5))

def expr3(x):
    return (1/7 + math.log(math.sqrt(x))) * math.e

def expr4(x):
    return math.sqrt(x) * math.sin(x**2) - 1.3

def expr5(x):
    return math.sqrt(abs(math.exp(math.sin(x)))) + 2*math.log(3*x) - 1/9

def expr6(x):
    return (math.sqrt(1 + x**2) + abs(math.log(x**3))) / (1.6 + x)

def expr7(x):
    return (1/5*math.sqrt(5*x)) / abs(math.log(x**2)-1.3)/2

def expr8(x):
    return 1.8 + math.log(4 - (2/7) - math.tan(math.sin(5*x/3)))


x = 2

print(f"Результат 1: {expr1(x)}")
print(f"Результат 2: {expr2(x)}")
print(f"Результат 3: {expr3(x)}")
print(f"Результат 4: {expr4(x)}")
print(f"Результат 5: {expr5(x)}")
print(f"Результат 6: {expr6(x)}")
print(f"Результат 7: {expr7(x)}")
print(f"Результат 8: {expr8(x)}")