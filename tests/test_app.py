from app.core.config import Settings, get_settings


# Simple tests just to validate its running
def test_app_name():
    """
    Test app's name
    """
    settings: Settings = get_settings()
    assert settings.app_name == "fastapipoc"


def test_version():
    """
    Test app's version
    """
    settings: Settings = get_settings()
    assert settings.app_version == "0.0.1"
