from website import create_app, create_database

#Calling initializer function
app = create_app()

#Running web server
if __name__ == '__main__':
    with app.app_context():
        create_database(app)
    app.run(debug=True)