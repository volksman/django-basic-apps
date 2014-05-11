from django.conf.urls import *

from basic.blog.views import (CategoryDetailView, CategoryListView,
    PostListView, PostArchiveYearView, PostArchiveMonthView, PostArchiveDayView,
    PostDetailView)


urlpatterns = patterns('basic.blog.views',
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        PostDetailView.as_view(),
        name='blog_detail'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/$',
        PostArchiveDayView.as_view(),
        name='blog_archive_day'
    ),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
        PostArchiveMonthView.as_view(),
        name='blog_archive_month'
    ),
    url(r'^(?P<year>\d{4})/$',
        PostArchiveYearView.as_view(),
        name='blog_archive_year'
    ),
    url(r'^categories/(?P<slug>[-\w]+)/$',
        CategoryDetailView.as_view(),
        name='blog_category_detail'
    ),
    url(r'^categories/$',
        CategoryListView.as_view(),
        name='blog_category_list'
    ),
    url(r'^page/(?P<page>\d+)/$',
        PostListView.as_view(),
        name='blog_index_paginated'
    ),
    url(r'^$',
        PostListView.as_view(),
        name='blog_index'
    ),
)
