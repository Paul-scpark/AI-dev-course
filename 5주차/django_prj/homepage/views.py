from django.shortcuts import HttpResponse, render
from .models import Coffee
from .forms import CoffeeForm

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello, world!</h1>")
    number = 10
    name = 'Paul'
    lst = [1, 2, 3, 4, 5]
    return render(request, 'index.html', {
        'my_num': number,
        'my_name': name, 
        'my_list': lst
    })
    
def coffee_view(request):
    coffee_all = Coffee.objects.all() # .get(), .filter()
    
    # 만약 request가 POST:
        # POST를 바탕으로 Form을 완성
        # Form이 유효하면, 저장하기
    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = CoffeeForm()
    return render(request, 'coffee.html', {
        "coffee_list": coffee_all, 
        "coffee_form": form
    })