from decimal import Decimal

def simulate(dice: int, side: int):

    case_count = side**dice
    if case_count > 1000:
        return "Sorry, the simulation is run on server-side so I have limited the maximum number of results to 1000 in \
    order to prevent overloading. Please use a smaller combination of input."

    case_probability = Decimal('1')/case_count
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

        min_sum = dice
        max_sum = side*dice
        result = []

        for i in list(range(min_sum, max_sum+1)):
            p = round(list_case.count(i) * case_probability * 100, 6)
            result.append({'outcome': i, 'probability': p})

    return result