def rotate(text, key):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            cypher = ord(char) + key
            if cypher > ord('z'):
                cypher -= 26
            result += chr(cypher)
        elif 'A' <= char <= 'Z':
            cypher = ord(char) + key
            if cypher > ord('Z'):
                cypher -= 26
            result += chr(cypher)
        else:
            result += char
    return result