from django.views.generic import dates, list
from django.conf import settings

from basic.blog.models import *

class PostListView(list.ListView):
    page_size = getattr(settings,'BLOG_PAGESIZE', '20')
    queryset = Post.objects.published()
    paginate_by = page_size

class PostArchiveYearView(dates.YearArchiveView):
    date_field = 'publish'
    queryset = Post.objects.published()
    make_object_list = True

class PostArchiveMonthView(dates.MonthArchiveView):
    date_field = 'publish'
    queryset = Post.objects.published()

class PostArchiveDayView(dates.DayArchiveView):
    date_field = 'publish'
    queryset = Post.objects.published()

class PostDetailView(dates.DateDetailView):
    date_field = 'publish'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.published()

class CategoryListView(list.ListView):
    """
    Category list

    Template: ``blog/category_list.html``
    Context:
        object_list
            List of categories.
    """
    queryset = Category.objects.all()
    template_name = 'blog/category_list.html'

class CategoryDetailView(list.ListView):
    """
    Category detail

    Template: ``blog/category_detail.html``
    Context:
        object_list
            List of posts specific to the given category.
        category
            Given category.
    """
    template_name = 'blog/category_detail.html',

    def get_queryset(self):
        return Category.objects.filter(slug__iexact=self.slug).post_set.published()
