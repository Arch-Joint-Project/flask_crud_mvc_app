# local imports
from app import create_app

# entry point for application
app = create_app('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run()
