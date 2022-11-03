# Contributing

[starterkit-lessons][repo] is an open source project, and we welcome contributions of all kinds:

* New lessons;
* Fixes to existing material;
* Bug reports; and
* Reviews of proposed changes.

By contributing, you are agreeing that we may redistribute your work under [these licenses][license].
You also agree to abide by our [contributor code of conduct][conduct].

## Getting Started

1.  We use the [fork and pull][gh-fork-pull] model to manage changes.
    More information about [forking a repository][gh-fork] and [making a Pull Request][gh-pull].

2.  To build the lessons please install the [dependencies](#dependencies).

2.  For our lessons, you should branch from and submit pull requests against the `master` branch.

3.  When editing lesson pages, you need only commit changes to the Markdown source files.

4.  If you're looking for things to work on, please see [the list of issues for all those repositories][issues].
    Comments on issues and reviews of pull requests are equally welcome.

## Building the documentation locally

We recommend using python virtual environment `venv`, but `conda` will also just work fine.

### Requirements
Make sure you have `venv` (virtual environment) in your working directory, and create a new virtual environment `myvenv`
```
$ python3 -m venv myvenv
```

Activate it in the shell and install the requirements
```
$ source myvenv/bin/activate
pip3 install -r requirements.txt
```

Your shell prompt will be augmented by the `(myvenv)` prefix, e.g.
```
(myvenv) mylaptop:~/documentation
```

### Building
The pages are build by executing in the virtual env
```shell
sphinx-build -b html . build
```

### Browsing the result
Open in your browser the file
```shell
$PWD/build/index.html
```

[conduct]: CONDUCT.md
[repo]: https://github.com/EPFL-STD/documentation
[issues]: https://github.com/EPFL-STD/
[license]: LICENSE.md
[pro-git-chapter]: http://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project
[gh-fork]: https://help.github.com/en/articles/fork-a-repo
[gh-pull]: https://help.github.com/en/articles/about-pull-requests
[gh-fork-pull]: https://reflectoring.io/github-fork-and-pull/


```{eval-rst}
.. toctree::
    :hidden:

    CONDUCT.md
    LICENSE.md
```
