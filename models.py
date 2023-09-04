from datetime import datetime


class Contract:
    def __init__(self, name, project=None):
        self.name = name
        self.creation_date = datetime.now()
        self.signing_date = None
        self.status = "Черновик"
        self.project = project

    def confirm_contract(self):
        if self.status == "Черновик":
            self.status = "Активен"
            self.signing_date = datetime.now()
            if self.project:
                self.project.add_contract(self)

    def complete_contract(self):
        if self.status == "Активен":
            self.status = "Завершен"
            if self.project:
                self.project.remove_contract(self)

class Project:
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.contracts = []

    def add_contract(self, contract):
        if contract.status == "Активен" and contract not in self.contracts:
            self.contracts.append(contract)
            contract.project = self

    def remove_contract(self, contract):
        if contract in self.contracts:
            self.contracts.remove(contract)
            contract.project = None
