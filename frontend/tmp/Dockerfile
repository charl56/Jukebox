# # build stage
# FROM node:lts-alpine as build-stage
# WORKDIR /app
# COPY package*.json ./
# # install project dependencies
# RUN npm install

# # Copy the project files
# COPY public/ ./public
# COPY src/ ./src
# COPY babel.config.js ./
# COPY vue.config.js ./

# RUN npm run build

# # production stage
# FROM nginx:stable-alpine as production-stage
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# # EXPOSE 8080
# CMD ["nginx", "-g", "daemon off;"]





#####
##### Docker multi-stage build : Node.js build image
#####
FROM node:18-alpine as build-stage
WORKDIR /app

# Copy project files and restore as distinct layers
COPY package.json ./
COPY package-lock.json ./

# Restore npm packages using custom .npmrc file and base64 encoded PAT`
RUN apk update && \
    apk add --no-cache --virtual .gyp \
    python3 \
    make \
    g++ 

# Copy everything else for build
COPY public/ ./public
COPY src/ ./src
COPY babel.config.js ./
COPY vue.config.js ./

RUN export NODE_ENV=production 
RUN export VUE_APP_BASE_PATH='/' 

RUN rm -rf node_modules
RUN rm -f package-lock.json

RUN yarn cache clean

RUN yarn global add @vue/cli
RUN yarn global upgrade --latest @vue/cli

RUN chmod -R 777 /app

RUN npm install
RUN npm run build

#####
##### Docker multi-stage build : runtime image using nginx as web server
#####
FROM nginx:1.21.0-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
# COPY Docker/front-entrypoint.sh .
# RUN chmod +x ./front-entrypoint.sh
#EXPOSE 8082
CMD ["nginx", "-g", "daemon off;"]
# ENTRYPOINT ["./front-entrypoint.sh"]