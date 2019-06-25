import json
import re

mapping = {
    "INCOME": "Income Account",
    "EXPENSE": "Expense Account",
    "ASSET": "Asset",
    "LIABILITY": "Liability",
    "PAYABLE": "Payable",
    "RECEIVABLE": "Receivable",
    "EQUITY": "Equity",
    "ROOT": "ROOT",
    "CASH": "Cash",
    "BANK": "Bank"
}


class Account:
    def __init__(self, acc_json):
        self.is_group = acc_json["is_group"]
        self.account_type = mapping[acc_json["account_type"]]
        self.account_number = acc_json["account_number"]
        self.name = re.sub("^[0-9]{4} ", "", acc_json["name"])
        self.id = acc_json["id"]
        self.parent = acc_json["parent"]
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def as_json(self):
        acc = {}

        if self.is_group:
            acc["is_group"] = self.is_group

        if self.account_number:
            acc["account_number"] = self.account_number

        if self.account_type:
            acc["account_type"] = self.account_type

        for child in self.children:
            acc[child.name] = child.as_json()

        return acc


with open("gnucash_skr04_array.json", "r") as f:
    accounts_json = json.load(f)

accounts = [Account(acc_json) for acc_json in accounts_json]

for acc in accounts:
    if len(acc.name) > 135:
        print(acc.name, 'is too long')
    if acc.parent:
        parent = list(filter(lambda x: x.id == acc.parent, accounts))[0]
        parent.add_child(acc)

tree = accounts[0].as_json()

with open("skr_erpnext.json", "w") as f:
    print(json.dump(tree, f, indent=4))
