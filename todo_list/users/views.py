from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import FormView

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login

class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            messages.success(self.request, f'Hi {self.request.user}, you are registered successfully')
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Enter correct passwords and email')
        return self.render_to_response(self.get_context_data(form=form))
    
    
class LogInView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        messages.success(self.request, f"Hi {self.request.user}, you are logged in successfully")
        return reverse_lazy('tasks')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid password or username')
        return self.render_to_response(self.get_context_data(form=form))


class ProfileView(LoginRequiredMixin, View):

    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'users/profile.html', context)
    
    
    def post(self, request):
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Hi {request.user}, your profile has updated successfully')
            return redirect('profile')
        else:
            context = {'user_form': user_form, 'profile_form': profile_form}
            messages.error(request, 'error updating your profile')
            return render(request, 'users/profile.html', context)


class ProfileDeleteView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "users/profile_delete.html")

    def post(self, request, *args, **kwargs):
        user = request.user
        messages.success(request, f"Hi {user}, your profile has been deleted successfully.")
        user.delete()
        return redirect('register')

