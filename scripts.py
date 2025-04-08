from datacenter.models import Schoolkid, Lesson, Commendation, Chastisement, Mark
import random

COMPLIMENTS = ["Молодец!", "Отлично!"]


def get_student(schoolkid_name):
    try:
        student = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return student
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем {schoolkid_name}")
        return None
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем '{schoolkid_name}' не найден.")
        return None


def create_commendation(schoolkid_name, subject_title):
    text = random.choice(COMPLIMENTS)
    schoolkid = get_student(schoolkid_name)

    if not schoolkid:
        return

    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_title
    ).order_by('date').first()

    if not lesson:
        print("Урок не найден")
        return

    if not Commendation.objects.filter(
        schoolkid=schoolkid,
        subject=lesson.subject,
        created=lesson.date
    ).exists():
        Commendation.objects.create(
            text=text,
            created=lesson.date,
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )


def remove_chastisements(schoolkid_name):
    try:
        student = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем {schoolkid_name}")
        return
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем '{schoolkid_name}' не найден.")
        return

    Chastisement.objects.filter(schoolkid=student).delete()


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


def main():
    student_name = "Фролов Иван"
    subject_for_commendation = "Музыка"

    student = get_student(student_name)
    if student:
        fix_marks(student)

    remove_chastisements(student_name)

    create_commendation(student_name, subject_for_commendation)


if __name__ == '__main__':
    main()