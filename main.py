import sys

from models import Contract, Project


class ContractManagementApp:
    def __init__(self):
        self.contracts = []
        self.projects = []
        self.menu_choices = {
            "1": self.create_contract,
            "2": self.confirm_contract,
            "3": self.complete_contract,
            "4": self.create_project,
            "5": self.add_contract_to_project,
            "6": self.print_contracts_and_projects,
            "7": self.exit_program
        }

    def create_contract(self):
        name = input("Введите название договора: ")
        contract = Contract(name)
        self.contracts.append(contract)
        print(f"Договор '{name}' создан.")

    def confirm_contract(self):
        print("\nСписок доступных договоров для подтверждения:")
        for i, contract in enumerate(self.contracts):
            if contract.status == "Черновик":
                print(f"{i + 1}. {contract.name}")

        choice = input("Выберите номер договора для подтверждения (или 0 для отмены): ")
        if choice == "0":
            return

        try:
            choice_index = int(choice) - 1
            selected_contract = self.contracts[choice_index]
            if selected_contract.status == "Черновик":
                selected_contract.confirm_contract()
                print(f"Договор '{selected_contract.name}' подтвержден.")
            else:
                print("Нельзя подтвердить этот договор.")
        except (ValueError, IndexError):
            print("Неправильный выбор. Попробуйте снова.")

    def complete_contract(self):
        print("\nСписок активных договоров для завершения:")
        for i, contract in enumerate(self.contracts):
            if contract.status == "Активен":
                print(f"{i + 1}. {contract.name}")

        choice = input("Выберите номер договора для завершения (или 0 для отмены): ")
        if choice == "0":
            return

        try:
            choice_index = int(choice) - 1
            selected_contract = self.contracts[choice_index]
            if selected_contract.status == "Активен":
                selected_contract.complete_contract()
                print(f"Договор '{selected_contract.name}' завершен.")
            else:
                print("Нельзя завершить этот договор.")
        except (ValueError, IndexError):
            print("Неправильный выбор. Попробуйте снова.")

    def create_project(self):
        name = input("Введите название проекта: ")
        project = Project(name)
        self.projects.append(project)
        print(f"Проект '{name}' создан.")

    def add_contract_to_project(self):
        print("\nСписок активных договоров:")
        for i, contract in enumerate(self.contracts):
            if contract.status == "Активен":
                print(f"{i + 1}. {contract.name}")

        contract_choice = input("Выберите номер договора для добавления к проекту (или 0 для отмены): ")
        if contract_choice == "0":
            return

        try:
            contract_index = int(contract_choice) - 1
            selected_contract = self.contracts[contract_index]
            if selected_contract.status != "Активен":
                print("Нельзя добавить этот договор к проекту.")
                return

            print("\nСписок проектов:")
            for i, project in enumerate(self.projects):
                print(f"{i + 1}. {project.name}")

            project_choice = input("Выберите номер проекта для добавления договора (или 0 для отмены): ")
            if project_choice == "0":
                return

            try:
                project_index = int(project_choice) - 1
                selected_project = self.projects[project_index]

                if selected_project.add_contract(selected_contract):
                    print(f"Договор '{selected_contract.name}' добавлен к проекту '{selected_project.name}'.")
                else:
                    print("Нельзя добавить договор к этому проекту.")
            except (ValueError, IndexError):
                print("Неправильный выбор проекта. Попробуйте снова.")
        except (ValueError, IndexError):
            print("Неправильный выбор договора. Попробуйте снова.")

    def main_menu(self):
        while True:
            print("\nГлавное меню:")
            print("1. Создать договор")
            print("2. Подтвердить договор")
            print("3. Завершить договор")
            print("4. Создать проект")
            print("5. Добавить договор к проекту")
            print("6. Вывести список договоров и проектов")
            print("7. Завершить работу")

            choice = input("Выберите действие: ")

            if choice in self.menu_choices:
                self.menu_choices[choice]()
            else:
                print("Неправильный выбор. Попробуйте снова.")

    def print_contracts_and_projects(self):
        print("\nДоговоры:")
        for contract in self.contracts:
            print(f"- {contract.name} ({contract.status})")
        print("\nПроекты:")
        for project in self.projects:
            print(f"- {project.name} ({len(project.contracts)} договоров)")

    def exit_program(self):
        print("Завершение работы программы.")
        sys.exit(0)


if __name__ == "__main__":
    app = ContractManagementApp()
    app.main_menu()
