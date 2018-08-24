from app import create_app
import os



app = create_app(env=os.environ.get('APP_SETTING', "debug"))


if __name__ == "__main__":
    app.run()

    