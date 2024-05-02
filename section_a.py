#NUMBER 1 a)(i)
# As a python student, write a program using functions and conditions to display the grades that the students 
#will be receiving 
#the grades are;
#90% -100% Grade is A
#80% - 89% Grade is B
#70% - 79% Grade is C
#60% - 69%Grade is D
#50% - 59% Grade is E
#<50% Fail


#grading the marks 
def calculating_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    elif mark >= 50:
        return "E"
    else:
        return "FAIL"

def main():
    try:
        mark = float(input("Enter the student's mark: ")) 
        if mark < 0 or mark > 100:
            print("Invalid mark! Mark should be between 0 and 100.")
        else:
            grade = calculating_grade(mark)
            print(f"The student's grade is: {grade}")
    except ValueError:
        print("Invalid input! Please enter a numeric value for the mark.")

if __name__ == "__main__":
    main()


#number (ii)
#converting temperatures from celcius to Fahrenheight
def CelsiusToFahrenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():
    try:
        celsius = float(input("Enter temperature in Celsius: ")) #float type string()
        fahrenheit = CelsiusToFahrenheit(celsius)
        print("Temperature in Fahrenheit:", fahrenheit)
    except ValueError:
        print("Please enter a valid value for temperature.")

if __name__ == "__main__":
    main()

#number 1 b)(i)

#calculating the area of a triangle
#base = 2, height = 3
#formula = A = 1/2 X b x h

def calculate_rectangle_area(base, height):
    return 0.5 * base * height

def main():
    try:
        base = float(input("Enter the base of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))

        area = calculate_rectangle_area(base, height)

        print("The area of the rectangle is:", area)
    except ValueError:
        print("Please enter valid numeric values for base and height.")

if __name__ == "__main__":
    main()

#NUMBER 1 b)(ii)
#sample list : (9, 2, 3, 5, 8)

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

#sample list
numbers = [9, 2, 3, 5, 8]
output = sum_list(numbers)
print("The sum of the numbers in the list is:", output)