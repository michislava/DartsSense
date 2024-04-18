FROM node:19.0.0-slim
WORKDIR /app
COPY ./package.json ./
COPY prisma ./prisma/
RUN npm cache clean --force
RUN npm i
RUN npx prisma generate
COPY . .
ENV DATABASE_URL="mysql://root:1856@34.172.223.188:3306/darts"
EXPOSE 9000
CMD ["npm", "run", "start"]

