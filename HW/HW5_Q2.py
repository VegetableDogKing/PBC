# i, j, budget: integers
# price_happiness: integer
# price_heart: integer
# return true if B is enough to purchase i sets of "Happiness Bouquets" and j sets of "True Heart Bouquets"
# return false otherwise
def within_budget(i, j, price_happiness, price_heart, budget):
    is_within_budget = True
    if price_happiness * i + price_heart * j > budget:

        is_within_budget = False
    return is_within_budget

# i, j, budget: integers
# happy_flower: a list of three integers (red, white, and then yellow) 
# heart_flower: a list of three integers (red, white, and then yellow)
# price_happiness: integer
# price_heart: integer
# budget: integer
# requirement: a list of three integers (K_1, K_2, K_3)
# return the price needed to buy i sets of "Happiness Bouquets" and j sets of "True Heart Bouquets" if such a purchase plan meets at least one requirement
# return the budget value + 1 otherwise 
def meet_one_req(i, j, happy_flower, heart_flower, price_happiness, price_heart, budget, requirement):
  # do some calculation here ...
    total_price = i * price_happiness + j * price_heart
    req1 = i * happy_flower[0] + j * heart_flower[0]
    req2 = i * (happy_flower[1] + happy_flower[2]) + j * (heart_flower[1] + heart_flower[2])
    req3 = req1 * 3 + i * happy_flower[1] + j * heart_flower[1]
    if total_price <= budget and (req1 >= requirement[0] or req2 >= requirement[1] or req3 >= requirement[2]):
        return total_price
    else:
        return budget + 1