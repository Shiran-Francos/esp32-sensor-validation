# Get the information from the sensors/ Esp32 output

import serial


class SerialReader:

    def __init__(self, baud_rate=115200 , port='COM3'):

        self.ser=serial.Serial(port,baud_rate, timeout=1)
        if self.ser.is_open:
            print("Serial Reader Successfully Opened")
        else:
            print("Error accured, Reader Did Not Open!")

    def read_line(self):
        line= self.ser.readline().decode('utf-8').strip()
        if line:
            return line
        return None

    def close(self):

        self.ser.close()
        if not self.ser.is_open:
            print("Serial Reader Successfully Closed")
        else:
            print("Reader Is Still Open!")


        









