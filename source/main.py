import VolumePlot
import ReceiverAudioFilter

# VP = VolumePlot.VolumePlot(True)


root = ReceiverAudioFilter.tk.Tk()
root.withdraw()  # Hide the root window

VP1 = ReceiverAudioFilter.ReceiverAudioFilter('cw', True)
VP2 = ReceiverAudioFilter.ReceiverAudioFilter('ssb', True)
VP3 = ReceiverAudioFilter.ReceiverAudioFilter('am', True)
VP4 = ReceiverAudioFilter.ReceiverAudioFilter('fm', True)
VP5 = ReceiverAudioFilter.ReceiverAudioFilter('data', True)
VP6 = ReceiverAudioFilter.ReceiverAudioFilter('rtty', True)

VP1.createMainWindow(100, 100)
VP2.createMainWindow(522, 100)
VP3.createMainWindow(944, 100)
VP4.createMainWindow(100, 512)
VP5.createMainWindow(522, 512)
VP6.createMainWindow(944, 512)

root.mainloop()
