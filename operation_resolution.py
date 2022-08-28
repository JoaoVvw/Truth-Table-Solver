from combinations_using_binarie import combinations_setter

op = "~a ^ ~b"
letters = []
combinations_dictionary = {"T": True, "F": False}
order_of_results = []
quantity_of_true = 0
quantity_of_false = 0


def operation_preparer(operation):
    operation_list = []

    for char in operation:
        if char != " ":
            operation_list.append(char)

    for idx, i in enumerate(operation_list):
        if i == "-":
            operation_list.pop(idx + 1)
            operation_list[idx] = "imp"
        elif i == "<":
            operation_list.pop(idx + 1)
            operation_list.pop(idx + 1)
            operation_list[idx] = "bic"

    for i in operation_list:
        if i.isalpha() and len(i) == 1 and i not in letters and i != "V":
            letters.append(i)
    return operation_list


operation_list_imported = operation_preparer(op)
combinations = combinations_setter(len(letters))
recursion = 0


def operation_resolution(operation_list):
    global recursion
    global quantity_of_true
    global quantity_of_false
    temp_operation = operation_list.copy()
    while len(temp_operation) > 1:
        if "(" in temp_operation:
            recursion += 1
            open_parentheses = False
            close_parentheses = False
            for list_idx, i in enumerate(temp_operation):
                if i == "(" and not close_parentheses:
                    open_parentheses = list_idx
                if i == ")" and not close_parentheses:
                    close_parentheses = list_idx
            inside_temp_operation = []
            for inside_list_idx, inside_i in enumerate(temp_operation):
                if open_parentheses < inside_list_idx < close_parentheses:
                    inside_temp_operation.append(inside_i)
            parentheses_result = operation_resolution(inside_temp_operation)[0]
            temp_operation.insert(open_parentheses, parentheses_result)
            for i in range(close_parentheses - open_parentheses + 1):
                temp_operation.pop(open_parentheses + 1)

        def and_operator():
            if "^" in temp_operation:
                for list_idx, i in enumerate(temp_operation):
                    if i == "^":
                        quantity_of_not = 0
                        first_negation = False
                        first_condition = combinations_dictionary[temp_operation[list_idx - 1]]
                        if temp_operation[list_idx + 1] != "~":
                            second_condition = combinations_dictionary[temp_operation[list_idx + 1]]
                        else:
                            second_condition = combinations_dictionary[temp_operation[list_idx + 2]]
                        if temp_operation[list_idx - 2] == "~":
                            quantity_of_not += 1
                            first_negation = True
                            first_condition = not first_condition
                        if temp_operation[list_idx + 1] == "~":
                            quantity_of_not += 1
                            second_condition = not second_condition
                        if first_condition and second_condition:
                            temp_operation.insert(list_idx - 1, "T")
                        else:
                            temp_operation.insert(list_idx - 1, "F")
                        for i in range(3 + quantity_of_not):
                            if first_negation:
                                print(f"poping {temp_operation(list_idx - 1)}")
                                temp_operation.pop(list_idx - 1)
                            else:
                                print(f"poping {temp_operation(list_idx)}")
                                temp_operation.pop(list_idx)

        def or_operator():
            if "V" in temp_operation:
                for list_idx, i in enumerate(temp_operation):
                    if i == "V":
                        if combinations_dictionary[temp_operation[list_idx - 1]] or combinations_dictionary[temp_operation[list_idx + 1]]:
                            temp_operation.insert(list_idx - 1, "T")
                        else:
                            temp_operation.insert(list_idx - 1, "F")
                        for i in range(3):
                            temp_operation.pop(list_idx)

        def imp_operator():
            if "imp" in temp_operation:
                for list_idx, i in enumerate(temp_operation):
                    if i == "imp":
                        if not combinations_dictionary[temp_operation[list_idx - 1]] or combinations_dictionary[temp_operation[list_idx + 1]]:
                            temp_operation.insert(list_idx - 1, "T")
                        else:
                            temp_operation.insert(list_idx - 1, "F")
                        for i in range(3):
                            temp_operation.pop(list_idx)

        def bic_operator():
            if "bic" in temp_operation:
                for list_idx, i in enumerate(temp_operation):
                    if i == "bic":
                        if combinations_dictionary[temp_operation[list_idx - 1]] == combinations_dictionary[temp_operation[list_idx + 1]]:
                            temp_operation.insert(list_idx - 1, "T")
                        else:
                            temp_operation.insert(list_idx - 1, "F")
                        for i in range(3):
                            temp_operation.pop(list_idx)

        if "(" not in temp_operation:
            and_operator()
        if "^" not in temp_operation:
            or_operator()
        if "V" not in temp_operation:
            imp_operator()
        if "imp" not in temp_operation:
            bic_operator()
    if recursion == 0:
        order_of_results.append(temp_operation[0])
        if temp_operation[0] == "T":
            quantity_of_true += 1
        elif temp_operation[0] == "F":
            quantity_of_false += 1
    else:
        recursion -= 1
    return temp_operation


for letter in letters:
    combinations_dictionary[letter] = ""

for conditions_combinations in combinations:
    for idx, conditions in enumerate(conditions_combinations):
        if conditions == "T":
            combinations_dictionary |= {letters[idx]: True}
        else:
            combinations_dictionary |= {letters[idx]: False}
    operation_resolution(operation_list_imported)


def print_result():
    if quantity_of_true == 0:
        result = "Contradição"
    elif quantity_of_false == 0:
        result = "Tautologia"
    else:
        result = "Contingência"
    print()
    print(f"A equação resolvida foi: {op}")
    print(f"O resultado da operação foi: {result}")
    print(f"A quantidade de resultados verdadeiros foi: {quantity_of_true}")
    print(f"A quantidade de resultados falsos foi: {quantity_of_false}")
    print(f"A ordem de resultados foi: ", end="")
    for idx, results in enumerate(order_of_results):
        if idx != len(order_of_results) - 1:
            print(f"{results}, ", end="")
        else:
            print(results)


print_result()
