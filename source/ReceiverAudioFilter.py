import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import CatInterface

class ReceiverAudioFilter:

    def __init__(self, dbg):
        self.catInterface = CatInterface.CatInterface('COM4', 9600, dbg)
        self.lcutFreqRange  = [i for i in range(0,1001, 50)]
        self.minlcutVal = 0
        self.maxlcutVal = 20
        self.lcutVal = 0

        self.hcutFreqRange  = [4000] + [i for i in range(700,4001, 50)]
        self.minhcutVal = 0
        self.maxhcutVal = 67
        self.hcutVal = 0

        
        self.slopeRange = [4, 12]  # 2 = 3db ;  4 = 6db ; 6 = 9dB ; 8 = 12dB ; 10 = 15dB ; 12 = 18db
        self.lSlopeVal = 0
        self.hSlopeVal = 0

        self.debug = dbg
        
    def readData(self, what):
        if what == 'lowFrequency':
            dataReceived = self.catInterface.writeReadCom("EX099;")
            return int(dataReceived[5:7])
        elif what == 'highFrequency':
            dataReceived = self.catInterface.writeReadCom("EX101;")
            return int(dataReceived[5:7])
        elif what == 'lowSlope':
            dataReceived = self.catInterface.writeReadCom("EX100;")
            return int(dataReceived[5:6])
        elif what == 'highSlope':
            dataReceived = self.catInterface.writeReadCom("EX102;")
            return int(dataReceived[5:6])


        else:
            return 42

    def writeData(self, what, data):
        if what == 'lowFrequency':
            if data == 0:
                vString = "EX09900"+";"
            else:
                vString = "EX099"+str(data)+";"
            self.catInterface.writeReadCom(vString)

        elif what == 'highFrequency':
            if data < 10:
                vString = "EX1010"+str(data)+";"
            else:
                vString = "EX101"+str(data)+";"
            self.catInterface.writeReadCom(vString)

        elif what == 'lowSlope':
            vString = "EX100"+str(data)+";"

        elif what == 'highSlope':
            vString = "EX102"+str(data)+";"

        return 42

# Function to update the plot
    def update_plot(self):
        frequencies = np.linspace(0, 4000, 4000)
        self.lcutFreq = self.lcutFreqRange[self.lcutVal]
        self.hcutFreq = self.hcutFreqRange[self.hcutVal]
        self.lSlope = self.slopeRange[self.lSlopeVal]
        self.hSlope = self.slopeRange[self.hSlopeVal]

        response = np.piecewise(frequencies, [frequencies < self.lcutFreq, (frequencies >= self.lcutFreq) & (frequencies <= self.hcutFreq), frequencies > self.hcutFreq],
        [lambda x: 2**(self.lSlope*(x - self.lcutFreq)/self.lcutFreq ), 1, lambda x: 2**(self.hSlope * ((self.hcutFreq - x) / (4000 - self.hcutFreq)))])
        self.ax.clear()
        self.ax.plot(frequencies, response, label='Filter Response')
        self.ax.set_title('Combined Filter Characteristics')
        self.ax.set_xlabel('Frequency (Hz)')
        self.ax.set_ylabel('Magnitude')
        self.canvas.draw()



