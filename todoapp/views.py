from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from todoapp.models import Task

OBJECT_NAME_TASK = 'task'
OBJECT_NAME_TASK_LIST = 'task_list'
URL_NAME_TASK_LIST = 'task_list'
INPUT_NAME_SEARCH = 'search'
FORM_FIELDS = ['title', 'category', 'description', 'completed']


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = OBJECT_NAME_TASK_LIST

    def get_context_data(self, **kwargs):
        # コンテキストを取得
        context = super().get_context_data(**kwargs)
        # タスクをログインユーザーでフィルタ
        context[OBJECT_NAME_TASK_LIST] = context[OBJECT_NAME_TASK_LIST].filter(user=self.request.user)
        # 検索窓を設定
        search_input_text = self.request.GET.get(INPUT_NAME_SEARCH) or ''
        # 検索入力があった場合
        if search_input_text is not None:
            context[OBJECT_NAME_TASK_LIST] = context[OBJECT_NAME_TASK_LIST].filter(title__icontains=search_input_text)
        # 検索窓を設定
        context[INPUT_NAME_SEARCH] = search_input_text
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = OBJECT_NAME_TASK


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = FORM_FIELDS
    success_url = reverse_lazy(URL_NAME_TASK_LIST)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = FORM_FIELDS
    success_url = reverse_lazy(URL_NAME_TASK_LIST)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = OBJECT_NAME_TASK
    fields = '__all__'
    success_url = reverse_lazy(URL_NAME_TASK_LIST)
