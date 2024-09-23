from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'PMS.urls', name='www'),  # Default host
    host(r'blog', 'blog.urls', name='blog'),        # blog.example.com
    host(r'user', 'user.urls', name='user'),        # user.example.com
)
