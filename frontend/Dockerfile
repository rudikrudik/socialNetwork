# Stage 1: Build stage
FROM node:18-alpine AS build
WORKDIR /build
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build

# Stage 2: Production stage
FROM nginx:alpine AS production
COPY --from=build /build/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]