=======================
pytest-factoryboy-state
=======================

.. image:: https://img.shields.io/pypi/v/pytest-factoryboy-state.svg
    :target: https://pypi.org/project/pytest-factoryboy-state
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-factoryboy-state.svg
    :target: https://pypi.org/project/pytest-factoryboy-state
    :alt: Python versions

.. image:: https://github.com/hrother/pytest-factoryboy-state/workflows/build/badge.svg
    :target: https://github.com/hrother/pytest-factoryboy-state/actions?workflow=build
    :alt: Status tests

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

.. image:: https://results.pre-commit.ci/badge/github/hrother/pytest-factoryboy-state/main.svg
   :target: https://results.pre-commit.ci/latest/github/hrother/pytest-factoryboy-state/main
   :alt: pre-commit.ci status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


`pytest`_ plugin to manage random state in `factory_boy`_.

---

`factory_boy`_ uses randomness in order to generate its fuzzed values which makes it hard to reproduce tests which fail due to a fuzzed value.
This plugin shows the random state used by factory_boy (and faker) when there are test failurs. And allows to run the tests with a specific random state.


Features
--------

* Show random state on test failures using cli option ``--show-state`` or by setting an environment variable.
* Set random state through environment variable or with cli option ``--set-state``


Requirements
------------

* Python > 3.7
* `pytest`_
* `factory_boy`_


Installation
------------

You can install "pytest-factoryboy-state" via `pip`_ from `PyPI`_::

    $ pip install pytest-factoryboy-state


Usage
-----

Show the random state of factoryboy on test failure with::

    $ pytest --show-state

Or by defining the environment variable ``SHOW_FACTORYBOY_STATE`` to ``True``.

Rerun the tests with a given state::

    $ pytest --set-state=<factoryboy_state>

You can also set the environment variable ``FACTORYBOY_STATE`` to the state and run pytest as usual.

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-factoryboy-state" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/hrother/pytest-factoryboy-state/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.org/project/pip/
.. _`PyPI`: https://pypi.org/project
.. _`factory_boy`: https://factoryboy.readthedocs.io/en/stable/
