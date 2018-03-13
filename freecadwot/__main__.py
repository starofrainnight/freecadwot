#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Console script for freecadwot."""

from .freecadwot import Application

import click


@click.command()
def main(args=None):
    """Console script for freecadwot."""

    app = Application()
    app.exec_()

if __name__ == "__main__":
    main()
