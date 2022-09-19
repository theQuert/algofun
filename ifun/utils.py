def find_max(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    print(max)