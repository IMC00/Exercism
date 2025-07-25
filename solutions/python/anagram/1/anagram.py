def find_anagrams(main_word, candidates):
    print()
    sorted_word = sorted(main_word.lower())
    expected = []
    for word in candidates:
        if word.lower() == main_word.lower(): continue
        if sorted(word.lower()) == sorted_word:
            expected.append(word)
    return expected
