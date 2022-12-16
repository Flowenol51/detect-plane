# detect-plane

# Backend API
I used Flask because its a popular and deemed the best API for python backend.  

# Build and run the docker image
docker load -i aircraftdetector.tar  
docker run aircraftdetector:1.0.0  

# Start Backend Server
cd backend  
docker build . -t backend

# Start Frontend Server
cd frontend   
docker build . -t frontend 