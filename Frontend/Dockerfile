# Frontend/Dockerfile
FROM node:20-alpine

WORKDIR /app

# Copy config and source files
COPY package*.json ./
COPY vite.config.js ./
RUN npm install

# Run npm audit fix (safe mode first)
RUN npm audit fix || true

# (Optional but forceful fix)
RUN npm audit fix --force || true

# Copy the source files after installing
COPY src/ ./src

EXPOSE 5173

CMD ["npm", "run", "dev"]
