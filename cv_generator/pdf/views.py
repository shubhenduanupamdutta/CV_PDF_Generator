from django.shortcuts import redirect, render

from .models import Profile


# Create your views here.


def accept_views(request):

    if request.method == "POST":
        fields = ['name', 'email', 'phone', 'summary', 'degree',
                  'school', 'university', 'previous_work', 'skills']
        data = {field: request.POST.get(field) for field in fields}

        profile = Profile(**data)
        profile.save()

        return redirect('accept')

    return render(request, "pdf/accept.html")


def resume(request, id):
    user_profile = Profile.objects.get(id=id)

    return render(request, "pdf/resume.html", {'user_profile': user_profile})
