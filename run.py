from src import configure_app

app=configure_app()

if __name__ == "__main__":
    app.run(debug=True,port=5000)