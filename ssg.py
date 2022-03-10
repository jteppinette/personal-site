#!/usr/bin/env python3

import os
import sys
from distutils.dir_util import copy_tree
from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Process
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader
from markdown import markdown
from watchgod import watch
from watchgod.watcher import AllWatcher, Change

theme = Environment(loader=FileSystemLoader(Path("theme")))

LISTEN_PORT = 8000
LISTEN_ADDRESS = "0.0.0.0"

MD_EXTENSIONS = ["nl2br"]

SITE_TITLE = "Joshua Taylor Eppinette"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory="dist", **kwargs)


class Watcher(AllWatcher):
    def check(self):
        changes = set()
        new = {}

        for directory in ("pages", "static", "theme"):
            try:
                self._walk(Path(directory), changes, new)
            except OSError:
                pass

        deleted = self.files.keys() - new.keys()
        if deleted:
            changes |= {(Change.deleted, entry) for entry in deleted}

        self.files = new

        return changes


def context(content):
    return dict(content=content, title=SITE_TITLE)


def build():
    copy_tree("static", "dist")

    template = theme.get_template("base.jinja")

    with Path("pages", "home.md").open() as file:
        content = markdown(file.read(), extensions=MD_EXTENSIONS)

    with Path("dist", "index.html").open("w") as file:
        file.write(template.render(**context(content)))

    print("built")


def serve(address, port):
    try:
        with HTTPServer((address, port), Handler) as server:
            print("serving at port", port)
            server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)


@click.command()
@click.option("--listen/--no-listen", default=False)
def cli(listen):
    build()

    if not listen:
        return

    Process(target=serve, args=(LISTEN_ADDRESS, LISTEN_PORT)).start()

    for changes in watch(os.getcwd(), watcher_cls=Watcher):
        build()


if __name__ == "__main__":
    cli()
