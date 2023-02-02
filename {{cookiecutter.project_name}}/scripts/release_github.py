"""Release GitHub."""
import pathlib
import re
import sys
import tomllib
import webbrowser
from urllib.parse import urlencode


def main() -> None:
    """
    Open a tab ready to review and approve for new release.

    Based on https://github.com/pypa/hatch/blob/master/scripts/release_github.py
    """
    pkg_data = tomllib.loads(pathlib.Path("pyproject.toml").read_text(encoding="utf-8"))
    about_data = (pathlib.Path("{{cookiecutter.project_name.lower().replace('-', '_')}}") / "__about__.py").read_text(
        encoding="utf-8"
    )
    search_result = re.search(r"__version__ = \"(.*?)\"", about_data)
    if search_result is None:
        sys.exit(1)

    version = search_result.group(1)
    params = urlencode(
        query={
            "title": "v{version}".format(version=version),
            "tag": "v{version}".format(version=version),
        }
    )

    webbrowser.open_new_tab(
        url="{source}/releases/new?{params}".format(
            source=pkg_data["project"]["urls"]["Source"], params=params
        )
    )


if __name__ == "__main__":
    main()
