FROM node:19.0.0-slim
WORKDIR /app
COPY ./package.json ./
COPY prisma ./prisma/
RUN npm cache clean --force
RUN npm i
RUN npm prisma generate
COPY . .
EXPOSE 9000
CMD ["npm", "run", "start"]
