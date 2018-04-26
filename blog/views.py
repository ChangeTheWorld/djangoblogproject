from django.shortcuts import render, get_object_or_404
'''from django.http import HttpResponse'''
from .models import Post, Category
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
'''Django ListView视图'''
# Create your views here.

#def index(request):
#    post_list = Post.objects.all()
#    return render(request, 'blog/index.html', context={'post_list': post_list})
class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    #指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 2
'''    
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                     ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
              }
    return render(request, 'blog/detail.html', context=context)
'''
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    
    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response
        
    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
        return post
        
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form':form,
            'comment_list': comment_list
        })
        return context
'''def category(request, pk):
     记得在开始部分导入 Category 类
     cate = get_object_or_404(Category, pk=pk)
     post_list = Post.objects.filter(category=cate).order_by('-created_time')
     return render(request, 'blog/index.html', context={'post_list': post_list})
'''
class CategoryView(IndexView):
    '''model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    '''
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)
    
'''def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
'''
class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month
                                                               )
        
    