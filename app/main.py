from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Game Library API"}

@app.get("/games")
def get_games():
    return [
        {
            "id": 1,
            "title": "Elden Ring",
            "genre": "Action RPG"
        },
        {
            "id": 2,
            "title": "Hades",
            "genre": "Roguelike"
        }
    ]