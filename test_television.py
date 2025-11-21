from television import Television


def test_init():
    """Tests that a new Television object starts in the default state."""
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power():
    """Test that the power() method correctly turns the TV on and off
    without affecting the channel or volume."""
    tv = Television()

    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_channel_up():
    """Test that channel_up() works when the TV is on, and wraps from MAX_CHANNEL
    down to MIN_CHANNEL."""
    tv = Television()
    tv.power()

    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 2, Volume = 0"

    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down():
    """Test that the channel_down() method works when the TV is on,
    and wraps from MIN_CHANNEL up to MAX_CHANNEL."""
    tv = Television()
    tv.power()

    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"


def test_channel_when_off():
    """Test that channel_up() and channel_down() do nothing when the TV is off."""
    tv = Television()
    tv.channel_up()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_volume_up():
    """Test that volume_up() increases the volume when the TV is on,
    stops at MAX_VOLUME, and does not exceed it."""
    tv = Television()
    tv.power()

    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    """ Test that volume_down() decreases the volume when the TV is on,
    stops at MIN_VOLUME, and does not go below it."""
    tv = Television()
    tv.power()

    tv.volume_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_volume_when_off():
    """Test that volume_up() and volume_down() do nothing when the TV is off."""
    tv = Television()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    """Test that mute() works when the TV is on. When muted, the TV displays 0
    When unmuted, it returns to its original volume"""
    tv = Television()

    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"


def test_volume_changes_unmute():
    """    Test that changing the volume while muted automatically unmutes the TV."""
    tv = Television()
    tv.power()

    tv.volume_up()
    tv.volume_up()

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"