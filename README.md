# Personal Site

[![pre-commit](https://github.com/jteppinette/personal-site/actions/workflows/pre-commit.yml/badge.svg?branch=master)](https://github.com/jteppinette/personal-site/actions/workflows/pre-commit.yml)

## Development

### Required Software

Refer to the links provided below to install these development dependencies:

- [direnv](https://direnv.net)
- [git](https://git-scm.com/)
- [pyenv](https://github.com/pyenv/pyenv#installation)

### Getting Started

Notice, we are restricted to Python <= 3.7.12 due to Cloudflare Pages.

**Setup**

```sh
$ pyenv install 3.7.12
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
