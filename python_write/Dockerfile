FROM python:latest

ADD test.py ./
ADD infofile.py ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uproot awkward 

RUN pip install --no-cache-dir vector
RUN pip install --no-cache-dir matplotlib


CMD [ "python", "./test.py"]
