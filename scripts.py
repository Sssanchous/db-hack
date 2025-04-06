def create_commendation(schoolkid_name, subject_title):
    from datacenter.models import Schoolkid, Lesson, Commendation
    import random

    text = random.choice(["Молодец!", "Отлично!"])
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid_name}'")
        return
    except Schoolkid.DoesNotExist:
        print(f"Ученик с именем '{schoolkid_name}' не найден")
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
    from datacenter.models import Schoolkid, Chastisement
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
    from datacenter.models import Mark
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in bad_marks:
        mark.points = 5
        mark.save()
