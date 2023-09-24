FROM node    //node is an image which is available in docker hub.

WORKDIR /app

COPY . /app

RUN npm install

EXPOSE 80

CMD [ "node","server.js" ]