from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings


def home(request):
	return render(request, 'index.html')	


def about(request):
	return render(request, 'about.html')


def gallery(request):
	return render(request, 'gallery.html')


def menu(request):
	return render(request, 'menu.html')


def reservation(request):
	return render(request, 'reservation.html')


def contact(request):
	return render(request, 'contact.html')


def contact_us(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']
		message = f"От: {name}\nEmail: {email}\n{message}"
		send_mail(
			"Сообщение вам",
			message,
			email,
            [settings.EMAIL_HOST_USER],
			)
	return redirect("/")