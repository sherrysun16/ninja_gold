from django.shortcuts import render, HttpResponse, redirect
from time import strftime, gmtime
import random

# Create your views here.
def setting(request):

    request.session['count'] = request.POST['count1']
    request.session['gold_win'] = request.POST['gold']
    return redirect('/index')

def index(request):
    #del request.session['count']
    #del request.session['gold_win']
    if 'count' not in request.session:
        request.session['count'] = 10
    if 'gold_win' not in request.session:
        request.session['gold_win'] = 200
    if 'click' not in request.session:
        request.session['click'] = 0
    if 'comments' not in request.session:
        request.session['comments'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if int(request.session['click']) <= int(request.session['count']) and int(request.session['gold']) >= int(request.session['gold_win']):
        print(request.session['click'])
        print(request.session['gold'])
        return redirect('/win')
    return render(request, 'index.html')

def button1(request):
    print("HELLO")
    #logic goes here.  Or code
    randGold = random.randint(10, 20)
    time = strftime("%Y-%m-%d %H: %M %p",gmtime())
    #print(randGold)
    print(randGold)
    print(request.POST)
    request.session['gold'] += randGold
    request.session['click'] += 1
    request.session['comments'].append(f"Earned {randGold} golds from the Farm {time}")
    return redirect('/index')

def button2(request):
    print("HELLO")
    #logic goes here.  Or code
    randGold = random.randint(5, 10)
    time = strftime("%Y-%m-%d %H: %M %p",gmtime())
    print(randGold)
    request.session['gold'] += randGold
    request.session['comments'].append(f"Earned {randGold} golds from the Cave {time}")
    return redirect('/')

def button3(request):
    print("HELLO")
    #logic goes here.  Or code
    randGold = random.randint(2, 5)
    time = strftime("%Y-%m-%d %H: %M %p",gmtime())
    print(randGold)
    request.session['gold'] += randGold
    request.session['comments'].append(f"Earned {randGold} golds from the House {time}")
    return redirect('/')

def button4(request):
    print("HELLO")
    #logic goes here.  Or code
    randGold = random.randint(-50, 50)
    time = strftime("%Y-%m-%d %H: %M %p",gmtime())
    print(randGold)
    request.session['gold'] += randGold
    request.session['comments'].append(f"Earned {randGold} golds from the Casino {time}")
    #This function can add or subtract up to 50 gold
    return redirect('/')

def win(request):
    return render(request,'set.html')
