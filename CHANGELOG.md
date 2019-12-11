# 0.1.2 (2019-12-11)

- fix internal upgrade

# 0.1.1 (2019-12-3)

- add a way to set hive configuration and TSaslClientTransport instance
- refactor register_backend

# 0.1.0 (2019-12-2)

- fix indexima Timestamp column format
- add mypi typing
- complete documentation and fix typo
- use inner get_backend function in cli
- use python3 template String in tool migration script
- show glob pattern usage
- refactorisation of internal migration (avoid change internal module state)
- align source tree to yoyo project
- add '--force' command option
- add '--all' command option
- rewrote cli parser
- add rollback, mark, unmark, breaklock command
- add 'dry-run' mode

# 0.0.1 (2019-11-19)

- initial project structure based on [geronimo-iia/template-python](https://github.com/geronimo-iia/template-python)
- adding initial dependencies
- create IndeximaBackend backend
- rewrote internal migration
- hook datetime to timestamp
- hook yoyo with register_indexima
- hook defauly migratin table
- adding cli tool

