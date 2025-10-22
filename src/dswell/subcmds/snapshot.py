import shutil
from datetime import datetime
from pathlib import Path

import click


@click.command()
def snapshot() -> None:
    """Create a zip archive of the .dswell directory for debugging."""
    dswell_path = Path.home() / ".dswell"
    if not dswell_path.exists():
        click.echo("No .dswell directory found. Nothing to snapshot.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_name = f"dswell_snapshot_{timestamp}"
    # Place snapshot on the Desktop for easy access
    desktop_path = Path.home() / "Desktop"
    archive_path = desktop_path / snapshot_name

    try:
        shutil.make_archive(str(archive_path), "zip", str(dswell_path))
        click.echo(f"Successfully created snapshot: {archive_path}.zip")
    except Exception as e:
        click.echo(f"Failed to create snapshot: {e}", err=True)