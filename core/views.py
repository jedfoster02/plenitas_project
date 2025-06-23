"""
core/views.py
-------------
Centralized, clean view layer for the Plenitas prototype.

Endpoints
---------
1. /recommend/<user_id>/       – Simple product‐recommendation page
2. /watch/<user_id>/<video_id>/ – Video player + timed popup ad
"""

import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    User,        # custom user model with ManyToMany → Interest
    Product,     # each Product belongs to a single Interest (category)
    Video        # uploaded .mp4 file
)

# ────────────────────────────────────────────────────────────────────
# 1.  SIMPLE RECOMMENDATION PAGE (can keep for testing / demo slides)
# ────────────────────────────────────────────────────────────────────
def recommend_products(request, user_id):
    """
    Render a page that lists every product matching the user's interests.
    Useful for quick QA or as a separate dashboard.
    """
    user = get_object_or_404(User, pk=user_id)

    interests = user.preferences.all()
    products  = Product.objects.filter(category__in=interests).distinct()

    return render(
        request,
        "recommendations.html",
        {"user": user, "products": products},
    )

# ────────────────────────────────────────────────────────────────────
# 2.  VIDEO + ONE RANDOM POPUP AD
# ────────────────────────────────────────────────────────────────────
def watch_video(request, user_id, video_id):
    """
    • Plays the chosen video.
    • Picks exactly ONE random product from the user's four interests.
    • That single product is passed to the template (popup_product) and
      revealed by JS 10 s after playback starts.
    """
    user  = get_object_or_404(User, pk=user_id)
    video = get_object_or_404(Video, pk=video_id)

    # -------------------------------
    # Pull ONE random product per user interest
    # -------------------------------
    all_products = []
    for interest in user.preferences.all():
        # Grab all products for this interest, then randomly choose one
        interest_products = list(Product.objects.filter(category=interest))
        if interest_products:
            all_products.append(random.choice(interest_products))

    popup_product = random.choice(all_products) if all_products else None

    # -------------------------------
    # Render
    # -------------------------------
    return render(
        request,
        "watch_video.html",
        {
            "user":          user,
            "video":         video,
            "popup_product": popup_product,
        },
    )


# -------------------------------------
# 3. USER SELECTION + REDIRECT TO VIDEO
# -------------------------------------

def select_user(request):
    users = User.objects.all()
    return render(request, 'select_user.html', {'users': users})

def watch_video_redirect(request):
    user_id = request.GET.get('user_id')
    video = Video.objects.first()  # Or customize which video to start with
    return redirect('watch_video', user_id=user_id, video_id=video.id)
