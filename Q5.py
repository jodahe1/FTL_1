def compress_string(s: str) -> str:
    if not s:
        return s

    compressed = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(f"{current_char}{count}")
            current_char = char
            count = 1
    compressed.append(f"{current_char}{count}")

    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s


print(compress_string("aabcccccaaa"))
print(compress_string("abc"))
print(compress_string("a"))
