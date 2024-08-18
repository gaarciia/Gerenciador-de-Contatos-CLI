import json
import os
import csv

class ContactManager:
    def __init__(self, filename='contacts.json', csv_filename='contacts.csv'):
        self.filename = filename
        self.csv_filename = csv_filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        self.save_contacts()

    def list_contacts(self):
        if not self.contacts:
            print("Nenhum contato encontrado.")
        else:
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Contato '{name}' removido.")
        else:
            print(f"Contato '{name}' não encontrado.")

    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(f"{name}: {contact}")
        else:
            print(f"Contato '{name}' não encontrado.")

    def edit_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            self.save_contacts()
            print(f"Contato '{name}' atualizado.")
        else:
            print(f"Contato '{name}' não encontrado.")

    def export_to_csv(self):
        with open(self.csv_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone'])
            for name, phone in self.contacts.items():
                writer.writerow([name, phone])
        print(f"Contatos exportados para {self.csv_filename}.")

def show_menu():
    print("\nGerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Remover Contato")
    print("4. Buscar Contato")
    print("5. Editar Contato")
    print("6. Exportar para CSV")
    print("7. Sair")

def main():
    contact_manager = ContactManager()

    while True:
        show_menu()
        option = input("Escolha uma opção: ")

        if option == '1':
            name = input("Nome do contato: ")
            phone = input("Telefone do contato: ")
            contact_manager.add_contact(name, phone)
            print(f"Contato '{name}' adicionado.")
        elif option == '2':
            contact_manager.list_contacts()
        elif option == '3':
            name = input("Nome do contato a ser removido: ")
            contact_manager.remove_contact(name)
        elif option == '4':
            name = input("Nome do contato a ser buscado: ")
            contact_manager.search_contact(name)
        elif option == '5':
            name = input("Nome do contato a ser editado: ")
            new_phone = input("Novo telefone do contato: ")
            contact_manager.edit_contact(name, new_phone)
        elif option == '6':
            contact_manager.export_to_csv()
        elif option == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
