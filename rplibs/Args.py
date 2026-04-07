from argparse import ArgumentParser
from rplibs._version import __version__
from brs_utils import add_logger_args


def build_args_parser(
    prog: str, description: str = "", epilog: str = "", m_add_args=None
) -> ArgumentParser:

    parser = ArgumentParser(prog=prog, description=description, epilog=epilog)

    # Build Parser with rptools common arguments
    if m_add_args:
        parser = m_add_args(parser)
    parser = add_arguments(parser)

    return parser


def add_arguments(parser: ArgumentParser) -> ArgumentParser:
    # Add arguments related to the logger
    parser = add_logger_args(parser)

    # parser.add_argument(
    #     "--pathways",
    #     required=True,
    #     type=str,
    #     nargs="+",
    #     help="Pathways (rpSBML) to make statistics on",
    # )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s {}".format(__version__),
        help="show the version number and exit",
    )

    return parser
