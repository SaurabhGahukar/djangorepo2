from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def movie_page_view(request):

    news1='Salman will marrage soon..!! '
    news2='Shushant murder mistry revealed....!!! '
    news3='South Indian superstar Prabhas gave one more hit '
    news4='Kangna slam BMC and Uddhav for her office illegal dimolished '
    return render(request,'testapp/mnews.html',{'news1':news1,'news2':news2,'news3':news3,'news4':news4})

def political_page_view(request):

    news1='CBI Raids Congress D.K.Shivkumar in allegedcorruption case '
    news2='Doctors slam Trums drive to greet supporters outside Walter Reed Hospital  '
    news3='US and China could slip into new Cold War that pushes countries to pick side '
    news4='Indian PM Nrendra Modi inaugurates newly completed ATAL TUNNEL '
    return render(request,'testapp/pnews.html',{'news1':news1,'news2':news2,'news3':news3,'news4':news4})