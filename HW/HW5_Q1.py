def best_product_info(item_cnt, minutes, prices):
    best_ratio = 0
    second_ratio = 0
    best = 0
    second = 0
    for i in range(item_cnt):
        ratio = prices[i] / minutes[i]
        if ratio > best_ratio:
            best_ratio = ratio
            best = i
    for i in range(item_cnt):
        if i != best:
            ratio = prices[i] / minutes[i]
            if ratio > second_ratio:
                second_ratio = ratio
                second = i
    return best + 1, second + 1