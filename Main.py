from DataStruct import Transaction

tr = Transaction(transaction_id=1, banker=13, summ=12, beneficiaries=[1, 4], reason='food', )
with open('output.txt', 'w') as fh:
    tr.dump(fh)

debt = dict()
tr.change_debts(debt)
print(debt)

