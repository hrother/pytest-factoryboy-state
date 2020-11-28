def pytest_addoption(parser):
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
