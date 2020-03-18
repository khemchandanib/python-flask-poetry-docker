from web_app import app


def main():
    print('In Main')
    app.start()

myapp = app.webapp
if __name__ == '__main__':
    main()