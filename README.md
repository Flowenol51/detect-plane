# detect-plane

# For backend python https://fastapi.tiangolo.com/
pip3 install fastapi
pip3 install "uvicorn"

# Build the docker image
docker load -i aircraftdetector.tar
docker run aircraftdetector:1.0.0

# Launch the backend server
cd backend
uvicorn main:app --reload

# Frontend
cd frontend 
npm i axios
npm start
