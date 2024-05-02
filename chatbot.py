def hospital_chatbot():
    print("Welcome to the Hospital Service Chatbot!")
    while True:
        print("\nWhat do you need assistance with?")
        print("1. Schedule an appointment")
        print("2. Inquire about medical services")
        print("3. Talk to a doctor")
        print("4. Exit")
 
        choice = input("Enter your choice (1-4): ")
 
        if choice == '1':
            print("You have chosen to schedule an appointment.")
            # Logic for scheduling an appointment goes here
        elif choice == '2':
            print("You have chosen to inquire about medical services.")
            # Logic for inquiring about medical services goes here
        elif choice == '3':
            print("You have chosen to talk to a doctor.")
            # Logic for talking to a doctor goes here
        elif choice == '4':
            print("Thank you for using the Hospital Service Chatbot. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
