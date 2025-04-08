from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import UserEditForm,ProfileEditForm
from django.contrib import messages
from authentication.models import Profile
from .models import Post, Friendship,User,Like,Comment
from .forms import PostForm, CommentForm

@login_required
def home(request):
    posts = Post.objects.all().order_by("-created_at")
    
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
   
   
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("social:home")
    else:
        form = PostForm()
    following_ids = Friendship.objects.filter(follower=request.user).values_list("following_id", flat=True)
    people_to_connect = Profile.objects.exclude(user__id__in=following_ids).exclude(user=request.user)
    posts = Post.objects.all().order_by("-created_at")
    users = User.objects.exclude(id=request.user.id)  # Get all other users
    following = list(Friendship.objects.filter(follower=request.user).values_list("following_id", flat=True))
    return render(request, 'homepage.html', {
                    'form':form,
                    'posts':posts,
                    'profile':profile,
                    'people_to_connect':people_to_connect,
                    "users": users,
                    "following": following,
    })

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect('social:profile_edit')
        else:
            messages.error(request, "Error updating your profile.")
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)
    return render(request, 'profile.html', {'user_form':user_form, 'profile_form':profile_form, 'profile':profile})

#Connect view section
@login_required
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(User, id=user_id)
    if request.user != user_to_follow:
        Friendship.objects.get_or_create(follower=request.user, following=user_to_follow)
    # Get the 'next' parameter to determine the previous page
    next_page = request.GET.get('next', 'social:home')  # Defaults to 'home' if 'next' isn't provided
    return redirect(next_page)

@login_required
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(User, id=user_id)
    follow_instance = Friendship.objects.filter(follower=request.user, following=user_to_unfollow)
    if follow_instance.exists():
        follow_instance.delete()
    # Get the 'next' parameter to determine the previous page
    next_page = request.GET.get('next', 'social:home')  # Defaults to 'home' if 'next' isn't provided
    return redirect(next_page)

@login_required
def like_post(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect("social:home")
    
@login_required
def like_comment(request, comment_id):
    user = request.user  
    comment = get_object_or_404(Comment, id=comment_id)
    if user in comment.likes.all():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)
    return redirect("social:home")
       
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('social:home')
    return redirect('social:home')

@login_required
def friends_list(request):
    following_ids = Friendship.objects.filter(follower=request.user).values_list("following_id", flat=True)
    friends = User.objects.filter(id__in=following_ids)  # Get user objects of those being followed
    profile = Profile.objects.get(user=request.user)
    
    friends_with_profiles = []
    for friend in friends:
        friend_profile = Profile.objects.filter(user=friend).first()
        friends_with_profiles.append({"id":friend.id, "user":friend, "profile_image":friend_profile.photo.url if friend_profile and friend_profile.photo else None})
    return render(request, 'friends.html', {'friends': friends, 'friends_with_profiles':friends_with_profiles, 'profile':profile})
    
    
@login_required
def network(request):
    profile = Profile.objects.get(user=request.user)
    following_ids = Friendship.objects.filter(follower=request.user).values_list("following_id", flat=True)
    people_to_connect = Profile.objects.exclude(user__id__in=following_ids).exclude(user=request.user)
    return render(request, 'network.html', {'people_to_connect':people_to_connect, 'profile':profile})