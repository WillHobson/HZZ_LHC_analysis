FROM python:latest

#install required python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uproot awkward 

RUN pip install --no-cache-dir vector
RUN pip install --no-cache-dir matplotlib

ADD test.py .
ADD infofile.py .
CMD [ "python", "./test.py"]
