from django.db.models import Count
from django import template
from ..models import Post, Comment
from django.db.models import Q
import markdown
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    # post_with_comments = Comment.objects.filter(active=True).values('post_id').
    # annotate(total_comments=Count('post_id')).order_by(
    #     '-total_comments').values_list('post_id', flat=True)
    #
    # return Post.published.filter(id__in=post_with_comments)[:count]
    return Post.published.annotate(active_comments_count=Count('comments', filter=Q(comments__active=True))).filter(
        active_comments_count__gte=1).order_by(
        '-active_comments_count')[:count]
    # return Post.published.annotate(
    #     total_comments=Count('comments')
    # ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
