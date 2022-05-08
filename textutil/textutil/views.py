from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests as rq


# def index(request): demo
#     # parms = {'name':'Vinayak','place':'Mars'}
#     # return render(request,'index.html',parms)
#     # return HttpResponse("<h1>Home</h1>")
#
#     # print(request.GET.get("text")) # for getting the element form html file
#     # djtext = request.GET.get("text","default")
#     # print(djtext)
#     return render(request,"index.html")

def analyze(request):
    djtext = request.GET.get("text", "default")
    djcheck = request.GET.get("removepunc", "off")
    print(djtext)
    print(djcheck)
    if djcheck == 'on':
        punctutaion = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyze = ""
        for char in djtext:
            if char not in punctutaion:
                analyze = analyze + char
        param = {"purpose":"Removed Punctuation","analyze":analyze}
        return render(request,'analyze.html',param)
    else:
        return HttpResponse("<h1>ERROR</h1>")
        # return HttpResponse('''<h1>removepunc</h1> <a href='/'>back</a> <h1>{{djtext}}</h1>''')


 # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
query_params = {
    "source": "bbc-news",
    # "source": "the-verge",
    # "source": "Brian Fung, CNN",
    "sortBy": "top",
    "apiKey": "6091d75cec1e433fab552430eedd65d6"
}
main_url = " https://newsapi.org/v1/articles"

# fetching data in json format
res = rq.get(main_url, params=query_params)
open_bbc_page = res.json()

# getting all articles in a string article
article = open_bbc_page["articles"]


def index(request):

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        # print(i + 1,results[i])
        index = i + 1
        news_iterate = results[i]
    news_list = list(results)
    # data = {'index':i+1,'news':news_list[1]}
    data = {'index':index,'news1':news_list[0],'news2':news_list[1],'news3':news_list[2],'news4':news_list[3],
            'news5':news_list[4],'news6':news_list[5],'news7':news_list[6],'news8':news_list[7],
            'news9':news_list[8],'news10':news_list[9]}

    return render(request, 'index.html', data)
    # to read the news out loud for us


def speak(request):
    img_url = []
    results = []
    desc = []

    for ar in article:
        img_url.append(ar["urlToImage"])
        results.append(ar["title"])
        desc.append(ar["description"])


    news_list = list(img_url)
    news_title = list(results)
    news_desc = list(desc)

    data = {'news1':news_list[0],'news2':news_list[1],'news3':news_list[2],'news4':news_list[3],
            'news5':news_list[4],'news6':news_list[5],'news7':news_list[6],'news8':news_list[7],
            'news9':news_list[8],'news10':news_list[9],
            'title1':news_title[0],'title2':news_title[1],'title3':news_title[2],'title4':news_title[3],
            'title5':news_title[4],'title6':news_title[5],'title7':news_title[6],'title8':news_title[7],
            'title9': news_title[8],'title10':news_title[9],
            'desc1':news_desc[0],'desc2':news_desc[1],'desc3':news_desc[2],'desc4':news_desc[3],'desc5':news_desc[4],
            'desc6': news_desc[5],'desc7':news_desc[6],'desc8':news_desc[7],'desc9':news_desc[8],'desc10':news_desc[9],
            }

    return render(request,"speak.html",data)


def speakme(request):
    results = []

    for ar in article:
        results.append(ar["title"])

    from win32com.client import Dispatch

    speak = Dispatch("SAPI.Spvoice")

    speak.Speak("news start now")
    speak.Speak(results)
    # return render(request, "speak.html")
    return redirect("speak")



# def capfirst(request):
#     return HttpResponse('''<h1>capfirst</h1><a href='/'>back</a>''')
#
# def newlineremove(request):
#     return HttpResponse('''<h1>newlineremove</h1><a href='/'>back</a>''')
#
# def spaceremove(request):
#     return HttpResponse('''<h1>spaceremove</h1><a href='/'>back</a>''')
#
# def charcount(request):
#     return HttpResponse('''<h1>charcount</h1><a href='/'>back</a>''')
