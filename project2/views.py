from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    dj = (request.POST.get('text', 'Default'))
    remove_punc = (request.POST.get('rem_punc', 'off'))
    upper_case = (request.POST.get('capital', 'off'))
    lower_case = (request.POST.get('small', 'off'))
    extra = (request.POST.get('rem_space', 'off'))
    rem_new_line = (request.POST.get('newline', 'off'))

    if remove_punc == 'on':
        ans = ''
        punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in dj:
            if char not in punc:
                ans = ans+char
        params = {'purpose': 'Selected Operations', 'analyzed_text': ans}
        dj = ans

    if extra == 'on':
        ans = ''
        for index, char in enumerate(dj):
            if not (dj[index] == " " and dj[index+1] == " "):
                ans = ans+char
        params = {'purpose': 'Selected Operations', 'analyzed_text': ans}
        dj = ans

    if upper_case == 'on':
        ans = ''
        for char in dj:
            ans = ans+char.upper()
        params = {'purpose': 'Selected Operations', 'analyzed_text': ans}
        dj = ans

    if lower_case == 'on':
        ans = ''
        for char in dj:
            ans = ans+char.lower()
        params = {'purpose': 'Selected Operations', 'analyzed_text': ans}
        dj = ans

    if rem_new_line == 'on':
        ans = ''
        for char in dj:
            if char != '\n' and char != '\r':
                ans = ans+char
            else:
                print("no")
        params = {'purpose': 'Selected Operations', 'analyzed_text': ans}
        dj = ans
        
    if rem_new_line != 'on' and lower_case != 'on' and upper_case != 'on' and extra != 'on' and remove_punc != 'on':
        return HttpResponse("ERROR!!!!!!!")
 
    return render(request, 'show.html', params)