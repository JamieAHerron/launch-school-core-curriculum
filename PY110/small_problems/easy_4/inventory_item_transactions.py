'''
P:
input: integer (ID), list (transactions)
output: list (specified transactions)

- take an integer (ID) as anargument and a list of transactions (dictionaries)
- return a list with only the transactions specified by the given ID


D:
- lists
- dictionaries

A:
- iterate over list of transactions
- check if id key value matches ID given as argument
- if match found, append transaction to result list
- return result list


'''

#Code:
def transactions_for(id, transaction_lst):
    result = []

    for transaction in transaction_lst:
        if transaction['id'] == id:
            result.append(transaction)
    
    return result

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True