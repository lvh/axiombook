==============
 Installation
==============

Using pip
=========

Axiom is reasonably easy to install using pip. However, it does require its
dependency, Epsilon, during ``setup.py egg-info``. That means that it needs to
be avaiable before pip tries to install Axiom. In short, you need to do::

  $ pip install Epsilon
  $ pip install Axiom

Unfortunately, due to the way pip works, ``pip install Epsilon Axiom`` or
putting both of them in a requirements file and installing it using ``pip -r``
does *not* work.
