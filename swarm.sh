cd python_write
docker image build -t python_write .
docker volume create storage
docker run --rm -v storage:/storage python_write

cd ..
docker swarm init
#add nodes
docker stack deploy -c docker-compose.yaml my_stack6
#implement logic to wait for result
docker image build -t my-nginx-image-1 .
docker run --name my-nginx-2 -d my-nginx-image-1
