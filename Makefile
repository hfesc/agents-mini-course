# .PHONY: default

docker-build:
	docker-compose up --build -d

docker-down:
	docker-compose down

docker-start:
	docker start agents-mini-course
	docker exec -it agents-mini-course /bin/bash
