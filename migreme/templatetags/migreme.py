import urllib
import urllib2

from django import template
from django.core.cache import cache
from django.core.validators import URLValidator, ValidationError

register = template.Library()

@register.filter
def migreme(value):
    if isinstance(value, unicode):
        value = value.encode('utf-8')

    # Create URL validator
    url_validator = URLValidator()
    # Check if sent URL is valid
    try:
        url_validator(value)
    except ValidationError:
        return value

    data = urllib.urlencode({'url': value})

    # Generate cache key
    cache_key = 'migreme_{0}'.format(data)

    # Find URL in cache
    cached_shortned = cache.get(cache_key)
    if cached_shortned:
        return cached_shortned

    # Short URL with migre.me
    try:
       shortned = urllib2.urlopen('http://migre.me/api.txt?' + data).read()
    except urllib2.URLError, urllib2.HTTPError:
       return value

    # Check if generated URL is valid
    try:
        url_validator(shortned)
    except ValidationError:
        return value

    # Add URL shorted to cache for 1 month    
    cache.set(cache_key, shortned, 60 * 60 * 24 * 30)
    return shortned