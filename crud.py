from random import choice

from datacenter.models import (
    Schoolkid,
    Mark,
    Lesson,
    Chastisement,
    Commendation
)


TEXT_COMMENDATIONS = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Ты, как всегда, точен!"
    ]


def fix_marks(schoolkid_name):
    child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    child_marks = Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    child_marks.update(points=5)


def remove_chastisements(schoolkid_name):
    child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    child_chastisements = Chastisement.objects.filter(schoolkid=child)
    child_chastisements.delete()


def create_commendation(schoolkid_name, subject_title):
    child = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    lesson = Lesson.objects.filter(
        year_of_study=child.year_of_study,
        group_letter=child.group_letter,
        subject__title=subject_title
    ).order_by("date").first()
    Commendation.objects.create(
        text=choice(TEXT_COMMENDATIONS),
        teacher=lesson.teacher,
        subject=lesson.subject,
        created=lesson.date,
        schoolkid=child
    )
