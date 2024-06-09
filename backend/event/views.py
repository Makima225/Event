from django.shortcuts import render, redirect, get_object_or_404
from .models import Participant
from django.core.mail import EmailMessage



def register(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
       name =  request.POST.get('name')
       surname =  request.POST.get('surname')
       email =  request.POST.get('email')
       phone =  request.POST.get('phone')
       residence = request.POST.get('residence')
       obj = Participant.objects.create(name=name, surname=surname, email=email, phone=phone, residence=residence)
       # Envoyer un email avec le Qr code
       email_message = EmailMessage("Hello",
            'Vous venez de recevoir votre pass à travers ce qr code ci-joint.',
            'bauereudes225@example.com',  # Remplacez par votre adresse email
            [obj.email],)
       email_message.attach_file(obj.qr_code.path)
       email_message.send()
       
       
       return redirect("success",participant_id=obj.id )
    return render(request, 'register.html', context)


def success(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    return render(request, 'success.html', {'participant': participant})