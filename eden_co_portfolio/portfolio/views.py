from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from .forms import ContactForm


def landing_view(request):
    return render(request, "landing.html", status=200)


def home_view(request):
    return render(request, "home.html", status=200)


def about_view(request):
    return render(request, "about.html", status=200)


def projects_view(request):
    return render(request, "projects.html", status=200)


def services_view(request):
    return render(request, "services.html", status=200)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                "contact.html",
                {"form": ContactForm(), "success": True},
                status=200,
            )
        return render(
            request,
            "contact.html",
            {"form": form, "success": False},
            status=400,
        )

    form = ContactForm()
    return render(request, "contact.html", {"form": form}, status=200)


# Error handlers keep HTTP responses consistent across the site.

def handler404(request, exception):
    return HttpResponseNotFound("Page not found.")


def handler500(request):
    return HttpResponseServerError("Server error. Please try again later.")
