.PHONY: lint format ls

lint:
	pylint bgdb

ls:
	find bgdb -name migrations -prune -o -name front_end -prune -o -type f -name '*.py' -print

format:
	find bgdb -name migrations -prune -o -name front_end -prune -o -type f -name '*.py' -print | xargs -I {} bash -c 'isort {}; yapf --style setup.cfg -i {};'