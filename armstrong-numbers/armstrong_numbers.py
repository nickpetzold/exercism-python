def is_armstrong(number):
    digit_list = list(str(number))
    length = len(digit_list)
    digit_power_list = [int(n)**length for n in digit_list]
    if sum(digit_power_list) == number:
        return True
    return False
