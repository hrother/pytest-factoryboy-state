from __future__ import annotations

import base64
import os
import pickle

import factory.random
import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.reports import BaseReport
from _pytest.terminal import TerminalReporter
from pytest import Session


def pytest_addoption(parser: Parser) -> None:
    group = parser.getgroup("factoryboy-state")
    group.addoption(
        "--show-state",
        action="store_true",
        dest="show_state",
        default=False,
        help="Show factoryboy state for failures.",
    )
    group.addoption(
        "--set-state",
        action="store",
        dest="factoryboy_state",
        default=None,
        help="Set factoryboy state.",
    )


@pytest.hookimpl()
def pytest_sessionstart(session: Session) -> None:
    """Set factoryboy random state.

    Args:
        session (Session): The pytest session, unused in this function.
    """
    decoded_state = None
    state = session.config.getoption("factoryboy_state") or os.environ.get(
        "FACTORYBOY_STATE"
    )
    if state:
        try:
            decoded_state = pickle.loads(base64.b64decode(state.encode("ascii")))
        except ValueError:
            decoded_state = None
    if decoded_state:
        factory.random.set_random_state(decoded_state)


@pytest.hookimpl()
def pytest_terminal_summary(
    terminalreporter: TerminalReporter, exitstatus: int, config: Config
) -> None:
    """Show factoryboy random state when there are test failures or errors.

    Factoryboy uses randomness in order to generate its values which is great for
    fuzzing but makes it really hard to reproduce tests which fail due to a fuzzed
    value. This hook outputs the random state used by factory-boy (and faker) when
    there are test failures (or errors).

    The outputted state is an ascii, base64 encoded pickle dump.

    Args:
        terminalreporter (TerminalReporter): Add output to the pytest output.
        exitstatus (int): The exit status of pytest (unused)
        config (Config): The pytest config (unused)

    """
    show_state = config.getoption("show_state") or (
        os.environ.get("SHOW_FACTORYBOY_STATE") == "True"
    )
    failures: list[BaseReport] = terminalreporter.getreports("failed")
    errors: list[BaseReport] = terminalreporter.getreports("error")
    if show_state and (failures or errors):
        terminalreporter.write_sep("=", "factory-boy random state")
        encoded_state = base64.b64encode(
            pickle.dumps(factory.random.get_random_state())
        )
        terminalreporter.write_line(encoded_state.decode("ascii"))
