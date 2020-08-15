
from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'abc': 'abc123'})


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = dict()
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    count = len(wordlist)
    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': count, 'sortedwords': sortedwords})


def about(request):
    return render(request, 'about.html')
