# Ares Application - Docker Setup

## Overview

This application consists of a Flask backend and an Express frontend, both containerized using Docker.

## Architecture

- **Backend**: Flask API running on port 9000
- **Frontend**: Express/EJS server running on port 3000
- **Network**: Custom Docker network (`ares-network`) for container communication

## Quick Start

### Option 1: Using Docker Compose (Recommended)

```bash
# Build the images first (if not already built)
docker build -t areas-backend -f dockerfile-backend .
docker build -t areas-frontend -f dockerfile-frontend .

# Start both containers
docker-compose up -d

# Stop containers
docker-compose down
```

### Option 2: Manual Docker Commands

```bash
# Create network
docker network create ares-network

# Run backend
docker run -d -p 9000:9000 --name backend-container --network ares-network areas-backend

# Run frontend
docker run -d -p 3000:3000 --name frontend-container --network ares-network -e BACKEND_URL=http://backend-container:9000/api areas-frontend
```

## Building Images

### Backend

```bash
docker build -t areas-backend -f dockerfile-backend .
```

### Frontend

```bash
docker build -t areas-frontend -f dockerfile-frontend .
```

## Accessing the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:9000/api

## Useful Commands

### View logs

```bash
docker logs frontend-container
docker logs backend-container
```

### Stop containers

```bash
docker stop frontend-container backend-container
```

### Remove containers

```bash
docker rm frontend-container backend-container
```

### Check running containers

```bash
docker ps
```

## Troubleshooting

### Frontend can't connect to backend

- Ensure both containers are on the same network (`ares-network`)
- Verify the `BACKEND_URL` environment variable is set correctly
- Check backend logs: `docker logs backend-container`

### Port conflicts

If ports 3000 or 9000 are already in use, you can map to different ports:

```bash
docker run -d -p 8080:3000 --name frontend-container --network ares-network -e BACKEND_URL=http://backend-container:9000/api areas-frontend
```

## Development

For local development without Docker, see the individual README files in `/backend` and `/frontend` directories.
