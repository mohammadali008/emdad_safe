from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ticket

@login_required
def ticket_list_view(request):
    tickets = Ticket.objects.filter(user=request.user, is_active=True)
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})
