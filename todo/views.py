from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import TodoItem

# Register view for user signup
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view for user authentication
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('todo_list')  # Redirect to to-do list page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Only logged-in users can access their to-do list
@login_required
def todo_list(request):
    # Fetch all to-do items for the logged-in user
    todos = TodoItem.objects.filter(user=request.user)

    if request.method == 'POST':
        # Handle form submission to add a new to-do item
        todo_text = request.POST.get('todo-input')
        if todo_text:
            TodoItem.objects.create(user=request.user, text=todo_text)
        return redirect('todo_list')  # Redirect to the same page to display the updated list

    return render(request, 'todo_list.html', {'todos': todos})

# Delete a to-do item
@login_required
def delete_todo(request, id):
    try:
        todo_item = TodoItem.objects.get(id=id, user=request.user)  # Ensure it's the user's task
        todo_item.delete()  # Delete the task
        return redirect('todo_list') # Redirect back to the todo list
    except TodoItem.DoesNotExist:
        return redirect('todo_list')

