from django.shortcuts import render

# Your existing view
def fun(request):
    return render(request, 'sample.html', {'message': 'Welcome to the Home Page!'})

# NEW: Profile View
def profile_view(request):
    context = {
        'name': 'Your Name',
        'hobby': 'Learning Django'
    }
    return render(request, 'profile.html', context)

# NEW: Contact View
def contact_view(request):
    return render(request, 'contact.html')
