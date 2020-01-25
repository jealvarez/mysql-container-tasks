# **MySQL Container Tasks**

Dump a database to sql file.

## **Prerequisites**

* Docker

## **How to use it?**

* Building the image

```sh
docker build -t mysql-container-tasks .
```

* Getting container options

```sh
docker run --rm --name mysql-container-tasks mysql-container-tasks --help
```

* Dump database to sql file

```sh
docker run --rm --name mysql-container-tasks -v ${PWD}/data:/opt/apps/data mysql-container-tasks --host {HOST_IP} --user {USER} --password {PASSWORD} --database {DATABASE}
```
