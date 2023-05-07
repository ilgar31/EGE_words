from django.shortcuts import render
from .models import Words
import random


def index(request):
    return render(request, 'main/index.html')


def words(request):
    all_count = Words.objects.all().count()
    noun_count = Words.objects.filter(real_word="Имена существительные").count()
    adjective_count = Words.objects.filter(real_word="Имена прилагательные").count()
    verbs_count = Words.objects.filter(real_word="Глаголы").count()
    communion_count = Words.objects.filter(real_word="Причастия и отглагол. прил.").count()
    adverbs_count = Words.objects.filter(real_word="Наречия").count()
    gerunds_count = Words.objects.filter(real_word="Деепричастия").count()
    data = {"all": all_count, "noun": noun_count, "adjective": adjective_count,
            "verbs": verbs_count, "communion": communion_count,
            "adverbs": adverbs_count, "gerunds": gerunds_count}
    return render(request, "main/words.html", data)


all = 0
all_enumerate_words = Words.objects.order_by("?")
for i in all_enumerate_words:
    i.word = list(enumerate(str(i.word).upper()))


def all_words(request):
    global all
    flag = None
    words = all_enumerate_words[all]
    if request.method == 'GET' and request.GET.get("index"):
        if str(request.GET.get("index")) == str(words.ind_udar):
            all += 1
            flag = 1
            if all == len(Words.objects.all()):
                all = 0
            words = all_enumerate_words[all]
            return render(request, 'main/words/all_words.html', {'words': words, "flag": flag})
        flag = 0
    return render(request, 'main/words/all_words.html', {'words': words, "flag": flag})


noun = 0
noun_enumerate_words = Words.objects.filter(real_word="Имена существительные").order_by("?")
for i in noun_enumerate_words:
    i.word = list(enumerate(str(i.word).upper()))


def noun_words(request):
    global noun
    flag = None
    words = noun_enumerate_words[noun]
    if request.method == 'GET' and request.GET.get("index"):
        if str(request.GET.get("index")) == str(words.ind_udar):
            noun += 1
            flag = 1
            if noun == len(Words.objects.filter(real_word="Имена существительные")):
                noun = 0
            words = noun_enumerate_words[noun]
            return render(request, 'main/words/noun_words.html', {'words': words, "flag": flag})
        flag = 0
    return render(request, 'main/words/noun_words.html', {'words': words, "flag": flag})


adjective = 0
adjective_enumerate_words = Words.objects.filter(real_word="Имена прилагательные").order_by("?")
for i in adjective_enumerate_words:
    i.word = list(enumerate(str(i.word).upper()))


def adjective_words(request):
    global adjective
    flag = None
    words = adjective_enumerate_words[adjective]
    if request.method == 'GET' and request.GET.get("index"):
        if str(request.GET.get("index")) == str(words.ind_udar):
            adjective += 1
            flag = 1
            if adjective == len(Words.objects.filter(real_word="Имена прилагательные")):
                adjective = 0
            words = adjective_enumerate_words[adjective]
            return render(request, 'main/words/adjective_words.html', {'words': words, "flag": flag})
        flag = 0
    return render(request, 'main/words/adjective_words.html', {'words': words, "flag": flag})


verbs = 0
verbs_enumerate_words = Words.objects.filter(real_word="Глаголы").order_by("?")
for i in verbs_enumerate_words:
    i.word = list(enumerate(str(i.word).upper()))


def verbs_words(request):
    global verbs
    flag = None
    words = verbs_enumerate_words[verbs]
    if request.method == 'GET' and request.GET.get("index"):
        if str(request.GET.get("index")) == str(words.ind_udar):
            verbs += 1
            flag = 1
            if verbs == len(Words.objects.filter(real_word="Глаголы")):
                verbs = 0
            words = verbs_enumerate_words[verbs]
            return render(request, 'main/words/verbs_words.html', {'words': words, "flag": flag})
        flag = 0
    return render(request, 'main/words/verbs_words.html', {'words': words, "flag": flag})


communion = 0
communion_enumerate_words = Words.objects.filter(real_word="Причастия и отглагол. прил.").order_by("?")
for i in communion_enumerate_words:
    i.word = list(enumerate(str(i.word).upper()))


def communion_words(request):
    global communion
    flag = None
    words = communion_enumerate_words[communion]
    if request.method == 'GET' and request.GET.get("index"):
        if str(request.GET.get("index")) == str(words.ind_udar):
            communion += 1
            flag = 1
            if communion == len(Words.objects.filter(real_word="Причастия и отглагол. прил.")):
                communion = 0
            words = communion_enumerate_words[communion]
            return render(request, 'main/words/communion_words.html', {'words': words, "flag": flag})
        flag = 0
    return render(request, 'main/words/communion_words.html', {'words': words, "flag": flag})


adverbs = 0
adverbs_enumerate_words = Words.objects.filter(real_word="Наречия").order_by("?")
for i in adverbs_enumerate_words:
    i.word = list(enumerate(str(i.word).upper()))


def adverbs_words(request):
    global adverbs
    flag = None
    words = adverbs_enumerate_words[adverbs]
    if request.method == 'GET' and request.GET.get("index"):
        if str(request.GET.get("index")) == str(words.ind_udar):
            adverbs += 1
            flag = 1
            if adverbs == len(Words.objects.filter(real_word="Наречия")):
                adverbs = 0
            words = adverbs_enumerate_words[adverbs]
            return render(request, 'main/words/adverbs_words.html', {'words': words, "flag": flag})
        flag = 0
    return render(request, 'main/words/adverbs_words.html', {'words': words, "flag": flag})


gerunds = 0
gerunds_enumerate_words = Words.objects.filter(real_word="Деепричастия").order_by("?")
for i in gerunds_enumerate_words:
    i.word = list(enumerate(str(i.word).upper()))


def gerunds_words(request):
    global gerunds
    flag = None
    words = gerunds_enumerate_words[gerunds]
    if request.method == 'GET' and request.GET.get("index"):
        if str(request.GET.get("index")) == str(words.ind_udar):
            gerunds += 1
            flag = 1
            if gerunds == len(Words.objects.filter(real_word="Деепричастия")):
                gerunds = 0
            words = gerunds_enumerate_words[gerunds]
            return render(request, 'main/words/gerunds_words.html', {'words': words, "flag": flag})
        flag = 0
    return render(request, 'main/words/gerunds_words.html', {'words': words, "flag": flag})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')

