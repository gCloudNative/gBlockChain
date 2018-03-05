from flask_script import Manager, Server, Shell, Command, Option
from flask_script.commands import ShowUrls, Clean
from flask_migrate import Migrate, MigrateCommand

from gBlockChain import app
from gBlockChain.lib.database import db

manager = Manager(app)

is_sqlite = app.config.get('SQLALCHEMY_DATABASE_URI').startswith('sqlite:')
migrate = Migrate(app, db, render_as_batch=is_sqlite)

def _make_context():
    return dict(app=app, db=db)

manager.add_command('db', MigrateCommand)
manager.add_command('url', ShowUrls())
manager.add_command('clean', Clean())
manager.add_command('server', Server(host=app.config.get('HOST', '0.0.0.0'), port=app.config.get('PORT', 5000)))
manager.add_command('dev', Server(host=app.config.get('HOST', '0.0.0.0'), port=app.config.get('PORT', 5000), use_debugger=True))
manager.add_command("shell", Shell(make_context=_make_context))
#manager.add_command("gunicorn", GunicornServer())

if __name__ == '__main__':
    manager.run()
