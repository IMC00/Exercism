class StackUnderflowError(Exception):
    pass

def evaluate(input_data: list[str]):
    print()
    dict_words: dict[str, list[str | int]] = {}
    result_stack: list[int] = []

    def is_integer(tok: str) -> bool:
        return tok.strip().lstrip("+-").isdigit()

    def expand_tokens(tokens: list[str | int]) -> list[str | int]:
        result = []
        def expand_token(token: str):
            if is_integer(token): # If it's a number
                return [int(token)]
            token = token.lower()
            if token in dict_words:
                return dict_words[token]
            return [token]

        for tok in tokens:
            result += expand_token(tok)
        return result

    def apply_op(stack, op):
        def need(n):
            if len(stack) < n:
                raise StackUnderflowError("Insufficient number of items in stack")

        op = op.lower()

        if op == "+":
            need(2)
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif op == "-":
            need(2)
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif op == "*":
            need(2)
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
        elif op == "/":
            need(2)
            b = stack.pop()
            a = stack.pop()
            if b == 0:
                raise ZeroDivisionError("divide by zero")
            stack.append(a // b)
        elif op == "dup":
            need(1)
            stack.append(stack[-1])
        elif op == "drop":
            need(1)
            stack.pop()
        elif op == "swap":
            need(2)
            stack[-1], stack[-2] = stack[-2], stack[-1]
        elif op == "over":
            need(2)
            stack.append(stack[-2])
        else:
            raise ValueError("undefined operation")
    for line in input_data:
        line = line.strip()
        if line.startswith(":"): # This is a definition
            parts = line.split()

            if is_integer(parts[1]):
                raise ValueError("illegal operation")
            name = parts[1].lower()
            body_tokens = parts[2:-1]

            dict_words[name] = expand_tokens(body_tokens)
            print(dict_words)

        else:   # This is the main stack...
            tokens = line.split()
            expanded_tokens = expand_tokens(tokens)

            for tok in expanded_tokens:
                if isinstance(tok, int):
                    result_stack.append(tok)
                else:
                    apply_op(result_stack, tok)
            print(expanded_tokens)

    return result_stack

