# anaconda-mode [![Build Status](https://travis-ci.org/proofit404/anaconda-mode.png?branch=master)](https://travis-ci.org/proofit404/anaconda-mode) [![Dependency Status](https://gemnasium.com/proofit404/anaconda-mode.png)](https://gemnasium.com/proofit404/anaconda-mode)

Code navigation, documentation lookup and completion for Python.

## Requirements

* emacs 24.3
* python 2.6, 2.7, 3.2 or 3.3

## Features

* context-sensitive code completion for Python
* jump to definition
* find references
* view documentation
* virtualenv

## Install

All you need is install the package from [Melpa](http://melpa.milkbox.net/).

    M-x package-install RET anaconda-mode RET

## Usage

By default `anaconda-mode` starts its HTTP server on port `24970` for
interaction with Python process.  You may want to close this port for
incoming network connections.  This server will start automatically
when you call any anaconda command like reference search or
documentation lookup.  To start `anaconda-mode` automatically in all
python buffers add following to your configuration.

```lisp
(add-hook 'python-mode-hook 'anaconda-mode)
```

Anaconda mode detect active virtual environment through value of
`python-shell-virtualenv-path` variable defined in `python.el`
library.  When you set it to actual virtualenv path next anaconda-mode
command you call will restart its python process in proper environment
before performing this call.  This allow anaconda processing
virtualenv site-packages with minimum number of actions from your
side.  I strongly recommended you to use package like
[pyenv-mode](https://github.com/proofit404/pyenv-mode) or similar
package to hold `python-shell-virtualenv-path` in actual state.

## Contribs

Anaconda doesn't has internal contrib interface yet.  But any way you
can use additionally packages with manual setup.  To turn on any of
its add corresponding code snippet to your configuration.

#### anaconda-eldoc

ElDoc documentation lookup with `anaconda-mode`.

```lisp
(add-hook 'python-mode-hook 'anaconda-eldoc)
```

#### company-anaconda

Anaconda backend for [company-mode](http://company-mode.github.io).

```lisp
(add-to-list 'company-backends 'company-anaconda)
```

![screenshot1](screenshots/snapshot1.png)

## Contributions

Are very welcome.  But any significant change has to be accompanied
with tests, both for Emacs Lisp and Python code.  To run the test
suite, call:

    tox

## Thanks

* Dmitry Gutov **@dgutov**
* Bo Lin **@sadboy**
* Vasilij Schneidermann **@wasamasa**
