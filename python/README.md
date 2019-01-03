### Build image
```
docker build -t bot:latest .
```

### Run container
```
MOTION_ROOT=/data/motion

docker run -d --restart=unless-stopped -e TOKEN=$(cat token) -v ${MOTION_ROOT}:/data/motion:rw bot:latest
```
