from src.classes.config import Config

def test_config():
    config = Config.get_instance()

    assert config.get_setting("gene_insertion_chance") == 0.33

def test_get_personality_expression():
    config = Config.get_instance()

    assert config.get_personality_expression() == {20: 1, 40: 2, 60: 3, 80: 4, 100: 5}