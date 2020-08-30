up:
	@docker build -t nnp:latest .
	@docker run -t --name nnp -d nnp:latest

install:
	@docker exec -it nnp python setup.py sdist
	@docker exec -it nnp bash -c "pip install /home/nnp/dist/*.gz"
	@docker exec -it nnp bash -c "rm -rf /home/nnp/*	"

run:
	@docker exec -it nnp interpreter

down:
	@docker stop nnp
	@docker rm nnp

tests:
	@coverage run -m unittest discover
	@coverage report

.PHONY: up install run down tests

