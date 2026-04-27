'''
Building on the previous exercise, write a function that returns True or False based on whether or not an inventory item (an ID number) is available. As before, the function takes two arguments: an item ID and a list of transactions. The function should return True only if the sum of the quantity values of the item's transactions is greater than zero. Notice that there is a movement property in each transaction object. A movement value of 'out' will decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.
'''

def transactions_for(item_id, transaction_lst):
    return [transaction for transaction in transaction_lst if transaction['id'] == item_id]

def is_item_available(item_id, transaction):
    sum_of_quantity = 0

    for transaction in transactions_for(item_id, transaction):
        if transaction['movement'] == 'in':
            sum_of_quantity += transaction['quantity']
        else:
            sum_of_quantity -= transaction['quantity']
    
    return sum_of_quantity > 0
    


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

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True