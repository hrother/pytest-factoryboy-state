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
