def find_anagrams(main_word, candidates):
    sorted_word = sorted(main_word.casefold())
    result = [x for x in candidates if x.casefold() != main_word.casefold() and sorted(x.casefold()) == sorted_word]
    return result
