class Luhn:
    """Class that verifies a card number is valid via Luhn's method."""
    def __init__(self, card_num: str):
        """
        Creates a verifier class for card numbers.

        :param card_num: Number to be verified.
        """
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        """
        Verifies that card_num is a valid card number.

        :return: Whether the number is valid or not.
        """
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