def combinations_setter(quantity_of_letters):
    combinations_number = 2 ** quantity_of_letters
    binaries = []
    formatted_binaries = []
    ready_binaries = []
    combinations = []
    for i in range(combinations_number):
        binaries.append(str(bin(i)))
    for i in binaries:
        formatted_binaries.append(i.replace("0b", ""))
    for i in formatted_binaries:
        full_size = len(formatted_binaries[-1])
        size = len(i)
        size = full_size - size
        rest = ""
        for sizes in range(size):
            rest += "0"
        i = rest + i
        ready_binaries.append(i)
    for bins in ready_binaries:
        temporary_combination = ""
        for numbers in bins:
            if numbers == "0":
                temporary_combination += "T"
            elif numbers == "1":
                temporary_combination += "F"
        combinations.append(temporary_combination)
    return combinations