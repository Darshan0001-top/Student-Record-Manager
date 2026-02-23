def student_record_manager():
    students = []

    while True:
        print("\n--- Student Record Manager ---")
        print("1. Add Student")
        print("2. View All Records")
        print("3. Search by Roll Number")
        print("4. Calculate Average Marks")
        print("5. Find Topper")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ")

        if choice == '1':
            name = input("Enter Name: ")
            roll = input("Enter Roll Number: ")
            try:
                marks = float(input("Enter Marks: "))
                students.append({"name": name, "roll": roll, "marks": marks})
                print(f"Record for {name} added successfully!")
            except ValueError:
                print("Invalid input. Marks must be a number.")

        elif choice == '2':
            print("\n--- All Records ---")
            for s in students:
                print(f"Roll: {s['roll']} | Name: {s['name']} | Marks: {s['marks']}")

        elif choice == '3':
            search_roll = input("Enter Roll Number to search: ")
            found = next((s for s in students if s['roll'] == search_roll), None)
            if found:
                print(f"Found: {found['name']} - Marks: {found['marks']}")
            else:
                print("Student not found.")

        elif choice == '4':
            if students:
                avg = sum(s['marks'] for s in students) / len(students)
                print(f"Average Marks: {avg:.2f}")
            else:
                print("No records found.")

        elif choice == '5':
            if students:
                topper = max(students, key=lambda x: x['marks'])
                print(f"Topper: {topper['name']} with {topper['marks']} marks!")
            else:
                print("No records found.")

        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
student_record_manager()