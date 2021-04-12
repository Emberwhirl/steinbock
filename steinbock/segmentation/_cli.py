import click

from steinbock.segmentation.cellprofiler._cli import cellprofiler_cmd
from steinbock.utils import cli


@click.group(
    cls=cli.OrderedClickGroup,
    help="Perform cell segmentation to create cell masks",
)
def segment():
    pass


segment.add_command(cellprofiler_cmd)
