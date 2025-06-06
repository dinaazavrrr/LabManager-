from lab_manager import add_lab, list_labs

def show_menu():
    print("\n1. Додати лабораторну")
    print("2. Показати всі")
    print("3. Показати здані")
    print("4. Показати не здані")
    print("5. Вийти")

def main():
    while True:
        show_menu()
        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Назва: ")
            number = input("Номер: ")
            grade = input("Оцінка: ")
            status = input("Статус (здано/не здано): ")
            add_lab(name, number, grade, status)
        elif choice == "2":
            labs = list_labs()
        elif choice == "3":
            labs = list_labs("здано")
        elif choice == "4":
            labs = list_labs("не здано")
        elif choice == "5":
            break
        else:
            print("Невірна опція")
            continue

        for lab in labs:
            print(f"Лаб. №{lab['number']}: {lab['name']} — {lab['grade']} ({lab['status']})")

if __name__ == "__main__":
    main()
