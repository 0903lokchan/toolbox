def simulation(dice, side, target_sum='all'):
    case_probability = 1 / (side**dice)
    list_case = []
    target_case = []
    temp_a = [[]]
    temp_b =[]
    
    for x in list(range(dice)):
        for i in temp_a:
            for s in [ x + 1 for x in range(side)]:
                item = i.copy()
                item.append(s)
                temp_b.append(item)
        temp_a = temp_b.copy()
        temp_b = []
    list_case = temp_a.copy()

    for i, case in enumerate(list_case):
        list_case[i] = sum(case)

    if type(target_sum) is int:
        possibility = case_probability * list_case.count(int(target_sum))
        return print(f'{dice} {side}-sided dice, possibility to obtain {target_sum}: {possibility*100}%')
    elif target_sum == 'all':
        min_sum = dice
        max_sum = side*dice
        result = {}

        for i in list(range(min_sum, max_sum+1)):
            p = list_case.count(i)*case_probability
            result[i] = p
        return result