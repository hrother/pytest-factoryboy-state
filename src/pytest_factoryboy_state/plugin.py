import base64
import pickle
from typing import Generator
from typing import List

import factory.random
import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from _pytest.reports import BaseReport
from _pytest.terminal import TerminalReporter


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


@pytest.hookimpl(hookwrapper=True)
def pytest_terminal_summary(
    terminalreporter: TerminalReporter, exitstatus: int, config: Config
) -> Generator[None, None, None]:
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

    Yields:
        Let other plugins execute their ``pytest_terminal_summary`` hook before the
        random state is shown.
    """
    yield
    failures: List[BaseReport] = terminalreporter.getreports("failed")
    errors: List[BaseReport] = terminalreporter.getreports("error")
    if failures or errors:
        terminalreporter.write_sep("=", "factory-boy random state")
        encoded_state = base64.b64encode(
            pickle.dumps(factory.random.get_random_state())
        )
        terminalreporter.write_line(encoded_state.decode("ascii"))
