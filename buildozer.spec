[app]

# ── Identity ──────────────────────────────────────────────────────────────────
title         = SkillBond
package.name  = skillbond
package.domain = com.skillbond
version       = 1.0

# ── Source ────────────────────────────────────────────────────────────────────
source.dir          = .
source.include_exts = py,png,jpg,kv,atlas,ttf
source.exclude_dirs = venv,.venv,.git,__pycache__,.github,bin,.buildozer

# ── Requirements ──────────────────────────────────────────────────────────────
# Single line — multiline breaks buildozer silently
# KivyMD installed from GitHub zip (2.0.1 not on PyPI as stable)
requirements = python3,kivy==2.3.0,https://github.com/kivymd/KivyMD/archive/2.0.1.zip,pillow,certifi

# ── Android ───────────────────────────────────────────────────────────────────
android.permissions     = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api             = 33
android.minapi          = 24
android.ndk             = 25b
android.ndk_api         = 24

# arm64 only — building both archs doubles build time and often causes OOM on CI
android.archs           = arm64-v8a

android.accept_sdk_license  = True
android.allow_backup        = False
android.release_artifact    = apk

# ── python-for-android ────────────────────────────────────────────────────────
p4a.branch = master

# ── Display ───────────────────────────────────────────────────────────────────
orientation = portrait
fullscreen  = 0

# ── Logging ───────────────────────────────────────────────────────────────────
log_level = 2

[buildozer]
log_level    = 2
warn_on_root = 1
