import json


class Transaction:
    def __init__(self, transaction_id, banker, summ, beneficiaries = [], reason='None', date=''):
        self.transaction_id = transaction_id
        self.banker = banker
        self.beneficiaries = beneficiaries
        self.reason = reason
        self.date = date
        self.summ = summ

    @classmethod
    def from_dict(cls, datadict):
        "Initialize Transaction from a dict's items"
        return cls(datadict.items())

    def dump(self, file_handler):
        "write dictionary of Transaction fields asa json to a file given by its handler"
        json.dump(self.__dict__, file_handler)

    def change_debts(self, debts):
        share = self.summ/(0.0 + len(self.beneficiaries))
        debts[self.banker] = debts.get(self.banker, 0) - self.summ #  negative debt means he's being owed
        for i in self.beneficiaries:
            debts[i] = debts.get(i, 0) + share




