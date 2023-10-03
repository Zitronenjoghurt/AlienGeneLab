from src.classes.config import Config

def test_config():
    config = Config.get_instance()

    assert config.get_setting("gene_insertion_chance") == 0.5