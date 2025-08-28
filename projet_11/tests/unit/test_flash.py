from server import clubs, competitions

def test_club_points():
    # Vérifie que le club a bien un champ points
    club = clubs[0]
    assert "points" in club
    assert int(club["points"]) >= 0

def test_competition_places():
    # Vérifie que numberOfPlaces est un entier positif ou nul
    for comp in competitions:
        assert int(comp["numberOfPlaces"]) >= 0
