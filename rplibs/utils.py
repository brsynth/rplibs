from argparse import (
    ArgumentParser,
    Namespace
)
from logging import Logger
from colored import fg, bg, attr
from brs_utils import create_logger


def init(
    parser: ArgumentParser,
    args: Namespace,
    version: str
) -> Logger:
    if args.log.lower() in ['silent', 'quiet'] or args.silent:
        args.log = 'CRITICAL'

    # Create logger
    logger = create_logger(parser.prog, args.log)

    logger.info(
        '{color}{typo}{prog} {version}{rst}{color}{rst}\n'.format(
            prog = logger.name,
            version = version,
            color=fg('white'),
            typo=attr('bold'),
            rst=attr('reset')
        )
    )
    logger.debug(args)

    return logger
