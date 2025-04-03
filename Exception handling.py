def division_calculator(x,y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print("Enter a number other than 0")
    finally:
        print("program completed")
    
division_calculator(50,0)