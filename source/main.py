import VolumePlot
import ReceiverAudioFilter
import sys


com = 'COM4'
bd = 9600
dbg = True

for argInd in range(1,len(sys.argv), 2):
	print(argInd)
	print(sys.argv[argInd])
	if sys.argv[argInd] in ["-com", "-COM"]:
		com = sys.argv[argInd+1]
	if sys.argv[argInd] in ["-bd", "-baud", "-rate", "-BD","-BAUD"]:
		bd = int(sys.argv[argInd+1])
	if(sys.argv[argInd] in ["-dbg","-DBG","-debug","-DEBUG"]):
		dbg = sys.argv[argInd+1].lower() in ["true", "1", "yes", "y", "t"]

print(com)
print(dbg)



root = ReceiverAudioFilter.tk.Tk()
root.withdraw()  # Hide the root window

VP = VolumePlot.VolumePlot(com, bd, dbg)
VP1 = ReceiverAudioFilter.ReceiverAudioFilter('cw', com, bd, dbg)
VP2 = ReceiverAudioFilter.ReceiverAudioFilter('ssb', com, bd, dbg)
VP3 = ReceiverAudioFilter.ReceiverAudioFilter('am', com, bd, dbg)
VP4 = ReceiverAudioFilter.ReceiverAudioFilter('fm', com, bd, dbg)
VP5 = ReceiverAudioFilter.ReceiverAudioFilter('data', com, bd, dbg)
VP6 = ReceiverAudioFilter.ReceiverAudioFilter('rtty', com, bd, dbg)

VP1.createMainWindow(100, 100)
VP2.createMainWindow(522, 100)
VP3.createMainWindow(944, 100)
VP4.createMainWindow(100, 512)
VP5.createMainWindow(522, 512)
VP6.createMainWindow(944, 512)

VP.createMainWindow(944 + 422, 100)

root.mainloop()
