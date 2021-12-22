from functools import wraps
from random import choice

from flask import g, request


class FlaskReplicated:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        assert hasattr(app, "extensions")
        assert "sqlalchemy" in app.extensions
        if "replicated" not in app.extensions:
            app.extensions["replicated"] = self
            binds = app.config.get("SQLALCHEMY_BINDS") or {}
            print(binds)
            if "replica_0" in binds:
                print("Replica is in binds")
                app.before_request(self._pick_database)
                db = app.extensions["sqlalchemy"].db
                get_engine_vanilla = db.get_engine

                def get_replicated_engine(app=app, bind=None):
                    if bind is None and g:
                        use_replica = getattr(g, "use_replica", False)
                        use_master = getattr(g, "use_master", False)
                        print(f"Use Replica: {use_replica} ; Use master: {use_master}")
                        if use_replica and not use_master:
                            bind = random_replica(app.config.get("REPLICA_SET"))
                    return get_engine_vanilla(app, bind)

                db.get_engine = get_replicated_engine

    def _pick_database(self):
        print("Choosing database...")
        # print("Choosing database....")
        # # Does this do anything?
        # func = current_app.view_functions.get(request.endpoint)
        # print(f"Current app view function get: {func}")
        # use_master_database = getattr(func, "use_master_database", False)
        # print(f"Should we use master database? {use_master_database}")
        # if use_master_database:
        #     g.use_master = True
        # use_replica_database = getattr(
        #     func, "use_replica_database", False
        # )  # or request.method == 'GET'
        # print(f"Should we use replica database? {use_replica_database}")
        # g.use_replica = use_replica_database
        if request.method == 'GET' and "author" in request.path:
            g.use_replica = True

def random_replica(replicas):
    return choice(replicas)

def use_master_database(func):
    def wrapper(*args, **kwargs):
        func.use_master_database = True
        return func(*args, **kwargs)

    return wrapper


def use_replica_database(func):
    def wrapper(*args, **kwargs):
        # setattr(func, "use_replica_database", True)
        func.use_replica_database = True
        return func(*args, **kwargs)

    return wrapper
