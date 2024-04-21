from django.shortcuts import render


def index(request):
    name = "mr. Anderson"
    context = {
        'name': name
    }
    return render(request=request, template_name='cargo/index.html', context=context)
