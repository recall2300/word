from django.shortcuts import render, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Vocabulary
from django.db.models import Max


# Create your views here.

def main(request):
    max_day = Vocabulary.objects.all().aggregate(Max('day'))['day__max']
    day_range = list(range(1, max_day + 1))
    return render(request, 'main.html', {'max_day': max_day, 'day_range': day_range})


@staff_member_required
def admin(request):
    dd_list = list(range(1, 41))
    return render(request, 'admin.html', {'dd_list': dd_list})


def show_test_paper(request):
    if request.method == "POST":
        first = int(request.POST.get("first"))
        last = int(request.POST.get('last'))
        word_count = int(request.POST.get('word_count'))
        word_list = Vocabulary.objects.filter(day__gte=first).filter(day__lte=last).order_by('?')[:word_count]
        list_length = len(word_list)
        word_list1 = word_list[:int(list_length / 2)]
        word_list2 = word_list[int(list_length / 2):]
        return render(request, 'test_paper.html', {'word_list1': word_list1, 'word_list2': word_list2})
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
