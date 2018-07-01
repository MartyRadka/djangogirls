# from django.shortcuts import render, get_object_or_404
# from .models import Question
#
#
# def post_list(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)  # helper f() to catch Http404 if the object doesn't exist
#     return render(request, 'blog/post_list.html', {'question': question})

from django.shortcuts import render
from .models import Post
from django.utils import timezone


def post_list(request):
    """ this function will put together our template blog/post_list.html & data """
    # filtruje vsechny publikovane posty starsiho casu, nez ted, takžze bude vlastne filtrovat vsechny
    # lte - less that or equal to <=
    # lt - less than <
    # gte - greater than equal to >=
    # gt - greater than >
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('published_date')
    # request everything we receive from the user via the Internet
    # blog/post_list.html
    # {'posts': posts} = place in which we can add some things for the template to use
    return render(request, 'blog/post_list.html', {'posts': posts})




