def is_armstrong_number(number):
    list_of_numbers = [int(x) ** len(list(str(number))) for x in list(str(number))]
    return sum(list_of_numbers) == number
