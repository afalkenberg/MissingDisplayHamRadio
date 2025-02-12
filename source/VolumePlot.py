import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import CatInterface


# Sample data

class VolumePlot:

    def __init__(self):
        self.categories = ['A', 'B', 'C', 'D', 'E']
        self.values = np.array([4, 7, 1, 8, 5])
        self.catInterface = CatInterface.CatInterface('COM4', 9600)

    def readVolume(self):
        dataReceived = self.catInterface.writeReadCom("AG0;")
        print(dataReceived)
        return int(dataReceived[3:6])


    def writeVolume(self, vol):
        if len(str(vol)) == 1:
            vString = "AG000"+str(vol)+";"
        elif len(str(vol)) == 2:
            vString = "AG00"+str(vol)+";"
        elif len(str(vol)) == 3:
            vString = "AG0"+str(vol)+";"
        self.catInterface.writeReadCom(vString)


# Function to update the plot
    def update_plot(self):
        self.ax.clear()
        self.ax.bar(self.categories, self.values, color='blue')
        self.ax.set_ylim(0, 125)  # Adjust y-axis limits if necessary
        self.ax.set_title('Interactive Bar Plot')
        self.ax.set_xlabel('Categories')
        self.ax.set_ylabel('Values')
        self.canvas.draw()

# Function to handle button clicks
    def increase_value(self):
        vol = self.readVolume()
        print(vol)
        vol += 1
        self.values[0] += 1
        self.writeVolume(vol)
        self.update_plot()

    def decrease_value(self):
        vol = self.readVolume()
        vol = vol - 1
        self.writeVolume(vol)
        self.update_plot()


    def createMainWindow(self):
# Create the main window
        root = tk.Tk()
        root.title("Interactive Bar Plot")

# Create the figure and axis
        self.fig, self.ax = plt.subplots()

# Create the canvas for the figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack()

# Create buttons for each category
        frame = tk.Frame(root)
        frame.pack(side=tk.LEFT, padx=5)

        label = tk.Label(frame, text=self.categories[0])
        label.pack(side=tk.TOP)

        btn_increase = tk.Button(frame, text="+", command=self.increase_value)
        btn_increase.pack(side=tk.LEFT)

        btn_decrease = tk.Button(frame, text="-", command=self.decrease_value)
        btn_decrease.pack(side=tk.LEFT)

# Initial plot update
        self.update_plot()

# Run the Tkinter event loop
        root.mainloop()


VP = VolumePlot()
VP.createMainWindow()


