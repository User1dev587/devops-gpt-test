FROM nginx:stable
COPY index.html /usr/share/nginx/html/index.html
# Uncomment the following line to use the custom NGINX configuration file.
# COPY nginx.conf /etc/nginx/conf.d/default.conf
