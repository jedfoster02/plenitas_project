"""
core/views.py
-------------
Centralized, clean view layer for the Plenitas prototype.

Endpoints
---------
1. /recommend/<user_id>/        – Simple product‐recommendation page
2. /watch/<user_id>/<video_id>/ – Video player + timed popup ad
3. /select/                     – User and video selection
"""

import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Product, Video, ViewingHistory

# ────────────────────────────────────────────────
# 1. SIMPLE RECOMMENDATION PAGE (for testing/demo)
# ────────────────────────────────────────────────
def recommend_products(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    interests = user.preferences.all()
    products = Product.objects.filter(category__in=interests).distinct()

    return render(request, "recommendations.html", {
        "user": user,
        "products": products,
    })

# ────────────────────────────────────────────────
# 2. VIDEO PLAYER + POPUP AD + VIEWING HISTORY
# ────────────────────────────────────────────────
def watch_video(request, user_id, video_id):
    user = get_object_or_404(User, pk=user_id)
    video = get_object_or_404(Video, pk=video_id)

    # Record the view
    ViewingHistory.objects.create(user=user, video=video)

    # Fetch recent viewing history (last 5 videos)
    history = ViewingHistory.objects.filter(user=user).order_by('-watched_at')[:5]

    # Pick one product ad to show in popup (random from user's interests)
    all_products = []
    for interest in user.preferences.all():
        products = list(Product.objects.filter(category=interest))
        if products:
            all_products.append(random.choice(products))

    popup_product = random.choice(all_products) if all_products else None

    return render(request, 'watch_video.html', {
        'user': user,
        'video': video,
        'history': history,
        'popup_product': popup_product,
    })

# ────────────────────────────────────────────────
# 3. USER + VIDEO SELECTION & REDIRECTS
# ────────────────────────────────────────────────
def select_user(request):
    users = User.objects.all()
    return render(request, 'select_user.html', {'users': users})

def select_video(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    videos = Video.objects.all()
    return render(request, 'select_video.html', {'user': user, 'videos': videos})

def watch_video_redirect(request):
    user_id = request.GET.get('user_id')
    video = Video.objects.first()
    return redirect('watch_video', user_id=user_id, video_id=video.id)
