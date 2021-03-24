from django.shortcuts import render,HttpResponse


def index(request):
    return render(request, 'home.html')

#Form
def form(request):
    return render(request, 'form.html')









#captchaa
#def captcha(request):
    #return render(request, 'captcha.html')


                #  <ahref='/'>back</a>")

