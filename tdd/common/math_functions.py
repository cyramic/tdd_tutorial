def add_numbers(a:int, b:int)->int:
    try:
        return int(a) + int(b)
    except ValueError as errinfo:
        return False
