FROM node:19.0.0-slim
WORKDIR /app
COPY ./package.json ./
RUN npm i
COPY . .
EXPOSE 9000
CMD ["npm", "run", "start"]
