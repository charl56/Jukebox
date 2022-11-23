
# Docker 

## Start docker-compose
### Start by create image of backend and frontend
```
README.MD in frontend and flask folder
```
### Launch docker compose
```
docker-compose up -d
with '-d' to don't see logs
```
#
## Commit and push
### Launch docker compose
```
docker-compose up -d
with '-d' to don't see logs
```
### Get container ID
```
docker ps
```
### Commit 
```
docker commit "CONTAINER ID" name-repository/image-name:tag
ex : docker commit 0ab20a7cbfd2 charl56/muse-discovery:frontend
```
### Push
```
docker push name-repository/image-name:tag
ex : docker push charl56/muse-discovery:frontend    
```
#
##  Pull
```
docker pull name-repository/image-name:tag
ex : docker pull charl56/muse-discovery:frontend    
```