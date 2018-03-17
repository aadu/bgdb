.PHONY: lint format ls kill

lint:
	pylint bgdb

ls:
	find bgdb -name migrations -prune -o -name front_end -prune -o -type f -name '*.py' -print

format:
	find bgdb -name migrations -prune -o -name front_end -prune -o -type f -name '*.py' -print | xargs -I {} bash -c 'isort {}; yapf --style setup.cfg -i {};'

kill:
	ps aux | grep scrapy | grep -v grep | awk '{print $2}' | xargs -I '{}' bash -c 'kill -9 {};'