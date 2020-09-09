Cost = int(input("unit cost: "))
Price = int(input("unit price: "))
Demand = int(input("expected demand: "))

maxProfit = 0.0
optimalQ = 0
cumPr = 0.0
Rev = 0.0
addRev = 0.0

for Q in range(Demand + 1):
    TotalCost = Q * Cost
    Rev += addRev
    expProfit = Rev - TotalCost
    
    # print(Q, 1 - cumPr, Rev, TotalCost, expProfit)
    
    Pr = float(input("probability of each demand: "))
    cumPr += Pr
    addRev = (1 - cumPr) * Price

    
    if expProfit > maxProfit:
        maxProfit = expProfit
        optimalQ = Q
        
print(optimalQ, int(maxProfit))