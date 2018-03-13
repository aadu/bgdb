FROM node:9-alpine
RUN mkdir -p /code
WORKDIR /code
ADD . /code

RUN yarn
CMD [ "yarn", "run", "dev" ]
EXPOSE 8080
