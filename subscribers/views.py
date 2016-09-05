from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm, SignUpForm


# Create your views here.
def home(request):
    title = 'Welcome to Strange Sweets'
    form = SignUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form
    }

    if form.is_valid():
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you"
		}

    return render(request, 'home.html', context)


def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'strangesweets301@gmail.com']
		contact_message = "%s: %s via %s"%(
				form_full_name,
				form_message,
				form_email)
		some_html_message = """
		<h1>Thank you!</h1>
		"""
		send_mail(subject,
				contact_message,
				from_email,
				to_email,
				html_message=some_html_message,
				fail_silently=True)

    context = {
		"form": form,
        "title": title,
        "title_align_center": title_align_center,
	}

    return render(request, "forms.html", context)
