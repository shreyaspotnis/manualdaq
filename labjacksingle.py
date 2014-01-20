"""Implements a class to conveniently get single measurements from LabjackU3."""

import u3
import LabJackPython
import sys

# define MODBUS registers

FIO_ANALOG = 50590
EIO_ANALOG = 50591


class LabJackSingle(object):

    def __init__(self):
         # create a list of all channels
        self.all_channels = ['AIN0', 'AIN1', 'AIN2', 'AIN3', 'AIN4',
                             'AIN5', 'AIN6', 'AIN7', 'AIN8', 'AIN9',
                             'AIN10', 'AIN11', 'AIN12', 'AIN13', 'AIN14',
                             'AIN15']

    def configure(self, channels=None):
        """Opens labjack and configures to read analog signals.

        channels - List of channel addresses to be read.
        e.g in channels = [0, 2, 15], then read AIN0, AIN2, AIN15
        """
        # initialize a labjack u3 device
        print("Getting a handle for LabJack")
        try:
            self.d = u3.U3()
        except LabJackPython.NullHandleException:
            print("Could not open device. Please check that the device you are trying to open is connected")
            sys.exit(1)

        # get the labjack configuration
        self.ljconfig = self.d.configU3()

        if(self.ljconfig['DeviceName'] != 'U3-HV'):
            print "Sorry, your device %s is not supported. Only U3-HV is supported" % self.ljconfig['DeviceName']
            sys.exit(1)

        # Configure all FIO pins to be analog
        # FIO pins are located on LabJack
        # for U3-HV, FI00-03 are equivalent to AIN0-3
        print "Configuring FI00-07 as analog inputs"
        self.d.writeRegister(FIO_ANALOG, 255)

        # Configure all EIO pins to be analog
        print "Configuring EI00-07 as analog inputs"
        self.d.writeRegister(EIO_ANALOG, 255)

        self.configureChannels(channels)

    def configureChannels(self, channels=None):
        # check if a list of channels has been provided. If not then just use
        # all channels.
        if channels:
            self.channels = channels
        else:
            self.channels = range(16)
        # make a list of read commands
        self.cmd = []
        for ch in self.channels:
            self.cmd.append(u3.AIN(ch, 31,
                                    QuickSample = False,
                                    LongSettling = False))
    def closeLJ(self):
        self.d.close()

    def read(self, averages=1):
        bits =  self.d.getFeedback(self.cmd)
        voltage = [0.0]*len(bits)
        for j in range(averages):
            for ch, bit, i in zip(self.channels, bits, range(len(bits))):
                if ch<4:
                    LV = False
                else:
                    LV = True
                voltage[i] += 1000.0*self.d.binaryToCalibratedAnalogVoltage(bit,
                          isLowVoltage = LV,
                          isSingleEnded = True, isSpecialSetting = False,
                          channelNumber = ch)
        for i in range(len(voltage)):
            voltage[i] = voltage[i]/averages
        return voltage

    def getChannels(self):
        if self.channels:
            return self.channels
        else:
            return None

    def getAllChannels(self):
        return self.all_channels
