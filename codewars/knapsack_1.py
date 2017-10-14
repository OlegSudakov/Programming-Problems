# https://www.codewars.com/kata/53ffbba24e9e1408ee0008fd

def knapsack(capacity, items):
    ratios = [item[1]/item[0] for item in items]
    result = [0]*len(items)
    while capacity >= min(size for (size, value) in items):
        print("Ratios: ",ratios)
        max_ratio = max(ratios)
        max_index = ratios.index(max_ratio)
        num_items = capacity // items[max_index][0]
        capacity -= num_items*items[max_index][0]
        print("Capacity: ", capacity)
        result[max_index] = num_items
        print("Result: ",result)
        ratios[max_index] = 0
    # Be greedy!
    return result
