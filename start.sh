#!/bin/sh
python -c 'import db_manager; db_manager.update()'
exec gunicorn -b :5000 -w 4 --access-logfile - --error-logfile - run:app