from datetime import datetime

class JournalManager:
    def __init__(self):
        self.file_name = "journal.txt"

    def add_entry(self):
        text = input("Write your journal entry:\n")
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            file = open(self.file_name, "a")
            file.write("[" + time_now + "]\n")
            file.write(text + "\n\n")
            file.close()
            print("Entry saved")
        except PermissionError:
            print("File permission error")

    def show_entries(self):
        try:
            file = open(self.file_name, "r")
            data = file.read()
            file.close()

            if data == "":
                print("Journal is empty")
            else:
                print("Your Entries")
                print("------------------------")
                print(data)

        except FileNotFoundError:
            print("No journal file found")

    def search_entry(self):
        key = input("Enter word or date to search: ")
        found = False

        try:
            file = open(self.file_name, "r")
            for line in file:
                if key.lower() in line.lower():
                    print(line.strip())
                    found = True
            file.close()

            if found == False:
                print("No matching entry found")

        except FileNotFoundError:
            print("Journal file not found")

    def delete_entries(self):
        ans = input("Delete all entries? yes/no: ")

        if ans == "yes":
            try:
                file = open(self.file_name, "w")
                file.close()
                print("Journal cleared")
            except PermissionError:
                print("File permission error")
        else:
            print("Delete cancelled")


def menu():
    jm = JournalManager()

    while True:
        print("\nPersonal Journal Manager")
        print("1 Add new entry")
        print("2 View all entries")
        print("3 Search entry")
        print("4 Delete all entries")
        print("5 Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            jm.add_entry()
        elif ch == "2":
            jm.show_entries()
        elif ch == "3":
            jm.search_entry()
        elif ch == "4":
            jm.delete_entries()
        elif ch == "5":
            print("Program closed")
            break
        else:
            print("Wrong choice")


menu()
