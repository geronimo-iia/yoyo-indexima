import os

from yoyo_indexima import get_backend, read_migrations


if __name__ == "__main__":
    backend = get_backend('indexima://admin:super_password@localhost:10000/default')

    migrations = read_migrations(os.path.join(os.getcwd(), 'migrations/**/*'))
    print(f'migrations: {migrations}')
    if migrations:
        with backend.lock():
            backend.apply_migrations(backend.to_apply(migrations))
