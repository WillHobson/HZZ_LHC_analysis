# HZZ_LHC_analysis
A containerised version of the HZZ analysis using LHC's open data. Implemented in Docker.

To run on a single node:

git clone https://github.com/WillHobson/HZZ_LHC_analysis

cd HZZ_LHC_analysis

sh shellcomp.sh

This proves the concept of scalibilty. A docker-compose-forswarm.yaml is included which is an adapted version of docker-compose.yaml which enables the compose file to be run as a swarm. This is executed by running sh swarm.sh. Note this is speculative and needs further development, perhaps if multiple nodes were available, this would be eaier to debug. This shows that a compose file can be run on a distributed computing system.

NOTE: the commands executed in the shell script are intended for use on a linux based system 
may need adapting for a windows machine

....wait... analysis can take up to 5 minutes althought the variable fraction = 0.5 in python_read/test.py should half this.
This means the output is not the same as shown in original analysis. The correct graph can be obtainer by setting this parameter to 1.

The terminal will display where the output webpage is hosted.
eg. output displayed at localhost:XXXXX

copy and paste the address into a browser to see result.

There should always be one write and one finish container, the analysis (read) container can be multiplied using the replicas parameter in docker compose
(currently set to 4)
