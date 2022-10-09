from distutils.log import debug
from Test_web import create_app


#Test_web folder as a library, and run the app in this folder
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)