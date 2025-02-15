from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board

def index(request):
    boards = Board.objects.all()
    return render(request, 'board/index.html', {'boards': boards})

def register(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Board.objects.create(title=title, content=content)
        return redirect('index')
    return render(request, 'board/register.html')

def view_board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board/view.html', {'board': board})

def modify(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.save()
        return redirect('index')
    return render(request, 'board/modify.html', {'board': board})
    
def delete_board(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('index')