import json

import click

from .export import request_listens, request_playing_now


@click.group()
def main() -> None:
    pass


@main.command()
@click.argument("LISTENBRAINZ_USERNAME")
def playing_now(listenbrainz_username: str) -> None:
    """
    Downloads your currently playing track from listenbrainz
    """
    data = request_playing_now(username=listenbrainz_username)
    click.echo(json.dumps(data))
    exit(0 if len(data) else 1)


@main.command()
@click.option(
    "-p",
    "--pages",
    type=int,
    default=None,
    help="Request these many pages of your history",
)
@click.option(
    "--days",
    type=int,
    default=None,
    help="Request listens no older than this many days",
)
@click.argument("LISTENBRAINZ_USERNAME")
def export(
    pages: int | None, days: int | None, listenbrainz_username: str
) -> None:
    """
    Downloads all scrobbles for your listenbrainz account
    """
    click.echo(
        json.dumps(
            request_listens(username=listenbrainz_username, pages=pages, days=days)
        )
    )


if __name__ == "__main__":
    main(prog_name="listenbrainz_export")
