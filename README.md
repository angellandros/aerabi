# Aerabi
My HTML Homepage

## Run

Run the database proxy:

```bash
$ wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
$ sudo chmod +x cload_sql_proxy
$ ./cloud_sql_proxy -instances=aerabi:europe-west3:aerabi-db=tcp:3306
```

Run the Django app:

```bash
$ ./manage.py runserver 8080
```

## GCloud Deploy

```bash
$ gcloud app deploy app.yaml --project=aerabi
```

## Gunicorn Deploy
```bash
$ nohup gunicorn --workers 3 --bind unix:/root/aerabi/gunicorn.sock aerabi.wsgi:application &
```
