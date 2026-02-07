from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import movie,reviews

def index(request):
    data=movie.objects.all()
    return render(request, 'index.html', {'data': data})

def result(request):
    data=movie.objects.all()
    return render(request, 'result.html', {'data': data})

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        movie.objects.create(
                name=name,
                desc=desc,
                img=img
            )
        return redirect('result')
    return render(request, 'form.html')

def delete(request,id):
    delete_item=movie.objects.get(id=id)
    delete_item.delete()
    return redirect('result')


def view_detail(request, id):
    view_item = movie.objects.get(id=id)
    w = reviews.objects.filter(movie_id=id).order_by('-id')
    prod = w.count()
    average = 0
    count = prod
    for r in w:
        average += r.rating
    avg = f'{average / count:.1f}' if count else "0.0"
    data = {
        'i': view_item,
        'w': w,
        'avg': avg,
        'prod': prod
    }
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        reviews.objects.create(
            rating=rating,
            comment=comment,
            movie_id=id
        )
        return redirect('detail', id=id)
    return render(request, 'detail.html', data)


def buy(request):
    return render(request,'buy.html')




from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})



