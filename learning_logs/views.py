from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# The home page for Learning Log!
def index(request):
    return render(request, "learning_logs/index.html")

# The Topics page
@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') 
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html',context)

# shows a single topic and all its entries!
@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    # Make sure the user owns the topic
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}

    return render(request, "learning_logs/topic.html",context)

# new topic form
@login_required
def new_topic(request):
    """Add a new topic"""   
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        form = TopicForm(data = request.POST)

        if form.is_valid():
            
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            return redirect('learning_logs:topics' )
    # Display a blank or invalid form
    context = {'form': form}

    return  render(request, 'learning_logs/new_topic.html', context)


# new entry form
@login_required
def new_entry(request, topic_id):
    topic =Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # No data submitted - create a blank form!
        form = EntryForm()
    else:
        # Data submitted - Process the data
        form = EntryForm(data = request.POST) 
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)

    # Display a blank or invalid form
    context = {'topic': topic, 'form': form}

    return render(request, 'learning_logs/new_entry.html', context)


# editing entry
@login_required
def edit_entry(request,entry_id):
    entry = Entry.objects.get(id=entry_id)

    # Protect the edit entry from Non-Owners
    if entry.owner != request.user:
        raise Http404
    topic = entry.topic
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry        
        form =EntryForm(instance = entry)
    else:
        form = EntryForm(instance= entry, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}

    return render(request, 'learning_logs/edit_entry.html', context)
    
