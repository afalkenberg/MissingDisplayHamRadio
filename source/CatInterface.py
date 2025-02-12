import serial
import time


def writeReadCom(port, baud_rate, data):
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)

        ser.write(data.encode())
        print(f"Sent: {data}")
        time.sleep(0.2) # Allow time for data to be received

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

    return "000000"    


    
    
