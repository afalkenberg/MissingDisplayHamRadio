import serial
import time


class CatInterface:

    def __init__(self, port, rate):
        self.port = port
        self.baudRate = rate
        self.sleepRate = 0.1


    def writeReadCom(self, data):
        return "123123"
        try:
            ser = serial.Serial(self.port, self.baudRate, timeout=1)
            ser.write(data.encode())
            print(f"Sent: {data}")
            time.sleep(self.sleepRate) # Allow time for data to be received
            if ser.in_waiting > 0:
                received_data = ser.readline().decode().strip()
                print(f"Received: {received_data}")
                return received_data
            else:
                print("No data received within the timeout period.")

        except serial.SerialException as e:
            print(f"Error: {e}")

        finally:  # Use finally to ensure the port is closed even if errors occur
            if 'ser' in locals() and ser.is_open:
                ser.close()
                print("Port closed.")

        return "123456"    


    
    
