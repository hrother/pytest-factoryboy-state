# -*- coding: utf-8 -*-
from __future__ import annotations


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


def test_does_nothing_when_not_explicitly_called(testdir):
    testdir.makepyfile(
        """
        def test_failure():
            assert False
        """
    )
    result = testdir.runpytest("")

    result.stdout.no_fnmatch_line("=*= factory-boy random state =*=")


def test_shows_state_on_failure(testdir):
    testdir.makepyfile(
        """
        def test_failure():
            assert False
        """
    )
    result = testdir.runpytest("--show-state")

    result.stdout.fnmatch_lines(["=*= factory-boy random state =*="])


def test_shows_state_on_failure_from_environment_variable(testdir, monkeypatch):
    monkeypatch.setenv("SHOW_FACTORYBOY_STATE", "True")
    testdir.makepyfile(
        """
        def test_failure():
            assert False
        """
    )
    result = testdir.runpytest()

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


def test_shows_state_on_error_for_environment_variable(testdir, monkeypatch):
    monkeypatch.setenv("SHOW_FACTORYBOY_STATE", "True")
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
    result = testdir.runpytest()

    result.stdout.fnmatch_lines(["=*= factory-boy random state =*="])


def test_uses_set_state(testdir, state):
    testdir.makepyfile(
        """
        import factory

        class User:
            def __init__(self, name):
                self.name = name

        class UserFactory(factory.Factory):
            class Meta:
                model = User

            name = factory.Faker("first_name")


        def test_user_name():
            user = UserFactory()
            assert user.name == "Sara"
        """
    )
    result = testdir.runpytest("-v", f"--set-state={state}")

    result.stdout.fnmatch_lines(
        [
            "*::test_user_name PASSED*",
        ]
    )

    assert result.ret == 0


def test_uses_set_state_from_environment(testdir, state, monkeypatch):
    monkeypatch.setenv("FACTORYBOY_STATE", state)
    testdir.makepyfile(
        """
        import factory

        class User:
            def __init__(self, name):
                self.name = name

        class UserFactory(factory.Factory):
            class Meta:
                model = User

            name = factory.Faker("first_name")


        def test_user_name():
            user = UserFactory()
            assert user.name == "Sara"
        """
    )
    result = testdir.runpytest("-v")

    result.stdout.fnmatch_lines(
        [
            "*::test_user_name PASSED*",
        ]
    )

    assert result.ret == 0


def test_ignores_invalid_state(testdir):
    testdir.makepyfile(
        """
        import factory

        class User:
            def __init__(self, name):
                self.name = name

        class UserFactory(factory.Factory):
            class Meta:
                model = User

            name = factory.Faker("first_name")


        def test_user_name():
            user = UserFactory()
            assert user.name == "Sara"
        """
    )
    result = testdir.runpytest("-v", "--set-state=x")
    result.stdout.fnmatch_lines(
        [
            "*::test_user_name FAILED*",
        ]
    )
    assert result.ret != 0
