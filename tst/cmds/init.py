import click


@click.command("init", short_help="Create or migrate the configuration")
@click.option(
    "--create-certs",
    "-c",
    default=None,
    help="Create new SSL certificates based on CA in [directory]",
    type=click.Path(),
)
@click.pass_context
def init_cmd(ctx: click.Context, create_certs: str):
    """
    Create a new configuration or migrate from previous versions to current

    \b
    Follow these steps to create new certificates for a remote harvester:
    - Make a copy of your Farming Machine CA directory: ~/.tst/[version]/config/ssl/ca
    - Shut down all tst daemon processes with `tst stop all -d`
    - Run `tst init -c [directory]` on your remote harvester,
      where [directory] is the the copy of your Farming Machine CA directory
    - Get more details on remote harvester on Tst wiki:
      https://github.com/Tst-Network/tst-blockchain/wiki/Farming-on-many-machines
    """
    from pathlib import Path
    from .init_funcs import init

    init(Path(create_certs) if create_certs is not None else None, ctx.obj["root_path"])


if __name__ == "__main__":
    from .init_funcs import tst_init
    from tst.util.default_root import DEFAULT_ROOT_PATH

    tst_init(DEFAULT_ROOT_PATH)
