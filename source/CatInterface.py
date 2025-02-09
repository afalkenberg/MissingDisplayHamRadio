import serial

def write_to_com_port(port, baud_rate, data):
    """
    Write data to the specified COM port.

    Parameters:
    port (str): The COM port to write to (e.g., 'COM1', 'COM2').
    baud_rate (int): The baud rate for the serial connection.
    data (str): The data to send to the COM port.

    Returns:
    None
    """
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        ser.write(data.encode())
        ser.close()
        print(f"Data '{data}' written to {port} successfully.")
    except Exception as e:
        print(f"Failed to write to {port}: {e}")

def read_from_com_port(port, baud_rate):
    """
    Read data from the specified COM port.

    Parameters:
    port (str): The COM port to read from (e.g., 'COM1', 'COM2').
    baud_rate (int): The baud rate for the serial connection.

    Returns:
    str: The data read from the COM port.
    """
    try:
        ser = serial.Serial(port, baud_rate, timeout=1)
        data = ser.readline().decode().strip()
        ser.close()
        print(f"Data read from {port}: {data}")
        return data
    except Exception as e:
        print(f"Failed to read from {port}: {e}")
        return None

# Example usage
port = 'COM1'  # Replace with your COM port
baud_rate = 9600

# Write data to COM port
write_to_com_port(port, baud_rate, "Hello, COM port!")

# Read data from COM port
data_received = read_from_com_port(port, baud_rate)
