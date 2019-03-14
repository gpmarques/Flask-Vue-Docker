FROM node

RUN npm install --quiet --global vue-cli
RUN npm install axios
RUN npm install bootstrap
RUN npm install bootstrap-vue

RUN mkdir ./client
WORKDIR ./client