from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Task, ChatWithAI
from .openrounter_utils import query_openrouter
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

class AskAIView(LoginRequiredMixin, View):
    """
    Handles the AI query and returns a response with the AI's answer.
    This view processes POST requests containing a prompt, queries the AI using
    the provided prompt, and returns the AI's response in JSON format.
    """

    def get(self, request, *args, **kwargs):
        chat_objects = ChatWithAI.objects.filter(user=request.user).order_by('created_at')
        chat_history = [{'request': chat.request, 'response': chat.ai_response} for chat in chat_objects]
        return render(request, 'todo/ask_ai.html', {"chat_history": chat_history})

    def post(self, request, *args, **kwargs):
        prompt = request.POST["user_input"]
        openrouter_ai_response = query_openrouter(prompt)
        ai_message = openrouter_ai_response["choices"][0]["message"]["content"]

        # Save the chat to the database
        chat = ChatWithAI.objects.create(request=prompt, ai_response=ai_message, user=request.user, title=prompt[:15])
        chat.save()

        chat_objects = ChatWithAI.objects.filter(user=request.user).order_by('created_at')
        chat_history = [{'request': chat.request, 'response': chat.ai_response} for chat in chat_objects]

        return render(request, 'todo/ask_ai.html', {"chat_history": chat_history})

class ChatDeleteView(LoginRequiredMixin, View):
    """
    Handles the deletion of chat entries for the authenticated user.
    Ensures that users can only delete their own chat entries.
    """

    def post(self, request, *args, **kwargs):
        chat = ChatWithAI.objects.filter(user=request.user)
        if not chat.exists():
            messages.error(request, 'No chat found to delete.')
        else:
            chat.delete()
            messages.success(request, 'Chat deleted successfully.')
        return HttpResponseRedirect(reverse_lazy('ask-ai'))

    def get(self, request, *args, **kwargs):
        return render(request, 'todo/chat_confirm_delete.html')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        """
        Override the context data to include user-specific tasks.
        This method customizes the context by filtering tasks to include only those
        associated with the currently authenticated user. It enhances the base
        implementation from the parent class by introducing user-specific
        filtering logic.
        """
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    content_object_name = 'task'

    def get_queryset(self):
        """
        Fetches and returns a filtered queryset for the TaskDetail view, limited to
        tasks associated with the currently authenticated user. This ensures that
        users can only access their own tasks.
        Returns:
            QuerySet: A queryset containing tasks limited to the authenticated user.
        """
        base_qs = super(TaskDetail, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Hi {self.request.user}, the task was created successfully')
        return super(TaskCreate, self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(TaskCreate, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Hi {self.request.user}, the task was updated successfully')
        return super(TaskUpdate, self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(TaskUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)
    
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, f'Hi {self.request.user}, the task was deleted successfully')
        return super(TaskDelete, self).form_valid(form)
    
    def get_queryset(self):
        base_qs = super(TaskDelete, self).get_queryset()
        return base_qs.filter(user=self.request.user)

