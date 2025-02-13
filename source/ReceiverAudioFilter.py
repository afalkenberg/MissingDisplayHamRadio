


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import CatInterface


# Sample data

class ReceiverAudioFilter:

    def __init__(self, dbg):
        self.categories = ['0-9', '10-19', '20-29', '30-39', '40-49']
        self.values = np.array([4, 7, 1, 8, 5])
        self.catInterface = CatInterface.CatInterface('COM4', 9600, dbg)

    def calcValues(self, vol):
        v = 50*vol/256
        self.values[4] = min(10, v-40)
        self.values[3] = min(10, v-30)
        self.values[2] = min(10, v-20)
        self.values[1] = min(10, v-10)
        self.values[0] = min(10, v)
        
    def readVolume(self):
        dataReceived = self.catInterface.writeReadCom("AG0;")
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

        lcutFreq = 1000
        hcutFreq = 3000
        lSlope = 6   # 2 = 3db ;  4 = 6db ; 6 = 9dB 
        hSlope = 1

        frequencies = np.linspace(0, 4000, 4000)
        response = np.piecewise(frequencies, [frequencies < lcutFreq, (frequencies >= lcutFreq) & (frequencies <= hcutFreq), frequencies > hcutFreq],
        [lambda x: 2**(lSlope*(x - lcutFreq)/lcutFreq ), 1, lambda x: 2**(hSlope * ((hcutFreq - x) / (4000 - hcutFreq)))])


        self.ax.clear()


        self.ax.plot(frequencies, response, label='Filter Response')


        # self.ax.set_ylim(0, 11)  # Adjust y-axis limits if necessary
        self.ax.set_title('Combined Filter Characteristics')
        self.ax.set_xlabel('Frequency (Hz)')
        self.ax.set_ylabel('Magnitude')
        self.canvas.draw()

# Function to handle button clicks
    def increase_value(self):
        vol = self.readVolume()
        print(vol)
        vol += 1
        # self.values[0] = vol
        self.calcValues(vol)
        self.writeVolume(vol)
        self.update_plot()

    def decrease_value(self):
        vol = self.readVolume()
        vol = vol - 1
        self.writeVolume(vol)
        #self.values[0] = vol
        self.calcValues(vol)
        self.update_plot()

    def on_closing(self):
        self.root.quit()

    def createMainWindow(self):
    # Create the main window
        self.root = tk.Tk()
        self.root.title("Interactive Bar Plot")

    # Create the figure and axis
        self.fig, self.ax = plt.subplots()

    # Create the canvas for the figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    # Create buttons for each category
        frame = tk.Frame(self.root)
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
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


