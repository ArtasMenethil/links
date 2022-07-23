from django.shortcuts import render
from .models import UsersLink
from .forms import LinkFromUser


def home(request):
    return render(request, 'link_add/home.html')


def who_are_we(request):
    return render(request, 'link_add/who_we.html')


def create_and_list(request):
    form = LinkFromUser(request.POST)
    if form.is_valid():
        objects = form.save(commit=False)
        objects.user = request.user
        objects.save()

    obj = UsersLink.objects.filter(user=request.user).all()
    return render(request, 'link_add/user_links.html', {'links_users': obj, 'form': form})

