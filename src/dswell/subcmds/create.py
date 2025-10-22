import os
from pathlib import Path
from datetime import datetime

import click

from ..daemon import start_daemon
from ..logger import logger
from ..utils import format_time, parse_time, parse_duration


@click.command()
@click.argument("path", type=click.Path(exists=True))
@click.argument("time")
def create(path: str, time: str) -> None:
    """Schedule a file or directory for deletion."""
    try:
        delta = parse_duration(time)
        scheduled_time = datetime.now() + delta
        full_path = os.path.abspath(path)
        start_daemon(full_path, scheduled_time)
        click.echo(f"Scheduled '{full_path}' for deletion in {time}.")
    except ValueError as e:
        logger.error(f"Invalid time format: {e}")
        # Ensure a non-zero exit code and proper Click error handling
        raise click.ClickException(str(e)) from e
    except Exception as e:
        click.echo(f"An unexpected error occurred: {e}", err=True)
