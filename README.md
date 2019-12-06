# Download Materials

As a student, I need to check the websites of the lectures I attend regularly
to see whether there are any new slides or exercise sheets online.
Unfortunately, those websites usually don't come with an RSS feed or similar.
This is a small script to automate that task. It works best with a `Makefile`:

```make
.PHONY: all slides exercises

DOWNLOAD=path/to/download-materials.py

all: slides exercises

slides:
	@$(DOWNLOAD) \
		--from 'http://theo.cs.ovgu.de/lehre/lehre2019w/funk-prog/slides/slides-{:02d}.pdf' \
		--to 'slides/slides-{:02d}.pdf'

exercises:
	@$(DOWNLOAD) \
		--from 'http://theo.cs.ovgu.de/lehre/lehre2019w/funk-prog/exercises/exercise-{:02d}.pdf' \
		--to 'exercises/exercise-{:02d}.pdf'
```

Its output will then look like this:

```
$ make
Downloading slides/slides-10.pdf ... not yet available
Downloading exercises/exercise-07.pdf ... not yet available
```

If you pass a `-v` to the script (e.g. on line 3 in the `Makefile`), it will
give some more information:

```
$ make
Skipped slides/slides-01.pdf
Skipped slides/slides-02.pdf
Skipped slides/slides-03.pdf
Skipped slides/slides-04.pdf
Skipped slides/slides-05.pdf
Skipped slides/slides-06.pdf
Skipped slides/slides-07.pdf
Skipped slides/slides-08.pdf
Skipped slides/slides-09.pdf
Downloading slides/slides-10.pdf ... not yet available
Skipped exercises/exercise-01.pdf
Skipped exercises/exercise-02.pdf
Skipped exercises/exercise-03.pdf
Skipped exercises/exercise-04.pdf
Skipped exercises/exercise-05.pdf
Skipped exercises/exercise-06.pdf
Downloading exercises/exercise-07.pdf ... not yet available
```

## Help Message

```
$ download-materials.py -h
usage: download-materials.py [-h] --from URL [--auth USER PASSWORD] --to FILE
                             [--first-id ID] [-v]

Download numbered materials

optional arguments:
  -h, --help            show this help message and exit
  --from URL            URL template, e.g. `foo.bar/slide{}.pdf`
  --auth USER PASSWORD  authentication for URL
  --to FILE             file template, e.g. `./slides/L{}.pdf`
  --first-id ID         number of first material, default: 1
  -v                    verbose mode
```

