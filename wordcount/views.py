
from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def count(request):
    fulltext=request.GET['fulltext']

    wordslist = fulltext.split()

    countDict = {}

    for word in wordslist:
        if word in countDict:
            countDict[word] += 1
        else:
            countDict[word]=1

    sortedWords = sorted(countDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordslist), 'countDict':sortedWords})


def about(request):
    return render(request, 'about.html')