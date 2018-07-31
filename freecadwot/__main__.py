#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Console script for freecadwot."""

import os
import click


@click.command()
def main(args=None):
    """Console script for freecadwot."""

    # Django specific settings
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "freecadwot.djangodb.settings")
    import django
    django.setup()

    from .freecadwot import Application

    app = Application()
    app.exec_()


if __name__ == "__main__":
    main()
