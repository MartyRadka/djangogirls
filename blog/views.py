# from django.shortcuts import render, get_object_or_404
# from .models import Question
#
#
# def post_list(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)  # helper f() to catch Http404 if the object doesn't exist
#     return render(request, 'blog/post_list.html', {'question': question})

from django.shortcuts import render


def post_list(request):
    """ this function will put together our template blog/post_list.html """
    return render(request, 'blog/post_list.html', {})
