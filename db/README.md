# Download mysql docker image
```
docker run --name some-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql
```

# Build Docker image
```
docker build -t jukebox:database .
```