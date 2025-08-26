# Plenitas — Personalized Video Recommender

A lightweight Django prototype that shows **personalized product suggestions** while a user watches a video. After ~10 seconds of playback, a popup recommends a product aligned with the user’s interests.

---

## Features
- User profiles with interests
- Simple product catalog
- Video player with a **10s** popup recommendation
- Rule-based matching (interests ↔ product tags)
- Django admin for quick data entry

---

## Tech Stack
- Python 3.10+ & Django
- SQLite for local dev (or any DB via `DATABASE_URL`)
- Django templates + vanilla JS

---

## Quickstart (60 seconds)

```bash
# 1) Clone
git clone https://github.com/jedfoster02/plenitas_project.git
cd plenitas_project

# 2) Virtual env
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

# 3) Install deps
# If requirements.txt exists:
pip install -r requirements.txt
# If not, at minimum:
# pip install django python-dotenv

# 4) Environment variables
cp .env.example .e
