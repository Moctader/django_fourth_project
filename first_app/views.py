from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, './first_app/home.html', {"name" : "I am Rahim", "marks" : 86,"courses" : [
        {
        "id" : 1,
        "course" : "C",
        "teacher" : "Rahim"
        },
        {
        "id" : 2,
        "course" : "C++",
        "teacher" : "Kahim"
        },
        {
        "id" : 3,
        "course" : "Python",
        "teacher" : "Fahim"
        },
        ]})
    
def about(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        
        return render(request, './first_app/about.html', context={'name':name, 'email':email})
    else:
        return render(request, './first_app/about.html', context={'name':name, 'email':email})
    


def submit_form(request):
    return render(request, './first_app/form.html')