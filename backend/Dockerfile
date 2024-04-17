FROM node:19.0.0-slim
WORKDIR /app
COPY ./package.json ./
COPY prisma ./prisma/
RUN npm cache clean --force
RUN npm i
RUN npx prisma generate
COPY . .
COPY .env ./.env
EXPOSE 9000
CMD ["npm", "run", "start"]