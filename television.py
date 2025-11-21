class Television:
    # Class constants
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        # Instance variables (all private)
        self.__status = False        # TV starts off
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        # Toggle the power
        self.__status = not self.__status

    def mute(self) -> None:
        # Toggle mute only when TV is on
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        # Only change channel if TV is on
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        # Only decrease channel if TV is on
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        #  Increases the volume if TV is on
        if self.__status:
            # Any volume change un-mutes the TV
            if self.__muted:
                self.__muted = False

            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        # Decreases the volume if TV is on
        if self.__status:
            # Any volume change un-mutes the TV
            if self.__muted:
                self.__muted = False

            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """  Return the TV details in the format:
        Power = [status], Channel = [channel], Volume = [volume]
         If the TV is muted, the shown volume is 0.   """

        if self.__muted:
            shown_volume = 0
        else:
            shown_volume = self.__volume

        return "Power = " + str(self.__status) + ", Channel = " + \
               str(self.__channel) + ", Volume = " + str(shown_volume)
