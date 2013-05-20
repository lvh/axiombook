# The Axiom Book

The Axiom Book is intended as a primer to [Axiom][axiom], an object
store for Python built on top of SQLite.

[axiom]: http://pypi.python.org/pypi/Axiom

## Reading

The [current version of the book][current] is graciously hosted by
[ReadTheDocs][rtd].

[current]: https://the-axiom-book.readthedocs.org/en/latest/
[rtd]: https://readthedocs.org

## Building

The repository is a fairly standard [Sphinx][sphinx] repository. To
build the documentation, run `make [builder]` where builder is the
format you want (e.g. `html` or `pdf`).

[sphinx]: http://sphinx-doc.org/

The documentation is self-testing using doctests, wich can be run
using `make doctests`.

## Contributing

Contributions and issue reports are welcome on [Github][github].

[github]: https://github.com/lvh/axiombook

Please make contributions self-testing using doctest wherever possible!

## Testing

Most of the Axiom book is written using doctests, so the book can
largely be automatically verified. This is done automatically by
[Travis CI][travis].

[![Build Status](https://travis-ci.org/lvh/axiombook.png?branch=master)](https://travis-ci.org/lvh/axiombook)

[travis]: https://travis-ci.org/lvh/axiombook
