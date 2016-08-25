from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Category
from .forms import EventoForm
from apps.users.models import User

from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	events = Event.objects.all().order_by('-created')[:6]
	categories = Category.objects.all()	
	return render(request, 'index.html', {'events' : events,
										  'categories' : categories})

def main_panel(request):
	events = Event.objects.filter(organizer__username='josue').order_by('is_free', '-created')
	cantidad_eventos = events.count()
	return render(request, 'events/panel/panel.html', {'events' : events, 'cantidad' : cantidad_eventos})

def crear_evento(request):
	if request.method == 'POST':
		modelform = EventoForm(request.POST, request.FILES)
		if modelform.is_valid():			
			modelform.save()
			
			return redirect(reverse('events_app:panel'))
	else:
		modelform = EventoForm()

	return render(request, 'events/panel/crear_evento.html', { 'form' : modelform })

def detalle_evento(request, evento_id):
	event = get_object_or_404(Event, pk=evento_id)
	return render(request, 'events/panel/detalle_evento.html', {'event':event})