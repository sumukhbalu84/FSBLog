from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post,Comment
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required #Decorators that can be used in case they're required!
from blog.forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin #mixins
from django.views.generic import (TemplateView,ListView,   #These are all the Generic views that come Built into Django.
                                    DetailView,CreateView,
                                    UpdateView,DeleteView,
                                    )
#These are Views for Post
# Template Views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

#Whatevers Underneath here are My CRUD views

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')#Here, after a Post is Deleted we want to display the list of the posts(post_list) remaining. we have to use reverse_lazy because you want the website to take its time after a deleting a post ; you dont want it to immediately jump to places here and there after deleting a Post.

class DraftListView(ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):# Here we Don't want Posts that have a Publication date as that means they're published, Drafts are for Posts that are'nt Published!
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

########################################################################################################
########################################################################################################
# These are the views for the Comments:
# Views for the comments are Function_Based Views unlike the Class Based Views for the Post.

#this one particular view is for post publishing!
@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)



#this is the first Functional view for Comments!
@login_required# Login is Required to Post Comments!
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)# if Post object is not found, return Error404 Not Found!
    if request.method == 'POST':
        form = CommentForm(request.POST)#pass in the request if and only if method == POST!
        if form.is_valid():# Django has some built in process for form validation and validating the form before using it is very important!
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
        return render(request,'blog/comment_form.html',{'form':form})

#This is for Comment approval:
@login_required #Login is Compulsory to execute this function:
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)#Same thing as above Get Comment if the corresponding primary key of the post the comment has to be attached to exists!
    comment.approve()# Check Models.py approve_comments; this basically just approves the comment and tell us that this particular comment is approved!
    return redirect('post_detail',pk=comment.post.pk)#after successfull addition of comment we are now redirected to the post_detail view where we can now see the newly added comments alongwith their respective Posts!


#this is for removing  a comment:

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk # Here we have to create a new variable post_pk because we are deleting our Comment from our original Post!
    comment.delete()
    return redirect('post_detail',pk=post_pk)
