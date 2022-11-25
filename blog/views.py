from django.urls import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import render


# Create your views here.
def starting_page(request):
    return (render(request, 'blog/index.html', {
        "content_snippet": "You have reached starting_page()."
    }))


def posts(request):
    return (render(request, 'blog/index.html', {
        "content_snippet": "You have reached posts()."
    }))


def post_detail(request, slug):
    match(slug):
        case "1":
            return (render(request, 'blog/blog_post.html', {
                "slug": slug
            }))
        case "2":
            return (render(request, 'blog/blog_post.html', {
                "slug": slug
            }))
        case "3":
            return (render(request, 'blog/blog_post.html', {
                "slug": slug
            }))
        case _:
            raise Http404()
