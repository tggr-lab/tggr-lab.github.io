# tggr-lab.github.io

Forwarding pages for the old GPCompaRe address. `tggr-lab.github.io/gpcompreports/...` forwards to the same page under `tggr-lab.github.io/GPCompaRe/`.

Regenerate after pages are added to the site:

```bash
git -C <GPCompaRe clone> ls-tree -r --name-only origin/gh-pages | grep '\.html$' > pages.txt
python3 make_redirects.py pages.txt
```
