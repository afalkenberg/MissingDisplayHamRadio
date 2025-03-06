import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import CatInterface


# Sample data

class VolumePlot:

    def __init__(self, com, bd, dbg):
        self.debug = dbg
        self.categories = ['0-9', '10-19', '20-29', '30-39', '40-49']
        self.values = np.array([1, 3, 7, 3, 1])
        self.catInterface = CatInterface.CatInterface(com, bd, self.debug)
        self.mainVol = 0

    def calcValues(self, vol):
        v = 50*vol/256
        self.values[4] = min(10, v-40)
        self.values[3] = min(10, v-30)
        self.values[2] = min(10, v-20)
        self.values[1] = min(10, v-10)
        self.values[0] = min(10, v)
        
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
        self.ax.set_ylim(0, 11)  # Adjust y-axis limits if necessary
        self.ax.set_title('Volume')
        self.ax.set_xlabel('')
        self.ax.set_ylabel('')
        self.canvas.draw()

# Function to handle button clicks
    def increase_value(self):
        if self.debug == False: 
            self.mainVol = self.readVolume()
        print(self.mainVol)
        self.mainVol += 1
        self.calcValues(self.mainVol)
        self.writeVolume(self.mainVol)
        self.update_plot()

    def decrease_value(self):
        if self.debug == False: 
            self.mainVol = self.readVolume()
        self.mainVol = self.mainVol - 1
        self.writeVolume(self.mainVol)
        self.calcValues(self.mainVol)
        self.update_plot()

    def value_changed(self, event):
        if self.debug == False: 
            self.mainVol = self.readVolume()
        self.mainVol = self.value_slider.get()
        self.writeVolume(self.mainVol)
        self.calcValues(self.mainVol)
        self.update_plot()


    def on_closing(self):
        self.root.quit()

    def createMainWindow(self, x, y):
    # Create the main window
        # self.root = tk.Tk()
        # self.root.title("Interactive Bar Plot")

        self.root = tk.Toplevel()  # was Tk()
        self.root.title("Volume Plot")
        self.root.geometry(f"+{x}+{y}")
        self.root.geometry("420x380")


    # Create the figure and axis
        self.fig, self.ax = plt.subplots(figsize=(4.2, 3.25), dpi=100)

    # Create the canvas for the figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    # Create buttons for each category
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT, padx=5)

        label = tk.Label(frame, text='0-49')
        label.pack(side=tk.TOP, anchor=tk.CENTER)

        #btn_increase = tk.Button(frame, text="+", command=self.increase_value)
        #btn_increase.pack(side=tk.LEFT)

        #btn_decrease = tk.Button(frame, text="-", command=self.decrease_value)
        #btn_decrease.pack(side=tk.LEFT)

        self.value_slider = tk.Scale(frame, from_=0, to=256, orient='horizontal', command=self.value_changed, showvalue=False, length=300)
        self.value_slider.pack(anchor=tk.CENTER, padx=100)


    # Initial plot update
        self.update_plot()

    # Run the Tkinter event loop
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # self.root.mainloop()


