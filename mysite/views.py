#This file is created by me in project

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):

    # get text from the uses in html
    djtext = request.POST.get('text', 'default')
    
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

   
    if(removepunc == 'on'):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations ', 'analyze_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
        

    if(newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char
            else:
                print("No")
        print("pre", analyzed)
        params = {'purpose':'New Line Removing', 'analyze_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    if(fullcaps=='on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Upper Case', 'analyze_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)



    if(extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Extra space Removing', 'analyze_text':analyzed}
        
        # return render(request, 'analyze.html', params)

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

    