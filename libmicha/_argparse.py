import argparse
from typing import Optional, Tuple


class Cli:
    _cli: dict[Tuple[str, str], str]

    @classmethod
    @property
    def cliobjects(cls):
        return cls._cli


def climethod(command, *args):
    class decorator:  # https://stackoverflow.com/a/54316392
        def __init__(self, fn):
            self.fn = fn

        def __set_name__(self, owner, name):
            if getattr(owner, "_cli", None) is None:
                setattr(owner, "_cli", {})
            owner._cli[(command, *args)] = self.fn.__name__
            setattr(owner, name, self.fn)

    return decorator


class StoreDict(argparse.Action):
    """Argparse action used to store arguments in the for key=value in a dict.
    >>> parser.add_argument("key_value", action=libmicha.StoreDict, type=str, nargs="*", default={})
    Inspired by https://gist.github.com/fralau/061a4f6c13251367ef1d9a9a99fb3e8d
    """

    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Optional[str],
        option_string: str | None = None,
    ) -> None:
        dest = getattr(namespace, self.dest)
        if values:
            for value in values:
                k, v = value.split("=", 1)
                k = k.strip()
                dest[k] = v
        setattr(namespace, self.dest, dest)
