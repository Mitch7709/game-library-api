def test_create_game(client):
    response = client.post(
        "/games",
        json={
            "title": "The Legend of Zelda",
            "genre": "Action-Adventure",
            "developer": "Nintendo",
            "release_year": 1986,
            "completed": False,
            "rating": 9.5
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] > 0
    assert data["title"] == "The Legend of Zelda"
    assert data["genre"] == "Action-Adventure"
    assert data["developer"] == "Nintendo"
    assert data["release_year"] == 1986
    assert data["completed"] is False
    assert data["rating"] == 9.5

def test_get_game(client):
    create_response = client.post(
        "/games",
        json={
            "title": "Super Mario Bros.",
            "genre": "Platformer",
            "developer": "Nintendo",
            "release_year": 1985
        }
    )

    game_id = create_response.json()["id"]

    response = client.get(f"/games/{game_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == game_id
    assert data["title"] == "Super Mario Bros."

def test_get_game_not_found(client):
    response = client.get("/games/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Game with id 999 was not found"
    }

def test_patch_game(client):
    create_response = client.post(
        "/games",
        json={
            "title": "Halo",
            "genre": "First-Person Shooter",
            "developer": "Bungie",
            "release_year": 2001,
            "completed": False,
            "rating": 9.0
        }
    )

    game_id = create_response.json()["id"]

    response = client.patch(
        f"/games/{game_id}",
        json={
            "completed": True
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["completed"] is True

    assert data["title"] == "Halo"
    assert data["genre"] == "First-Person Shooter"
    assert data["developer"] == "Bungie"
    assert data["release_year"] == 2001
    assert data["rating"] == 9.0

def test_patch_game_can_clear_rating(client):
    create_response = client.post(
        "/games",
        json={
            "title": "Portal",
            "genre": "Puzzle",
            "developer": "Valve",
            "release_year": 2007,
            "rating": 9.5
        }
    )

    game_id = create_response.json()["id"]

    response = client.patch(
        f"/games/{game_id}",
        json={
            "rating": None
        }
    )

    assert response.status_code == 200
    assert response.json()["rating"] is None

def test_create_game_rejects_invalid_rating(client):
    response = client.post(
        "/games",
        json={
            "title": "Test Game",
            "genre": "Test",
            "developer": "Test Developer",
            "release_year": 2020,
            "rating": 11
        }
    )

    assert response.status_code == 422

def test_delete_game(client):
    create_response = client.post(
        "/games",
        json={
            "title": "Doom",
            "genre": "First-Person Shooter",
            "developer": "id Software",
            "release_year": 1993
        }
    )

    game_id = create_response.json()["id"]

    delete_response = client.delete(f"/games/{game_id}")

    assert delete_response.status_code == 200

    get_response = client.get(f"/games/{game_id}")

    assert get_response.status_code == 404