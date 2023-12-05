
docker image build -t python_write .
docker run --rm -v storage:/storage python_write
