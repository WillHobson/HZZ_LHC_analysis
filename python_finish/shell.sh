
docker image build -t python_finish .
docker run --rm -v storage:/storage python_finish
