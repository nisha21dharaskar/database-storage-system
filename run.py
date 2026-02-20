from app import create_app


app = create_app()


if __name__ == "__main__":
    # Debug mode is convenient for development.
    # Disable debug in production.
    app.run(debug=True)

