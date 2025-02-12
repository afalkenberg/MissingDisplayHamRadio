import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import CatInterface


# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = np.array([4, 7, 1, 8, 5])


def readVolume():
    port = 'COM4'  # Replace with your COM port
    baud_rate = 9600


    # Write data to COM port
    data_received = CatInterface.writeReadCom(port, baud_rate, "AG0;")

    # Read data from COM port
    # data_received = CatInterface.read_from_com_port(port, baud_rate)

    print(data_received)
    
    return int(data_received[3:6])


def writeVolume(vol):
    port = 'COM4'  # Replace with your COM port
    baud_rate = 9600

    if len(str(vol)) == 1:
        vString = "AG000"+str(vol)+";"
    elif len(str(vol)) == 2:
        vString = "AG00"+str(vol)+";"
    elif len(str(vol)) == 3:
        vString = "AG0"+str(vol)+";"
        
    # Write data to COM port
    CatInterface.writeReadCom(port, baud_rate, vString)

    # Read data from COM port
    # data_received = CatInterface.read_from_com_port(port, baud_rate)

    # print(data_received);
    

# Function to update the plot
def update_plot():
    ax.clear()
    ax.bar(categories, values, color='blue')
    ax.set_ylim(0, 125)  # Adjust y-axis limits if necessary
    ax.set_title('Interactive Bar Plot')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    canvas.draw()

# Function to handle button clicks
def increase_value(index):

    if (index == 0):
        vol = readVolume()
        print(vol)
        values[index] = vol
        values[index] += 1
        writeVolume(values[index])
    else:
        values[index] += 1
        
    update_plot()

def decrease_value(index):
    values[index] -= 1
    update_plot()

# Create the main window
root = tk.Tk()
root.title("Interactive Bar Plot")

# Create the figure and axis
fig, ax = plt.subplots()

# Create the canvas for the figure
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# Create buttons for each category
for i, category in enumerate(categories):
    frame = tk.Frame(root)
    frame.pack(side=tk.LEFT, padx=5)

    label = tk.Label(frame, text=category)
    label.pack(side=tk.TOP)

    btn_increase = tk.Button(frame, text="+", command=lambda i=i: increase_value(i))
    btn_increase.pack(side=tk.LEFT)

    btn_decrease = tk.Button(frame, text="-", command=lambda i=i: decrease_value(i))
    btn_decrease.pack(side=tk.LEFT)

# Initial plot update
update_plot()

# Run the Tkinter event loop
root.mainloop()
