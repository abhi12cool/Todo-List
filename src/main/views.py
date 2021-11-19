from django.shortcuts import render
from .models import Todo

# Create your views here.
def TodoListView(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        item = request.POST.get('item')
        if text != None:
            text = text.strip()
            Todo.objects.get_or_create(todo=text)
        if item != "":
            try:
                item = Todo.objects.get(todo=item)
                item.delete()
            except Todo.DoesNotExist:
                item = None
            
    context = {
        'object_list' : Todo.objects.all(),
    }
    return render(request, 'home.html', context)