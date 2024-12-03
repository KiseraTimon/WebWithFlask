from website import create_app

#Calling initializer function
app = create_app()

#Running web server
if __name__ == '__name__':
    app.run(debug=True)