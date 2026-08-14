answer = "да"

while answer == "да":
  a = int(input("Введите первое число:"))
  b = int(input("Введите второе число:"))
  operation = input("Введите операцию (+, -, *, /, %):")
  if operation == "+":
    result = a + b
  elif operation == "-":
    result = a - b
  elif operation == "*":
    result = a * b
  elif operation == "/":
    if b == 0:
      print(" Не делится на ноль!")
      result = None
    else:
      result = a / b
  elif operation == "%":
    result = a % b
  else:
    print("Неизвестное действие!")
    result = None
  if result is not None:
    print("Ответ:" , result)
  answer = input("Хотите посчитать ещё? да/нет?").lower().strip()
  while answer !="да" and answer !="нет":
    answer = input("Пожалуйста, введите да или нет: ").lower().strip()
  
 print ("До свидания !")
    
  



