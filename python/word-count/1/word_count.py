def count_words(sentence):
    result = {}
    cur_word = ""
    l = len(sentence)
    for i, char in enumerate(sentence):
        if str.isalnum(char) or (char == "'" and 0 < i < l-1 and sentence[i-1].isalnum() and sentence[i+1].isalnum()):
            cur_word += char.lower()
        else:
            if cur_word != "":
                result[cur_word] = result.get(cur_word, 0) + 1
                cur_word = ""
    if cur_word != "":
        result[cur_word] = result.get(cur_word, 0) + 1

    return result