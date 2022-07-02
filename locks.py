import time
from contextlib import contextmanager

from django.core.cache import cache

LOCK_EXPIRE = 60 * 10  # Lock expires in 10 minutes


@contextmanager
def redis_lock(lock_id, oid):
    timeout_at = time.monotonic() + LOCK_EXPIRE - 3
    status = cache.add(lock_id, oid, timeout=LOCK_EXPIRE)
    try:
        yield status
    finally:
        if time.monotonic() < timeout_at and status:
            cache.delete(lock_id)


@contextmanager
def memcached_lock(lock_id, oid):
    timeout_at = time.monotonic() + LOCK_EXPIRE - 3
    from django.core.cache import caches
    from django.utils.connection import ConnectionProxy

    cache = ConnectionProxy(caches, 'memcached')
    status = cache.add(lock_id, oid, timeout=LOCK_EXPIRE)

    try:
        yield status
    finally:
        if time.monotonic() < timeout_at and status:
            cache.delete(lock_id)
