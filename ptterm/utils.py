"""
Some utilities.
"""
from __future__ import unicode_literals
import getpass
import os

__all__ = (
    'get_default_shell',
)


def get_default_shell():
    """
    return the path to the default shell for the current user.
    """
    import pwd  # XXX: Posix only.
    if 'SHELL' in os.environ:
        return os.environ['SHELL']
    else:
        username = getpass.getuser()
        shell = pwd.getpwnam(username).pw_shell
        return shell
