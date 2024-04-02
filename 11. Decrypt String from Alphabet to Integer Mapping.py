def freqAlphabets(s):
    mapping = {}
    for i in range(1, 27):
        if i <= 9:
            mapping[str(i)] = chr(96 + i)
        else:
            mapping[str(i) + "#"] = chr(96 + i)
    
    result = []
    i = 0
    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == '#':
            result.append(mapping[s[i:i+3]])
            i += 3
        else:
            result.append(mapping[s[i]])
            i += 1
    
    return ''.join(result)


