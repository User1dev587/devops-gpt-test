# COMMENT: Dockerfile for containerizing the NGINX website using the official NGINX image
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
