 print("Welcome to Airport Customer Support!")

while True:
    question = input("\nHow can I help you? ").lower()

    if "hello" in question or "hi" in question:
        print("Hello! Welcome to Airport Customer Support.")

    elif "check in" in question or "check-in" in question:
        print("Online check-in usually opens 24 hours before departure. Please check with your airline.")

    elif "baggage" in question or "luggage" in question:
        print("Baggage allowances depend on your airline and ticket.")

    elif "flight" in question:
        print("Please check your airline's website for the latest flight information.")

    elif "gate" in question:
        print("Please check the airport departure screens for your gate number.")

    elif "bye" in question or "exit" in question:
        print("Thank you for using Airport Customer Support!")
        break

    else:
        print("Sorry, I don't understand. Please contact airport customer service.")
