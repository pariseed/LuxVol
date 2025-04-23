from jnius import autoclass
import os


######################################################################BRIGHTNESS
# Prevent Kivy from initializing GUI components
os.environ['KIVY_NO_ARGS'] = '1'
#os.environ['KIVY_NO_CONSOLELOG'] = '1'

# Import Android classes
Intent = autoclass('android.content.Intent')
PythonActivity = autoclass('org.kivy.android.PythonActivity')

# Create and start intent
intent = Intent("com.android.intent.action.SHOW_BRIGHTNESS_DIALOG")
PythonActivity.mActivity.startActivity(intent)



#########################################################################VOLUME
# Import Android classes
Context = autoclass('android.content.Context')
AudioManager = autoclass('android.media.AudioManager')

# Get the current activity
current_activity = PythonActivity.mActivity

# Get the audio service
audio_service = current_activity.getSystemService(Context.AUDIO_SERVICE)
# No need for cast - directly use as AudioManager
audio_manager = audio_service

# Show volume panel
audio_manager.adjustVolume(AudioManager.ADJUST_SAME, AudioManager.FLAG_SHOW_UI)



# Exit
PythonActivity.mActivity.finish()
os._exit(0)
