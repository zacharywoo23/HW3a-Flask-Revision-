from flask import Flask

myobj = Flask (__name__)

@myobj.route("/")
def home():
    name = "Lisa"
    city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    return '''
    <html>
    <body>
        <h1> Welcome ''' + name + '''! </h1>
        <a href ="www.google.com">notgoogle </a>
        <ul>
            <li> ''' + city_names[0] + ''' </li>
            <li> ''' + city_names[1] + ''' </li>
            <li> ''' + city_names[2] + ''' </li>
            <li> ''' + city_names[3] + ''' </li>
        </ul>
    </body>
    </html>
    '''

    if __name__ == "__main__":
        myobj.run(debug=True)

    myobj.run()