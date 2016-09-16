# from DataStruct import Transaction
import json


class Score:
    def __init__(self, list_of_names=list(), title='Expenses'):
        self.title = title
        self.participants = dict()
        self.debts = dict()
        i = 0
        for name in list_of_names:
            i += 1
            self.participants[i] = name
            self.debts[i] = 0.0
        self.transactions = list()
        # self.de

    def add_transaction(self, transaction):
        transaction.change_debts(self.debts)
        self.transactions.append(transaction)

    def recalculate_debts(self):
        self.debts = {i: 0.0 for i in self.participants.keys()}
        for transaction in self.transactions:
            transaction.change_debts(self.debts)

    def dump(self, file_handler):

        json.dump(self.participants, file_handler)
        for tr in self.transactions:
            tr.dump(file_handler)