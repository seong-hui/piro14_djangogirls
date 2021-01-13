from django.shortcuts import render
from django.utils import timezone  # timezone 모듈 불러오기
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        'published_date')  # 블로그 글목록 게시일 기준 정렬
    return render(request, 'blog/post_list.html', {'posts': posts})
