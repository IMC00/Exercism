class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        num_len = len(self.card_num)

        if num_len < 2: return False
        if not self.card_num.isdigit(): return False

        is_second_digit = False
        total = 0
        for idx in range(num_len-1, -1, -1):
            digit = int(self.card_num[idx])
            if is_second_digit:
                digit *= 2
                if digit > 9:
                    digit -= 9

            total += digit
            is_second_digit = not is_second_digit

        if total % 10 == 0:
            return True

        return False

