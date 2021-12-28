import argparse
import sys
import tarfile
import tempfile
from pathlib import Path


def cli(argv=None):
    parser = argparse.ArgumentParser(
        description=("Matplotx"),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=_get_version_text(),
        help="display version information",
    )

    subparsers = parser.add_subparsers(title="subcommands", required=True)

    parser_spy = subparsers.add_parser("spy", help="Show sparsity pattern of matrix")
    _add_arguments_spy(parser_spy)
    parser_spy.set_defaults(
        func=lambda args: cli_spy(
            args.infile,
            args.outfile,
            args.border_width,
            args.border_color,
            args.colormap,
        )
    )

    args = parser.parse_args(argv)

    return args.func(args)


def _get_version_text():
    from .__about__ import __version__

    pmaj = sys.version_info.major
    pmin = sys.version_info.minor
    pmic = sys.version_info.micro

    return "\n".join(
        [
            f"matplotx {__version__} [Python {pmaj}.{pmin}.{pmic}]",
            "Copyright (c) 2021 Nico Schlömer <nico.schloemer@gmail.com>",
        ]
    )


def _read_spmatrix(filename):
    import scipy.io

    return {".mtx": scipy.io.mmread, ".mm": scipy.io.mmread, ".rb": scipy.io.hb_read}[
        filename.suffix
    ](filename)


def cli_spy(
    infile,
    outfile,
    border_width,
    border_color,
    colormap,
):
    from ._spy import spy

    if infile.suffixes == [".tar", ".gz"]:
        with tarfile.open(infile, "r:gz") as tar:
            A = None
            for m in tar.getmembers():
                if Path(m.name).suffix in [".mtx", ".rb"]:
                    with tempfile.TemporaryDirectory() as tmpdir:
                        tar.extract(m, path=tmpdir)
                        filename = Path(tmpdir) / Path(m.name)
                        A = _read_spmatrix(filename)
                    break
            assert A is not None, f"Couldn't find matrix file in {infile}."
    else:
        A = _read_spmatrix(infile)

    if outfile is None:
        plt = spy(A, border_width, border_color, colormap)
        plt.show()
    else:
        spy(A, border_width, border_color, colormap, filename=outfile)


def _add_arguments_spy(parser):
    parser.add_argument("infile", type=Path, help="input matrix market file")

    parser.add_argument(
        "outfile", type=str, nargs="?", default=None, help="output png file (optional)"
    )

    parser.add_argument(
        "--border-width",
        "-w",
        required=False,
        type=int,
        default=0,
        help="border width (default: 0)",
    )

    parser.add_argument(
        "--border-color",
        "-b",
        required=False,
        type=str,
        default="0.5",
        help="border color (default: 0.5, gray)",
    )

    parser.add_argument(
        "--colormap",
        "-c",
        required=False,
        type=str,
        default=None,
        help="border color (default: 0.5, gray)",
    )
