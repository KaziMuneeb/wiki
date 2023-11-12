from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound 
from . import util
import markdown , random


def index(request):
    if request.method == "POST":
        title = request.POST['q']
        list = []
        if title in list:
            return redirect('display', title=title)
        else:
            for entry in util.list_entries():
                if title.lower() in entry.lower():
                    list.append(entry)
            return render(request, 'encyclopedia/index.html', {
                'entries': list,
                'heading': "Available Entries"
            })

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        'heading': "All Pages"
    })


def display(request, title):
    content = util.get_entry(title)
    if content is not None:
        return render(request, 'encyclopedia/entry.html', {
            'title': title,
            'contents': markdown.markdown(content)
        })
    else:
        return HttpResponseNotFound(request)


def new_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if title.lower() in map(str.lower, util.list_entries()) and "edit" in request.build_absolute_uri():
            return render(request, 'encyclopedia/new_entry.html', {
                'message': 'Error!! This entry alredy exists...'
            })
        else:
            util.save_entry(title, content)
            return redirect("display", title=title)

    return render(request, 'encyclopedia/new_entry.html')


def edit_page(request, title):
    content = util.get_entry(title)
    return render(request, 'encyclopedia/new_entry.html', {
        'title': title,
        'content': content
    })

def random_pages(request):
    title = random.choice(util.list_entries())
    return redirect('display',title = title)
    