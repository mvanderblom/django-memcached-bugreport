# Django memcached bugreport

https://code.djangoproject.com/ticket/33092

## Reproducing the bug

Run containers with `docker-compose up -d`

After the client container exits, view the server logs `docker logs server`

This log should contain errors related to the bug report