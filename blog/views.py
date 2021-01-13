from django.shortcuts import render, get_object_or_404
from django.utils import timezone  # timezone 모듈 불러오기
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date')  # 블로그 글목록 게시일 기준 정렬
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
