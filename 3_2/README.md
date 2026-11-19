# Docker Quick Reference

A small Python web application displaying useful Docker commands. Built for
exercise 1.15; it uses the Python standard library without external packages.

## Build and run locally

Run these commands from this directory:

```sh
docker build -t docker-quick-reference .
docker run --rm -p 127.0.0.1:8090:8080 docker-quick-reference
```

Open http://localhost:8090 to view the reference. GET /health returns
`{"status": "ok"}`. The server listens on container port 8080 and runs as
an unprivileged user.

## Cloud deployment pipeline (exercise 3.2)

The application is deployed at https://docker-quick-reference.onrender.com.
The GitHub Actions workflow in `.github/workflows/deploy-render.yml` builds
and pushes `jhlow0106/docker-quick-reference:latest` on each push to main,
then calls the Render service deploy hook stored as `RENDER_DEPLOY_HOOK`.
`DOCKER_HUB` stores the Docker Hub access token. Render pulls the updated
image after the hook is called; the hook itself is never committed.
