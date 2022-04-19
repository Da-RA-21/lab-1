class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        '''
        This method initializes all the changeable variables for the class
        :return: None
        '''
        self.__pow = False
        self.__chan = self.MIN_CHANNEL
        self.__vol = self.MIN_VOLUME

    def power(self) -> None:
        '''
        This method flips the power on and off depending on the current state
        :return: None
        '''
        if self.__pow is True:
            self.__pow = False
        else:
            self.__pow = True

    def channel_up(self) -> None:
        '''
        increments the channel by one and defaults to the min if at the max already
        :return: None
        '''
        if self.__pow is True:
            if self.__chan == self.MAX_CHANNEL:
                self.__chan = self.MIN_CHANNEL
            else:
                self.__chan += 1
        else:
            pass

    def channel_down(self) -> None:
        '''
        decrements the channel by one and defaults to the max if at the min already
        :return: None
        '''
        if self.__pow is True:
            if self.__chan == self.MIN_CHANNEL:
                self.__chan = self.MAX_CHANNEL
            else:
                self.__chan -= 1
        else:
            pass

    def volume_up(self) -> None:
        '''
        increments the volume by one and defaults to the min if at max already
        :return: None
        '''
        if self.__pow is True:
            if self.__vol == self.MAX_VOLUME:
                pass
            else:
                self.__vol += 1
        else:
            pass

    def volume_down(self) -> None:
        '''
        decrements the volume by one and defaults to the max if at the min already
        :return: None
        '''
        if self.__pow is True:
            if self.__vol == self.MIN_VOLUME:
                pass
            else:
                self.__vol -= 1
        else:
            pass

    def __str__(self) -> str:
        '''
        prepares a string that includes info on current power status, channel number, and volume number
        :return: string containing information about the status of the television
        '''
        return str(f'TV status: Is on = {self.__pow}, Channel = {self.__chan}, Volume = {self.__vol}')
