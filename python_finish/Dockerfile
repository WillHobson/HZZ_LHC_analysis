FROM python:latest
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir uproot awkward 

RUN pip install --no-cache-dir vector
RUN pip install --no-cache-dir matplotlib
ADD test_finish.py .

CMD [ "python", "./test_finish.py"]
