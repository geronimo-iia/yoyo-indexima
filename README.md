# yoyo-indexima


[![Unix Build Status](https://img.shields.io/travis/geronimo-iia/yoyo-indexima/master.svg?label=unix)](https://travis-ci.org/geronimo-iia/yoyo-indexima)
[![PyPI Version](https://img.shields.io/pypi/v/yoyo-indexima.svg)](https://pypi.org/project/yoyo-indexima)
[![PyPI License](https://img.shields.io/pypi/l/yoyo-indexima.svg)](https://pypi.org/project/yoyo-indexima)

Versions following [Semantic Versioning](https://semver.org/)

## Overview

Indexima migration schema based on [yoyo](https://ollycope.com/software/yoyo/latest/) and [pyhive](https://pypi.org/project/PyHive/).


> The little story
>
>In the land of database migration tool, i have tried:
>
>- flyway
>- liquidbase with hive extention
>
>Both either did not support hive (as flyway), or indexima did not fully compliant with hive (wich cause probleme with liquidbase)
>
>So I try to found a module not too complex in order to migrate our indexima schema in a safe way.
>
>In this early release, I just trying to do the job.


## Setup

### Requirements

* Python 3.7+

### Installation

Install this library directly into an activated virtual environment:

```text
$ pip install yoyo-indexima
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add yoyo-indexima
```

## Usage

### Hive connection

1. backend ui must start with ```indexima://```
2. If you have trouble to obtain an hive connection, please read http://dwgeek.com/guide-connecting-hiveserver2-using-python-pyhive.html/


## Migration

You could see a complete sample under 'example' folder.


### using python client

```
yoyo_indexima
usage: yoyo_indexima [-h] [-s SOURCE] -u URI {show,apply}
```

example:

```
yoyo_indexima  apply  -s $(pwd)/example/migrations/ -u "indexima://admin:super_password@localhost:10000/default"
```

Commands:

- show: pring pending migration
- apply: apply ending migration

### within python code

If your migrations script are under directory ```migration``` folder

```python
import os

from yoyo_indexima import get_backend, read_migrations


if __name__ == "__main__":

    # obtain IndeximaBackend
    backend = get_backend('indexima://admin:super_password@localhost:10000/default')

    # Read migrations folder
    migrations = read_migrations(os.path.join(os.getcwd(), 'migrations'))
    print(f'migrations: {migrations}')
    if migrations:
        # apply migration
        with backend.lock():
            backend.apply_migrations(backend.to_apply(migrations))
```



## License

[The MIT License (MIT)](https://geronimo-iia.github.io/yoyo-indexima/license)


## Contributing

See [Contributing](https://geronimo-iia.github.io/yoyo-indexima/contributing)

## Next step

- production usage in order to see how this tool made the job
- more documentation in code
- purpose few change in 'yoyo' like set all SQL command on Backend class
- ...
