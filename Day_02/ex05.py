def check_string(str):
    return "Yes!" if str.startswith("The") else "NO"


if __name__ == "__main__":
    str1 = 'The'
    str2 = 'Thumbs up'
    str3 = 'Theatre can be boring'
    print(check_string(str1))
    print(check_string(str2))
    print(check_string(str3))
