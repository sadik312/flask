# import website package,
# grab create_app func to create application and run it

from website import create_app

app = create_app()

if __name__ == '__main__': # only if we run this file, are we going to execute this file
    app.run(debug=True) # run flask app, everytime python code is changed, it will rerun the flask webserver