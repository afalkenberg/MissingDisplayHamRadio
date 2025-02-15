import serial
import time  # Import the time module

try:
    ser = serial.Serial('COM4', 9600, timeout=1)  # Add timeout
    print("Port opened!")

    data_to_send = 'EX1000;'
    ser.write(data_to_send.encode())
    print(f"Sent: {data_to_send}")
    time.sleep(1.2) # Allow time for data to be received

    if ser.in_waiting > 0:
        received_data = ser.readline().decode().strip()
        print(f"Received: {received_data}")
    else:
        print("No data received within the timeout period.")

except serial.SerialException as e:
    print(f"Error: {e}")

finally:  # Use finally to ensure the port is closed even if errors occur
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Port closed.")
