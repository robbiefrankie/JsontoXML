import os

def execute_script(script_path):
    os.system(f"python {script_path}")

def main():
    choice = input("Is the input files are Batch Json ")

    if choice == "Y":
        execute_script("BatchJson.py")
    elif choice == "N":
        execute_script("IndiJson.py")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
