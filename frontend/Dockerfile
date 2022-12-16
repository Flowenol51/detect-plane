FROM node:17-alpine
WORKDIR /frontend
COPY package*.json /frontend/

RUN npm i --silent
RUN npm i -g react-scripts@5.0.1

CMD ["npm", "start"]