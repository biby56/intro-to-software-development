import pytest
from geo_calculator.rolling_stone.player import Player

@pytest.fixture
def new_player():
    return Player()

def test_player(new_player):
    assert isinstance(new_player, Player)
    assert new_player.score == 0

def test_player_receive_score():
    # Arrange
    player = Player()
    RECEIVED_SCORE = 10
    assert player.score == 0
    # Act
    player.receive_score(RECEIVED_SCORE)
    # Assert
    assert player.score == RECEIVED_SCORE
