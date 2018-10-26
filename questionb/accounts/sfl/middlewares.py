"""
MiddleWare for usage to restrict appllication usage to single session
"""

# Session model stores the session data
from django.contrib.sessions.models import Session

class UserRestrict(object):
    def process_request(self, request):
        # Checks if different session exists for user and deletes it
        if request.user.is_authenticated():
            cache = get_cache('default')
            cache_timeout = 86400
            cache_key = "user_pk_%s_restrict" % request.user.pk
            cache_value = cache.get(cache_key)

            if cache_value is not None:
                if request.session.session_key != cache_value:
                    engine = import_module(settings.SESSION_ENGINE)
                    session = engine.SessionStorage(session_key=cache_value)
                    session.delete()
                    cache.set(cahce_key, request.session.session_key, cache_timeout)
            else:
                cache.set(cache_key, request.session.session_key, cache_timeout)


