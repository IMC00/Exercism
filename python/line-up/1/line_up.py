def line_up(name, number):
    number_str = str(number)
    def choose_suffix():
        if number_str.endswith("1") and not number_str.endswith("11"):
            return "st"
        if number_str.endswith("2") and not number_str.endswith("12"):
            return "nd"
        if number_str.endswith("3") and not number_str.endswith("13"):
            return "rd"
        return "th"

    return f"{name}, you are the {number_str + choose_suffix()} customer we serve today. Thank you!"
