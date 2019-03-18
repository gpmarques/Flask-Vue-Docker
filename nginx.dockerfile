FROM node as build-stage

COPY ./client /client
WORKDIR client

RUN npm install
RUN npm run build

FROM nginx

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build-stage /client/dist/ app/