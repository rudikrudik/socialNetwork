# Stage 1: Build stage
FROM node:18-alpine as BUILD
WORKDIR /build
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build

# Stage 2: Production stage
FROM nginx:alpine AS PRODUCTION
COPY --from=BUILD /build/build /usr/share/nginx/html
EXPOSE 3000
CMD ["nginx", "-g", "daemon off;"]