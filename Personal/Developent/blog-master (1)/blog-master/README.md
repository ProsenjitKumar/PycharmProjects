# Blog App
blog is a Django powered app with advanced features.


Usage
-

add `blog` to your `INSTALLED_APPS`.

on top of your `settings.py` file add the line below.

```python

from blog.blog_settings import get_required_apps

```

then just below `INSTALLED_APPS` add the line below

```python
INSTALLED_APPS += get_required_apps()
```

finally add `url(r'^blog', include('blog.urls', namespace='blog'))` in your main `urls.py` file


**DEMO COMING SOON.**