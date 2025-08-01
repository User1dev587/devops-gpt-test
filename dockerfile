FROM nginx:latest

# Copy the static HTML file into the default NGINX directory
COPY index.html /usr/share/nginx/html/index.html

# Expose port 80 for HTTP traffic
EXPOSE 80
