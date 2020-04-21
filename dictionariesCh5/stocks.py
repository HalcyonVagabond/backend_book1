stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

purchaseList = list(purchases)

purchaseTotals = dict()

for purchase in purchaseList:
    print(f"I purchased {stockDict[purchase[0]]} stock for ${purchase[1] * purchase[3]}")
    
    print(purchase[0])
    if purchaseTotals[purchase[0]] in purchaseTotals:
        purchaseTotals[purchase[0]] += (purchase[1] * purchase[3])
    else:
        purchaseTotals[purchase[0]] = (purchase[1] * purchase[3])



print(purchaseTotals)