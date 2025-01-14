from django.shortcuts import render
from .models import User, Only_teacher, Request, Review  
from django.db.models import Avg

def teachers_page(request):
    teachers = Only_teacher.objects.select_related('teacher_id').all()
    data = []  
    for teacher in teachers:
        avg = teacher_rating(teacher.teacher_id_id) 
        free_places = places_left(teacher.teacher_id_id)  
        data.append({
            'teacher': teacher,
            'avg_rating': avg,
            'free_places': free_places,
        })
    context = {
        'data': data, 
    }
    return render(request, 'teachers_page.html', context)

def teacher_rating(teacher_id):
    rating = Review.objects.filter(teacher_id=teacher_id).values('rating')
    if rating:
        avg = rating.aggregate(Avg('rating'))
        return avg['rating__avg']
    return 0

def places_left(teacher_id):
    try:
        places = Only_teacher.objects.get(teacher_id=teacher_id).num_places_free  
        requests = Request.objects.filter(teacher_id=teacher_id, request_status='accepted').count()
        return places - requests
    except Only_teacher.DoesNotExist:
        return 0