# Function to handle button clicks
    def lowFrequencyIncrease(self):
        if self.debug == True:
            self.lcutVal = min(self.lcutVal + 1, self.maxlcutVal) 
        else:
            self.lcutVal = self.readData('lowFrequency')
            self.lcutVal = min(self.lcutVal + 1, self.maxlcutVal)
            self.writeData('lowFrequency', self.lcutVal)
        self.update_plot()

    def lowFrequencyDecrease(self):
        if self.debug == True:
            self.lcutVal = max(self.lcutVal - 1, self.minlcutVal) 
        else:
            self.lcutVal = self.readData('lowFrequency')
            self.lcutVal = max(self.lcutVal - 1, self.minlcutVal)
            self.writeData('lowFrequency', self.lcutVal)
        self.update_plot()


    def lowSlopeIncrease(self):
        if self.debug == True:
            self.lSlopeVal = 1
        else:
            self.lSlopeVal = self.readData('lowSlope')
            self.lSlopeVal = 1
            self.writeData('lowSlope', self.lSlopeVal)
        self.update_plot()

    def lowSlopeDecrease(self):
        if self.debug == True:
            self.lSlopeVal = 0
        else:
            self.lSlopeVal = self.readData('lowSlope')
            self.lSlopeVal = 0
            self.writeData('lowSlope', self.lSlopeVal)
        self.update_plot()


    def highFrequencyIncrease(self):
        if self.debug == True:
            self.hcutVal = min(self.hcutVal + 1, self.maxhcutVal) 
        else:
            self.hcutVal = self.readData('highFrequency')
            self.hcutVal = min(self.hcutVal + 1, self.maxhcutVal)
            self.writeData('highFrequency', high)
        self.update_plot()

    def highFrequencyDecrease(self):
        if self.debug == True:
            
            self.hcutVal = max(self.hcutVal - 1, self.minhcutVal)

        else:
            self.hcutVal = self.readData('highFrequency')
            self.hcutVal = max(self.hcutVal - 1, self.minhcutVal) 
            self.writeData('highFrequency', self.hcutVal)
        self.update_plot()


    def highSlopeIncrease(self):
        if self.debug == True:
            self.hSlopeVal = 1
        else:
            self.hSlopeVal = self.readData('highSlope')
            self.hSlopeVal = 1
            self.writeData('highSlope', self.hSlopeVal)
        self.update_plot()

    def highSlopeDecrease(self):
        if self.debug == True:
            self.hSlopeVal = 0
        else:
            high = self.readData('highSlope')
            self.hSlopeVal = 0
            self.writeData('highSlope', self.hSlopeVal)
        self.update_plot()






    def on_closing(self):
        self.root.quit()

    def createMainWindow(self):
    # Create the main window
        self.root = tk.Tk()
        self.root.title("Receiver Audio Filter")

    # Create the figure and axis
        self.fig, self.ax = plt.subplots()

    # Create the canvas for the figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

    # Create buttons for each category
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT, padx=5)

        labelLowFreq = tk.Label(frame, text="low frequency")
        labelLowFreq.grid(row = 0, column = 0, columnspan = 2)                    # (side=tk.TOP)
        buttonLowFreqIncrease = tk.Button(frame, text="+", command=self.lowFrequencyIncrease)
        buttonLowFreqIncrease.grid(row = 1, column = 0)  # (side=tk.LEFT)
        buttonLowFreqDecrease = tk.Button(frame, text="-", command=self.lowFrequencyDecrease)
        buttonLowFreqDecrease.grid(row = 1, column = 1)  # (side=tk.LEFT)

        labelLeftSlope = tk.Label(frame, text="low slope")
        labelLeftSlope.grid(row = 0, column = 2, columnspan = 2)                    # (side=tk.TOP)
        buttonLeftSlopeIncrease = tk.Button(frame, text="+", command=self.lowSlopeIncrease)
        buttonLeftSlopeIncrease.grid(row = 1, column = 2)  # (side=tk.LEFT)
        buttonLeftSlopeDecrease = tk.Button(frame, text="-", command=self.lowSlopeDecrease)
        buttonLeftSlopeDecrease.grid(row = 1, column = 3)  # (side=tk.LEFT)


        labelHighFreq = tk.Label(frame, text="high frequency")
        labelHighFreq.grid(row = 0, column = 4, columnspan = 2)                    # (side=tk.TOP)
        buttonHighFreqIncrease = tk.Button(frame, text="+", command=self.highFrequencyIncrease)
        buttonHighFreqIncrease.grid(row = 1, column = 4)  # (side=tk.LEFT)
        buttonHighFreqDecrease = tk.Button(frame, text="-", command=self.highFrequencyDecrease)
        buttonHighFreqDecrease.grid(row = 1, column = 5)  # (side=tk.LEFT)

        labelRightSlope = tk.Label(frame, text="high slope")
        labelRightSlope.grid(row = 0, column = 6, columnspan = 2)                    # (side=tk.TOP)
        buttonRightSlopeIncrease = tk.Button(frame, text="+", command=self.highSlopeIncrease)
        buttonRightSlopeIncrease.grid(row = 1, column = 6)  # (side=tk.LEFT)
        buttonRightSlopeDecrease = tk.Button(frame, text="-", command=self.highSlopeDecrease)
        buttonRightSlopeDecrease.grid(row = 1, column = 7)  # (side=tk.LEFT)









    # Initial plot update
        self.update_plot()

    # Run the Tkinter event loop
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()


