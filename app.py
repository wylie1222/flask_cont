from web import create_app
from flask import Flask, request
app = create_app()


if __name__ == "__main__":
    app.run()