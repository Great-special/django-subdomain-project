from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'app', 'PMS.urls', name='app'),  # Default host
    host(r'blog', 'blog.urls', name='blog'),        # blog.example.com
    host(r'user', 'users.urls', name='user'),        # user.example.com
)
