from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelform_factory
from .models import User, UserImage
from .forms import UserForm, ImageForm, UserFullForm

# Create your views here.
def add_face(request):
    ImageFormSet = modelform_factory(UserImage, form=ImageForm, extra=5)
    if request.method == 'POST':
        pass
    else:
        userForm = UserForm()
        formset = ImageFormSet()
        context = {'userForm': userForm, 'formset': formset}
        return render(request, 'face/index.html', context)


def addUser(request):
    if request.method == "POST":
        form = UserFullForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        print(files)
        if form.is_valid():
            name = form.cleaned_data['name']
            user = User.objects.create(name=name)
            for f in files:
                UserImage.objects.create(user=user, image=f)
            user.save()
            return render(request, 'face/success.html')

        else:
            print("Form invalid, see below error msg")
            print(form.errors)
            return render(request, 'face/error.html', {'error': form})

    else:
        form = UserFullForm()
        context = {'form': form}
        return render(request, 'face/index.html', context)


