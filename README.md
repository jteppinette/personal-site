# Personal Site

[![pre-commit](https://github.com/josheppinette/personal-site/actions/workflows/pre-commit.yml/badge.svg?branch=master)](https://github.com/josheppinette/personal-site/actions/workflows/pre-commit.yml)

## Development

### Required Software

Refer to the links provided below to install these development dependencies:

- [nix](https://zero-to-nix.com/start/install/)
- [direnv](https://direnv.net)
- [git](https://git-scm.com/)

### Getting Started

**Setup**

```sh
$ direnv allow
$ pip install -r requirements/dev.txt
$ pre-commit install
```

**Build**

```sh
$ ./ssg.py
```

**Watch and Listen**

```
$ ./ssg.py --listen
```
