from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),#setting the homepage to all the current published posts in the blog.
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),#(?P<pk>\d+) this is for identifying which particular post we're talking about, like Post1 or Post2 etc 1 or 2 are Primary Key Identifiers here
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(),name='post_edit'),#look at the above comment to understand why (?P<pk>\d+) is used here.
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(),name='post_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post,name='add_comment_to_post'),# Here since Comment is a function based view for the corresponding URL we don't need to the extension .as_view() and (?P<pk>\d+) is used to to refer to the Primary KEY for That Particular Post
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve,name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'), # this is for a post one unlike  a few other above which were for comments. this is the final one to publish the comments !
]
