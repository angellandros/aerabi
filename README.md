# Aerabi
My HTML Homepage

## Run
```bash
$ nohup gunicorn --workers 3 --bind unix:/root/aerabi/gunicorn.sock aerabi.wsgi:application &
```
