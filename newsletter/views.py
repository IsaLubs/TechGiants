from django.shortcuts import render, redirect
from django.contrib import messages

def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Here you would typically save the email to your database
        # For now, we'll just add a success message
        messages.success(request, f'Thank you for subscribing with {email}!')
        return redirect('newsletter_signup')
    return render(request, 'newsletter_signup.html')