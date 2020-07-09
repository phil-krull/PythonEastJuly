from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    # return 'Hello World!'  # Return the string 'Hello World!' as a response
    return render_template('index.html')

@app.route('/<name>')
def first_method(name):
    # return f'name sent as a route parameter is: {name}'
    
    return render_template('name.html', name_for_html = name, location = 'Tulsa')
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


# url(client) == route(server) -> Request
# Response is what the method returns