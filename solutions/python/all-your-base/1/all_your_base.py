def rebase(input_base, digits, output_base):
    if input_base < 2: raise ValueError("input base must be >= 2")
    if output_base < 2: raise ValueError("output base must be >= 2")
    reversed_digits = reversed(digits)
    mult = 1
    base_10_num = 0
    for dig in reversed_digits:
        if dig < 0 or dig >= input_base: raise ValueError("all digits must satisfy 0 <= d < input base")
        base_10_num += dig * mult
        mult *= input_base

    if base_10_num == 0: return [0]
    result = []
    while base_10_num >= output_base:
        result += [base_10_num % output_base]
        base_10_num = base_10_num // output_base

    if base_10_num > 0:
        result += [base_10_num]

    return list(reversed(result))