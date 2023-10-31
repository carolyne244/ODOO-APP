from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def create_account(request):
    # Implement your create account logic here
    return render(request, 'create_account.html')

def profile_view(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def my_time_off(request):
    return render(request, 'my_time_off.html')

def time_off_type_form(request):
    return render(request, 'time_off_type_form.html')

def time_off_request_form(request):
    return render(request, 'time_off_request_form.html')

def time_off_allocation_form(request):
    return render(request, 'time_off_allocation_form.html')

def my_time_off_table(request):
    time_off_data = [
        {'employee': 'John Doe', 'type': 'Paid', 'start_date': '2023-08-01', 'end_date': '2023-08-05', 'duration': '5 days', 'status': 'Approved'},
    ]
    
    context = {'time_off_data': time_off_data}
    return render(request, 'my_time_off_table.html', context)

def time_off_table(request):
    return render(request, 'time_off_table.html')