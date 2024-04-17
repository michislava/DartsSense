FROM node:19.0.0-slim
WORKDIR /app
COPY ./package.json ./
RUN npm i
RUN npx prisma generate
COPY . .
CMD ["npm", "run", "start"]
