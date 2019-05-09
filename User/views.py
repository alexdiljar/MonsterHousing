from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from User.forms.profile_form import ProfileForm
from User.models import Profile


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'User/SignUp.html', {
        'form': UserCreationForm()
    })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first() # gæti þurft að vera stórir stafir í user
    if request.method == "POST":
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'User/Account.html', {
        'form': ProfileForm(instance=profile)
    })
