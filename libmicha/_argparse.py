import argparse
from typing import Optional


# https://gist.github.com/fralau/061a4f6c13251367ef1d9a9a99fb3e8d
class StoreDict(argparse.Action):
    """Argparse action used to store arguments in the for key=value in a dict.
    >>> parser.add_argument("key_value", action=store_dict, type=str, nargs="*", default={})
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
