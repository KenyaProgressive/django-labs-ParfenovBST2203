def average_mark_count(marks: list[int]) -> float:
    return sum(marks) / len(marks)

def print_student_data(student_card: dict[str, str | list]) -> None:
    for key in student_card:
        print(f"{key}: {student_card[f"{key}"]}")
    print() 

def validate_average_mark(average_mark: float) -> bool:
    valid = (average_mark >= 2.0) and (average_mark <= 5.0)
    return True if valid else False 



def main() -> None:
    
    groupmates: list[dict] = [
        {
            "name": "Анастасия",
            "surname": "Пахомова",
            "exams": ["АиГ", "МИСПиСИТ", "АИС"],
            "marks": [5, 5, 3]
        },
        {
            "name": "Никита",
            "surname": "Парфенов",
            "exams": ["АиГ", "МИСПиСИТ", "АИС"],
            "marks": [5, 5, 5]
        },
        {
            "name": "Филипп",
            "surname": "Гилёв",
            "exams": ["АиГ", "МИСПиСИТ", "АИС"],
            "marks": [5, 5, 5]
        },
        {
            "name": "Светлана",
            "surname": "Озюменко",
            "exams": ["АиГ", "МИСПиСИТ", "АИС"],
            "marks": [5, 5, 4]
        }
    ]

    average_mark: float = float(input("Введите средний балл за экзамены: "))
    print()

    if not validate_average_mark(average_mark):
        print("Введите корректный средний балл!!! (2.0 <= x <= 5.0)")
        return

    for student_card in groupmates:
        if average_mark_count(student_card["marks"]) > average_mark:
            print_student_data(student_card)


if __name__ == "__main__":
    main()