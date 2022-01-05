def split_string(text):
    result = []
    for i in range(0, len(text), 2):
        if len(text[i:i+2]) < 2:
            result.append(text[i] + "_")
        else:
            result.append(text[i:i+2])
    return result


print(split_string("Ann"))
