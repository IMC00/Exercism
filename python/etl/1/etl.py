def transform(legacy_data: dict):
    result = {}
    for points, letters in legacy_data.items():
        for letter in letters:
            result[letter.lower()] = points
    return result
