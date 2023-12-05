#image to build webpage
FROM nginx
#add html file to web container
ADD index.html .
#add produced image to output
ADD finaloutput.png .
#copy html and image files to container
COPY index.html /usr/share/nginx/html
COPY finaloutput.png /usr/share/nginx/html


