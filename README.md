# bottec admin panel


### Docker run
```commandline
--no-cache

docker build --progress=plain  -t admin_panel . && \
docker run -it admin_panel
```

### Run local
```commandline
pyenv local 3.11.0
python -m venv .venv
source .venv/bin/activate
```