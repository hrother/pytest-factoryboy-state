# -*- coding: utf-8 -*-


def test_help_message(testdir):
    result = testdir.runpytest(
        "--help",
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "factoryboy-state:",
            "*--show-state*Show factoryboy state for failures.",
            "*--set-state=FACTORYBOY_STATE",
            "*Set factoryboy state.",
        ]
    )


def test_shows_state_on_failure(testdir):
    testdir.makepyfile(
        """
        def test_failure():
            assert False
        """
    )
    result = testdir.runpytest("--show-state")

    result.stdout.fnmatch_lines(["=*= factory-boy random state =*="])


def test_shows_state_on_error(testdir):
    testdir.makepyfile(
        """
        import pytest

        @pytest.fixture
        def foo():
            raise Exception


        def test_failure(foo):
            assert True
        """
    )
    result = testdir.runpytest("--show-state")

    result.stdout.fnmatch_lines(["=*= factory-boy random state =*="])
