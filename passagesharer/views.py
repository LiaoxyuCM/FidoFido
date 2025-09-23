from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.urls import Resolver404
import markdown
from .models import Passage
from .forms import CommentForm
from .models import Comment

# Create your views here.

def err404(request: HttpRequest, exception: Resolver404) -> HttpResponse:
    return render(request, 'homepage/404.html', status=404, context={"current_path": request.path, "exception": type(exception).__name__})

def index(request: HttpRequest) -> HttpResponse:
    try:
        passages = Passage.objects.order_by('-created_at')[:10]  # Fetch passages ordered by creation date
    except Passage.DoesNotExist:
        return render(request, 'homepage/404.html', status=404, context={"current_path": request.path})
    return render(request, 'homepage/index.html', {'passages': passages, 'is_logged': request.user.is_authenticated, 'username': request.user.get_username()})

def detail(request: HttpRequest, passage_id: int) -> HttpResponse:
    try:
        passage = Passage.objects.get(id=passage_id)  # Fetch the specific passage by ID
    except Passage.DoesNotExist:
        return render(request, 'homepage/404.html', status=404, context={"current_path": request.path})
    # Markdown support
    passage_content_html = markdown.markdown(passage.content)
    comments = Comment.objects.filter(to_passage=passage).select_related('reviewer').all()
    if request.method == 'POST':
        if 'delete_comment_id' in request.POST:
            comment_id = request.POST.get('delete_comment_id')
            comment = get_object_or_404(Comment, id=comment_id, to_passage=passage)
            if comment.reviewer == request.user:
                comment.delete()
                return redirect('detail', passage_id=passage_id)
        if not request.user.is_authenticated:
            form = CommentForm(request.POST)
            form.add_error(None, 'Please login before commenting')
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.to_passage = passage
                comment.reviewer = request.user
                comment.save()
                return redirect('detail', passage_id=passage_id)
    else:
        form = CommentForm()
    return render(request, 'homepage/detail.html', {
        'passage': passage,
        'passage_content_html': passage_content_html,
        'comments': comments,
        'form': form
    })


def search_passages(request: HttpRequest) -> HttpResponse:
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Passage.objects.filter(
            Q(title__icontains=query)
        ).order_by('-created_at')
    return render(request, 'homepage/search.html', {'query': query, 'results': results})


def change_color_mode(request: HttpRequest, color_mode: str) -> HttpResponse:
    if request.method != 'GET':
        return HttpResponse(status=405)
    response = redirect(request.GET.get('next', 'index'))
    response.set_cookie('color_mode', color_mode, max_age=30*24*60*60)  # 30 days
    return response
