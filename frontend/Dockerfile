## Stage 1: Build stage
FROM node:18-alpine AS build
WORKDIR /build
COPY package*.json ./
RUN npm install
COPY . ./
RUN npm run build
#
## Stage 2: Production stage
FROM nginx:alpine AS production
COPY --from=build /build/build /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
#
#
## Use the latest LTS version of Node.js
#FROM node:18-alpine
#
## Set the working directory inside the container
#WORKDIR /app
#
## Copy package.json and package-lock.json
#COPY package*.json ./
#
## Install dependencies
#RUN npm install
#
## Copy the rest of your application files
#COPY . .
#
## Expose the port your app runs on
#EXPOSE 3000
#
## Define the command to run your app
#CMD ["npm", "start"]