up:
	docker-compose up -d
.PHONY: up

down:
	docker-compose down
.PHONY: down

make s3-web:
	open http://localhost:9000
.PHONY: s3-web