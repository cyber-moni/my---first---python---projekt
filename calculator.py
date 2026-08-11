a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
operation = input(" Введите репарацию (+,-,*,/):")
if operation == "+":
  result = a + b
elif operation == "-":
  result = a - b
elif operation == "*":
  result = a * b
elif operation == "/":
  result = a/ b
print("Ответ:" ,result)
