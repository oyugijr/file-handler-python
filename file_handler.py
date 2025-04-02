def read_and_modify_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")

        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.readlines()

        # Modify content (e.g., convert to uppercase)
        modified_content = [line.upper() for line in content]

        # Write to a new file
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"Modified file saved as: {new_filename}")

    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file. Check permissions or file format.")

# Run the function
if __name__ == "__main__":
    read_and_modify_file()
