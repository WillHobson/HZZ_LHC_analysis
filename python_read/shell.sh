
docker image build -t python_read .
docker run --rm -v storage:/storage python_read
