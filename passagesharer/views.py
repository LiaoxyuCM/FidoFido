from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.db.models import Q
from django.urls import Resolver404
from .models import Passage

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
        passage = Passage.objects.get(pk=passage_id)  # Fetch the specific passage by ID
    except Passage.DoesNotExist:
        return render(request, 'homepage/404.html', status=404, context={"current_path": request.path})
    # Markdown support
    import markdown
    passage_content_html = markdown.markdown(passage.content)
    return render(request, 'homepage/detail.html', {'passage': passage, 'passage_content_html': passage_content_html})


def search_passages(request: HttpRequest) -> HttpResponse:
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Passage.objects.filter(
            Q(title__icontains=query)
        ).order_by('-created_at')
    return render(request, 'homepage/search.html', {'query': query, 'results': results})
