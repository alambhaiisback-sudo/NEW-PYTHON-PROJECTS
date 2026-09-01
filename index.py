def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def main():
    print("===== Student Grade Calculator =====")

    name = input("Enter student name: ")

    marks = []

    for i in range(1, 6):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / len(marks)
    grade = calculate_grade(percentage)

    print("\n===== Result =====")
    print(f"Student Name : {name}")
    print(f"Total Marks  : {total}/500")
    print(f"Percentage   : {percentage:.2f}%")
    print(f"Grade        : {grade}")


if __name__ == "__main__":
    main()