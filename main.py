from action import pdf_generator, get_table_of_content_prompt

Banner = '''
_____                ____  ____  _____
| ____|__ _ ___ _   _|  _ \|  _ \|  ___|
|  _| / _` / __| | | | |_) | | | | |_ 
| |__| (_| \__ | |_| |  __/| |_| |  _|
|_____\__,_|___/\__, |_|   |____/|_|
                |___/

PDF Generator with GPT-3.5 and Unsplash Image Integration
'''


def display_banner():
    print(Banner)


def main():
    display_banner()
    print("Welcome to PDF Generator!")
    while True:
        print("\n1. Generate PDF")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            topic = input("\nEnter the topic: ")
            try:
                pdf_generator(topic)
                print("PDF generated successfully!")
            except Exception as e:
                print(f"An error occurred: {e}")
                print("trying again.")
                pdf_generator(topic)
        elif choice == "2":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
