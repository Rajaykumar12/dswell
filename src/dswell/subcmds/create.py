import os
from pathlib import Path

import click

from ..daemon import start_daemon
from ..logger import logger
from ..utils import format_time, parse_time


def touch_file(filepath):
    """Create an empty file if it doesn't exist."""
    Path(filepath).touch()


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.argument("time")
def create(path: str, time: str) -> None:
    """Schedule a file or directory for deletion."""
    try:
        deletion_seconds = parse_time(time)
        full_path = os.path.abspath(path)
        start_daemon(full_path, deletion_seconds)
        click.echo(f"Scheduled '{full_path}' for deletion in {time}.")
    except ValueError as e:
        click.echo(f"Error: {e}", err=True)
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}", err=True)
