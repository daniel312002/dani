from django.shortcuts import render, get_object_or_404
from .models import Post
def render_posts(resquest):
    posts = Post.objects.all()
    return render(resquest, 'posts.html',{'posts' : posts})

def post_detail(resquest, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(resquest, 'post_detail.html', {"post": post_id})