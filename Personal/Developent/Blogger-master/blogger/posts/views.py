from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from comments.models import Comment
from comments.forms import Commentform
from django.contrib.contenttypes.models import ContentType

# Create your views here.
@login_required
def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	#if not request.user.is_authenticated():
	#	raise Http404

	form=PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, 'posts/post_form.html', context)

def post_detail(request, slug = None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.draft or instance.publish > timezone.now().date():
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share = quote(instance.content)
	initial_data={
		"content_type": instance.get_comment_type,
		"object_id": instance.id
	}
	comment_form = Commentform(request.POST or None, initial=initial_data)
	if comment_form.is_valid():
		c_type=comment_form.cleaned_data.get("content_type")
		content_type=ContentType.objects.get(model=c_type)
		obj_id=comment_form.cleaned_data.get('object_id')
		content_data=comment_form.cleaned_data.get('content')
		new_comment, created= Comment.objects.get_or_create(
								user=request.user,
								content_type=content_type,
								object_id=obj_id,
								content=content_data
							)
	comments = instance.comments#Comment.objects.filter_by_instance(instance)
	context = {
		"title": instance.title,
		"obj": instance,
		"share": share,
		"comments": comments,
		"comment_form": comment_form,
	}
	return render(request, 'posts/post_detail.html', context)

def post_list(request):
	today = timezone.now().date()
	if not request.user.is_staff or not request.user.is_superuser:
		queryset_list = Post.objects.active()#.order_by('-timestamp')
	else:
		queryset_list = Post.objects.all()#.order_by('-timestamp')
	query = request.GET.get('q')
	#queryset_list = queryset_list.filter(user=request.user)
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query) |
				Q(content__icontains=query) |
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var = 'page'
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	#if request.user.is_authenticated():
	#	context = {
	#		"title": "My list"
	#	}
	#else:
	context = {
		"title": "List",
		"object_list": queryset,
		'page_request_var': page_request_var,
		"today" : today,
	}
	return render(request, 'posts/post_list.html', context)

@login_required
def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form=PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Successfully updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"obj":instance,
		"form":form,
	}
	return render(request, 'posts/post_form.html', context)

@login_required
def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)	
	messages.success(request, "Successfully deleted")
	instance.delete()
	return redirect("post:list")
