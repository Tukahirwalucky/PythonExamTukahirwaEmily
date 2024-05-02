
#number4 a
def calculating_bonus(salary, years_of_service):
    if years_of_service >= 4:
        bonus_percentage = 0.08
    elif years_of_service == 3:
        bonus_percentage = 0.05
    else:
        bonus_percentage = 0

    bonus_amount = salary * bonus_percentage
    return bonus_amount

while True:
    try:
        salary = float(input("Enter your salary: "))
        years_of_service = int(input("Enter your years of service: "))

        bonus = calculating_bonus(salary, years_of_service)

        print(f"Net bonus amount: ${bonus:.2f}")
    except ValueError:
        print("Please enter a valid salary and years of service.")
    
    choice = input("Do you want to calculate another bonus? (yes/no): ")
    if choice.lower() != 'yes':
        break
