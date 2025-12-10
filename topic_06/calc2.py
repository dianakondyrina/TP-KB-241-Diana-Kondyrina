from operations2 import enter_num, enter_oper, operation 

print("Напишіть числа чи 'exit' аби закінчити") 
while True: 
    num1 = enter_num("Введіть перше число: ") 
    if num1 is None: 
        break 
    
    num2 = enter_num("Введіть друге число: ") 
    if num2 is None: 
        break 
    
    operator = enter_oper() 
    result = operation(num1, num2, operator) 
        
    print("Результат:", result)