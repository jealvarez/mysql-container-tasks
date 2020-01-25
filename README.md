# **MySQL Container Task**

Dump a database to sql file.

## **Prerequisites**

* Docker

## **How to use it?**

* Building the image

```sh
docker build -t mysql-task .
```

* Getting container options

```sh
docker run --rm --name mysql-task mysql-task --help
```

* Dump database to sql file

```sh
docker run --rm --name mysql-task -v ${PWD}/data:/opt/apps/data mysql-task --host {HOST_IP} --user {USER} --password {PASSWORD} --database {DATABASE}
```
