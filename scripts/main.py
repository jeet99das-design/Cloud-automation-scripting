import os
while True:
    print("\n=== CLOUD AUTOMATION TOOLKIT ===\n")
    print("1. Create EC2 Instance")
    print("2. List EC2 Instances")
    print("3. Toggle EC2 State")
    print("4. Exit")
    choice = input("\nEnter choice: ")
    if choice == "1":
        os.system("python3 scripts/create_ec2.py")
    elif choice == "2":
        os.system("python3 scripts/list_ec2.py")
    elif choice == "3":
        os.system("python3 scripts/toggle_ec2.py")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
