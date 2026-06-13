# NayePankh-Foundation-Task
Task1- Python Code with Output 
successfully.")
        else:
            print("  ❌ Deletion cancelled.")

    input("\n  Press Enter to continue...")


# ─────────────────────────────────────────────
#  Main Program
# ─────────────────────────────────────────────

def main():
    while True:
        clear()
        print_banner()
        print_menu()

        choice = input("\n  Enter your choice (1-6): ").strip()

        if choice == "1":
            register_volunteer()
        elif choice == "2":
            view_all_volunteers()
        elif choice == "3":
            search_volunteer()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            delete_volunteer()
        elif choice == "6":
            clear()
            print_banner()
            print("\n  👋 Thank you for contributing to NayePankh Foundation!")
            print("  🌱 Together we give wings to dreams.\n")
            break
        else:
            print("\n  ⚠️  Invalid choice! Please enter 1-6.")
            input("  Press Enter to continue...")


if __name__ == "__main__":
    main()