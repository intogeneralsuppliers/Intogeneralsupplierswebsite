from django.shortcuts import render, redirect
from .models import Service_Card
from .forms import MessageSubmissionForm

# Create your views here.
 

def home(request):
	return render(request, 'Into_General_Suppliers/home.html')

def about(request):
	return render(request, 'Into_General_Suppliers/about.html')

def services(request):
	context = {
		'cards': Service_Card.objects.all()
	}
	return render(request, 'Into_General_Suppliers/services.html', context)

def projects(request):
	return render(request, 'Into_General_Suppliers/projects.html')

def contact(request):
	form = MessageSubmissionForm()
	if request.method == 'POST':
		form = MessageSubmissionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('IGS-Home')
		else: 
			form = MessageSubmissionForm()
	return render(request, 'Into_General_Suppliers/contact.html', {'form': form})
