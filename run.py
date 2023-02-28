from api.v1.app import app as api
from web.app import app as web

if __name__ == '__main__':
    api.run()
    # web.run()
