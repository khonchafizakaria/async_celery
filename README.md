# async_celery 
[This repo is configured from my own, replace with your own values]

- Clone this repo into your project directory.
- Replace line 8 in `async_celery/app.py` with your own value.
- paste these 2 lines in `<BASE_DIR>/<settings_folder>/__init__.py`

<pre>
  <code>
    from __future__ import absolute_import
    from async_celery.app import app as celery_app
   </code>
</pre>

- locks require `pymemcache` and `redis`.
- `celery_results` relies on `django_celery_results`
