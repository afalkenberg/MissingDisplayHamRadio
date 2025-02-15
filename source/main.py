import VolumePlot
import ReceiverAudioFilter

# VP = VolumePlot.VolumePlot(True)
VP = ReceiverAudioFilter.ReceiverAudioFilter('ssb', True)

VP.createMainWindow()

