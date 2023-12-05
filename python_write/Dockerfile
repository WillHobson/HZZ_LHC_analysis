FROM python:latest

ADD test.py ./
ADD infofile.py ./

#install necessary packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uproot awkward 

RUN pip install --no-cache-dir vector
RUN pip install --no-cache-dir matplotlib

#command to execute python script
CMD [ "python", "./test.py"]
