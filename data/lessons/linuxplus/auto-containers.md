# Containers with Podman & Docker

Containers package an application with everything it needs to run, so it behaves
the same on a laptop, a server, or in the cloud. Linux+ expects you to understand
what a container *is*, how it differs from a virtual machine, and the everyday
commands of the two dominant engines, **Docker** and **Podman**.

## Containers vs. virtual machines

Both isolate workloads, but at different layers:

| | Virtual machine | Container |
|--|-----------------|-----------|
| Virtualizes | Hardware, via a hypervisor | The operating system |
| Kernel | Each VM has its own full OS + kernel | All share the **host's** kernel |
| Size / startup | Gigabytes, boots in seconds-to-minutes | Megabytes, starts in a fraction of a second |
| Isolation | Strong (separate kernels) | Lighter (process-level) |

A container is really just **isolated host processes**. The Linux kernel provides
the isolation using **namespaces** (each container gets its own view of
processes, network, mounts and users) and **cgroups** (which cap how much CPU,
memory and I/O it may consume). Because there is no second kernel to boot,
containers are far lighter than VMs.

## Images and containers

Two terms you must not confuse:

- An **image** is a read-only template — the packaged filesystem and metadata,
  built in stacked **layers**. Images follow the **OCI** (Open Container
  Initiative) standard, so they are portable across engines.
- A **container** is a running (or stopped) *instance* of an image, with a thin
  writable layer on top.

Images are stored in **registries** such as Docker Hub. You reference them as
`name:tag`, e.g. `nginx:1.27` (the tag defaults to `latest` if omitted).

## Two engines: Docker and Podman

**Docker** uses a central background **daemon, `dockerd`**, that runs as **root**.
The `docker` CLI sends requests to it over a socket, and the daemon (via
`containerd` and the `runc` runtime) does the work. A practical security
consequence: anyone in the `docker` group can control that root daemon and so is
effectively root.

**Podman** is **daemonless** — each command is an ordinary process that does its
job and exits, with no always-running root service. It is **rootless** by default,
so containers run as your unprivileged user. Its CLI is deliberately a **drop-in
replacement** for Docker's (many people `alias docker=podman`), and it builds
images with **Buildah** under the hood.

> For the exam, anchor on two phrases: **Docker is daemon-based and runs as root;
> Podman is daemonless and rootless.** That single distinction explains most of
> Podman's security appeal.

## Everyday commands

The verbs are the same for both engines (substitute `docker` or `podman`):

```
$ podman pull nginx:1.27            # download an image from a registry
$ podman images                     # list local images
$ podman run -d --name web \
      -p 8080:80 nginx:1.27          # run detached, publish host 8080 -> container 80
$ podman ps                         # running containers
$ podman ps -a                      # include stopped ones
$ podman logs web                   # view a container's output
$ podman exec -it web bash          # open an interactive shell inside it
$ podman stop web && podman rm web  # stop, then remove the container
$ podman rmi nginx:1.27             # remove the image
```

Useful `run` flags: **`-d`** detached (background), **`-p host:container`**
publish a port, **`-e KEY=val`** set an environment variable, **`-v`** mount a
volume, **`-it`** interactive terminal, **`--name`** a friendly name.

## Persisting data

A container's writable layer is **ephemeral** — delete the container and its
changes are gone. To keep data, attach storage:

- A **volume** is managed storage: `-v mydata:/var/lib/mysql`.
- A **bind mount** maps a host directory in: `-v /srv/html:/usr/share/nginx/html`.

Anything that must outlive the container (databases, uploads) belongs on a volume
or bind mount, never in the container layer.

## Building images

You describe an image in a **Dockerfile** (Podman also calls it a
**Containerfile**) — the same syntax works for both:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]
```

Key instructions: **`FROM`** (base image), **`RUN`** (execute a build step),
**`COPY`** (add files), **`EXPOSE`** (document a port), and **`CMD`**/
**`ENTRYPOINT`** (the default process). Build it:

```
$ podman build -t myapp:1.0 .
```

## Multi-container apps

Real applications bundle several containers (web + database + cache). A **Compose**
file (`compose.yaml`) declares them all, and `docker compose up` / `podman compose
up` starts the set together. Podman additionally groups containers into a **pod**
— containers that share a network namespace, the same concept Kubernetes uses.

## Exam focus

- Containers share the **host kernel** and are isolated by **namespaces** +
  **cgroups**; VMs virtualize hardware via a hypervisor and each carry a full OS.
  Containers are lighter and start faster.
- An **image** is a read-only, layered, OCI-standard template; a **container** is
  a running instance. Images come from **registries** (Docker Hub) and are named
  `image:tag` (default `latest`).
- **Docker = daemon (`dockerd`) running as root**; the `docker` group ≈ root.
  **Podman = daemonless and rootless**, with a Docker-compatible CLI and Buildah
  for builds.
- Core verbs (same for both): `pull`, `images`, `run`, `ps`/`ps -a`, `logs`,
  `exec -it`, `stop`, `rm`, `rmi`. Key `run` flags: `-d`, `-p host:container`,
  `-e`, `-v`, `-it`, `--name`.
- Container storage is **ephemeral**; persist data with **volumes** or **bind
  mounts** (`-v`).
- Build images from a **Dockerfile/Containerfile** (`FROM`, `RUN`, `COPY`,
  `EXPOSE`, `CMD`) via `build -t`. **Compose** runs multi-container apps; Podman
  **pods** share a network namespace like Kubernetes.
