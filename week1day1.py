print("👋 Hello! Welcome to Bayview Hospital!")

while True:
    name = input("📝 What is the patient's name?: ")
    age = input("🎂 How old is this patient?: ")
    nationality = input("🌍 Where is the patient from?: ")

    print(f"\n📋 Patient Summary:")
    print(f"👤 Name: {name}")
    print(f"🎂 Age: {age}")
    print(f"🌍 Nationality: {nationality}")

    is_this_correct = input("\n✅ Is all this correct? (yes/no): ").lower()

    if is_this_correct == 'yes':
        print("✅ Info saved. Thank you!")
        break
    else:
        print("\n🔁 Let's try again.\n")
