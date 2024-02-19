def one_down(txt: str) -> str:
    res = ""
    for char in txt:
        res += chr(ord(char) - 1)
    return res


print(one_down("Ifmmp"))
