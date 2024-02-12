from Task1 import create_app

app = create_app()

if __name__ == '__main__':  #to run this file only when we run it not import it
    app.run(debug=True)  # debog= True means that the server will automatically run the website whenever we change it
    
