from decimal import Decimal

def simulate(dice, side):

    case_count = side**dice
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
            p = Decimal(list_case.count(i) * case_probability)
            result.append({'result': i, 'possibility': p})

    output = ""
    for item in result:
        output += f"Result: {item['result']}    Possibility: {item['possibility']*100}%<br>"
    return output