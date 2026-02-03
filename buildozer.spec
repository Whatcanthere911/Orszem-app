[app]

# (str) Title of your application
title = Orszem

# (str) Package name
package.name = orszem

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Fontos: szóközök nélkül a vesszők után!
requirements = python3,kivy==2.2.1,cython==0.29.33,hostpython3

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) Android architecture to build for
android.archs = arm64-v8a

# (int) Log level (0 = error only, 1 = info, 2 = debug)
# Ezt 2-re állítottuk, ahogy a GitHub kérte a hibaüzenetben!
log_level = 2

[buildozer]

# (int) UNICODE Error handling
bin_dir = ./bin
