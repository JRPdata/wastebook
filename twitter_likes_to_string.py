def convert_likes_to_string(likes):
    if likes >= 1000000:
        digits_int = math.floor(likes / 100000)
        digits_dec = math.floor((likes - (100000 * digits_int)) / 10000)
        s = str(digits_int)
        if digits_dec > 0:
            s += f".{digits_dec}"
        s += "M"
    elif likes >= 100000:
        digits_int = math.floor(likes / 1000)
        digits_dec = math.floor((likes - (1000 * digits_int)) / 100)
        s = str(digits_int)
        if digits_dec > 0:
            s += f".{digits_dec}"
        s += "k"
    elif likes >= 10000:
        digits_int = math.floor(likes / 1000)
        digits_dec = math.floor((likes - (1000 * digits_int)) / 100)
        s = str(digits_int)
        if digits_dec > 0:
            s += f".{digits_dec}"
        s += "k"
    else:
        s = str(likes)
    return s
