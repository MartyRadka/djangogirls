from django.shortcuts import render
from .models import Post


def post_list(request):
    """ this function will put together our template blog/post_list.html & data """
    # filtruje vsechny publikovane posty starsiho casu, nez ted, takze bude vlastne filtrovat vsechny
    # lte - less that or equal to <=
    # lt - less than <
    # gte - greater than equal to >=
    # gt - greater than >
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('published_date')
    # request everything we receive from the user via the Internet
    # blog/post_list.html
    # {'posts': posts} = place in which we can add some things for the template to use
    # main_story = jinaappka.views.post_detail
    # "main_story" : main_story
    return render(request, 'post_list.html', {'posts': posts})
