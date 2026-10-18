"""Generate forwarding pages: /gpcompreports/<path> -> /GPCompaRe/<path>.

The GPCompaRe site moved when the repo was renamed from gpcompreports.
GitHub Pages does not redirect after a rename, so published links to the
old address would 404. Each page that exists on the live site gets a
forwarding page here; 404.html catches anything else under the old prefix.

Usage: python3 make_redirects.py <file listing live .html paths>
"""
import html
import pathlib
import sys

OLD = "gpcompreports"
NEW = "https://tggr-lab.github.io/GPCompaRe/"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>GPCompaRe database has moved</title>
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={url}">
<script>location.replace({url_js} + location.search + location.hash);</script>
</head>
<body style="font-family: system-ui, sans-serif; max-width: 40rem; margin: 3rem auto; padding: 0 1rem;">
<p>The GPCompaRe database has moved to <a href="{url}">{url}</a>.</p>
</body>
</html>
"""


def write(path, target):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(PAGE.format(url=html.escape(target), url_js=repr(target)))


def main(listing):
    root = pathlib.Path(__file__).parent
    for rel in pathlib.Path(listing).read_text().split():
        target = NEW + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)
        write(root / OLD / rel, target)


if __name__ == "__main__":
    main(sys.argv[1])
