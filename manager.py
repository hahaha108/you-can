from application import app
from flask_script import Manager,Server
import www

manager = Manager(app)
manager.add_command( "runserver", Server( host='127.0.0.1',port=app.config['SERVER_PORT'],use_debugger = True) )


def main():
    manager.run(default_command="runserver")

if __name__ == '__main__':
    try:
        import sys
        sys.exit( main() )
    except Exception as e:
        import traceback
        traceback.print_exc()
