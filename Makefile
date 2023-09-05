.PHONY: db-up
db-up:
	docker-compose -f docker-compose-db.yml up -d

.PHONY: db-down
db-down:
	docker-compose -f docker-compose-db.yml down