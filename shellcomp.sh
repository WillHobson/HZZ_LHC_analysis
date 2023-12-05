#run the docker-compose file and build all images
docker-compose up -d --build python_write python_read python_finish --remove-orphans
sleep 30
#making a temporary container to move the final output to a local directory
docker run --rm -v hzz_analysis_storage:/data -v $(pwd):/target busybox cp /data/finaloutput.png /target/ 



#copy the final output into the web folder to be used
cp finaloutput.png web/finaloutput.png

#remove final output
rm finaloutput.png

#move to web folder
cd web

#build webpage image
docker image build -t my-nginx-image-1 .

#run webpage container
docker run --name my-nginx-2 -P -d my-nginx-image-1

#name of webpage container
container_name="my-nginx-2"

# Get the container's port information
port_info=$(docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}}{{(index $conf 0).HostPort}}{{end}}' "$container_name")

#output to terminal the localhost address where the final output is accessible
if [ -n "$port_info" ]; then
    echo "The output is available at localhost:$port_info"
else
    echo "Container $container_name is not running or port information is not available."
fi