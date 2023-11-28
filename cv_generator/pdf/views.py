from django.shortcuts import redirect, render
import pdfkit
from django.http import HttpResponse
from django.template import loader
from .models import Profile
# import io

# pdfkit configuration
config = pdfkit.configuration(
    wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

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
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile})
    options = {
        "page-size": "Letter",
        "encoding": "UTF-8",
        "zoom": "1.5",
    }
    pdf = pdfkit.from_string(html, configuration=config, options=options)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    return response
