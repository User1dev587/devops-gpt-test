# Dockerfile to build NGINX image serving static website
FROM nginx:stable
COPY ./ /usr/share/nginx/html/
