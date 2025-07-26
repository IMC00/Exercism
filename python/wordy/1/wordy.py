def answer(question: str):
    print()
    processed_question = question[:-1]
    list_words = processed_question.split()[2:]
    if not list_words:
        raise ValueError("syntax error")

    result = None
    try:
        result = int(list_words.pop(0))
    except:
        raise ValueError("syntax error")

    while len(list_words) > 0:
        operator = list_words.pop(0)
        if not str.isalpha(operator):
            raise ValueError("syntax error")
        if operator not in ["multiplied", "divided", "plus", "minus"]:
            raise ValueError("unknown operation")
        if operator in ["multiplied", "divided"] and list_words.pop(0) != "by":
            raise ValueError("syntax error")

        number = list_words.pop(0) if list_words else None
        try:
            number = int(number)
        except:
            raise ValueError("syntax error")

        match operator:
            case "plus":
                result += number
            case "minus":
                result -= number
            case "multiplied":
                result *= number
            case "divided":
                result /= number

    return result
