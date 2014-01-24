motm
====

Collection of my MOTM talks for [Montréal-Python](http://montrealpython.org).

How to run it
-------------

I use [playerpiano](https://pypi.python.org/pypi/PlayerPiano/0.1.1) to run all my demos and I currently use [python 3.3](http://python.org/download/releases/3.3.3/) to run them. Also, all these files are [doctest files](http://docs.python.org/3.3/library/doctest.html) too so you can test the code yourself by running

    python -m doctest [the MOTM file]
    
and to run the demo, do

    playerpiano [the MOTM file]
    
FAQ
---

* **The doctests don't pass!**

    Some of the files use a combination of ``# doctest: +SKIP`` and other [doctest directives](http://docs.python.org/3.3/library/doctest.html#directives) to make the doctests pass and yet the playerpiano output look good, but sometimes (especially where ellipsis is necessary), the file was modified in preference to the playerpiano demo.

    Also, some of the os/fs based modules (i.e. sh, path) do create files, play with the fs, etc, so they are a bit more tempermental.

Upcoming MOTM
-------------

Here's a non-binding list of ideas for upcoming MOTM:

* [line_profiler](https://pypi.python.org/pypi/line_profiler) (Thanks Ronan!)
