from django.shortcuts import render, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Vocabulary
from django.db.models import Max


# Create your views here.

def main(request):
    max_day = Vocabulary.objects.all().aggregate(Max('day'))['day__max']
    return render(request, 'main.html', {'max_day': max_day})


@staff_member_required
def admin(request):
    dd_list = list(range(1, 41))
    return render(request, 'admin.html', {'dd_list': dd_list})


def show_test_paper(request):
    if request.method == "POST":
        first = int(request.POST.get("first"))
        last = int(request.POST.get('last'))
        word_list = Vocabulary.objects.filter(day__gte=first).filter(day__lte=last).order_by('?')
        return render(request, 'test_paper.html', {'word_list': word_list})
    else:
        return HttpResponseRedirect('/')


def create_voca(request):
    if request.method == "POST":
        day = request.POST.getlist('day')[0]
        word_list = request.POST.getlist('word')
        def_list = request.POST.getlist('def')

        word_list = [x for x in word_list if x != '']
        def_list = [x for x in def_list if x != '']

        if len(word_list) == len(def_list):
            for i in range(len(word_list)):
                Vocabulary.objects.create(day=day, word=word_list[i], definition=def_list[i])

        return HttpResponseRedirect('/admin')
    else:
        return HttpResponseRedirect('/')
