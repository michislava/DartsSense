# Build stage
FROM node:lts-alpine as build-stage

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application source code
COPY . .

# Build the Vue.js application
RUN npm run build

# Production stage
FROM nginx:stable-alpine as production-stage

# Copy the built Vue.js application from the build stage to the Nginx directory
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Copy the Nginx configuration file from the host to the container
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
