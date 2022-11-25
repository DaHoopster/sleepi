import subprocess


"""
binary: /usr/bin/mplayer
args  : [binary] -ao alsa:device=hw=0 $1 -loop $2 </dev/null >/dev/null 2>&1
"""

CMD_MPLAYER = '/usr/bin/mplayer'
CMD_ALSA_ARG1 = '-ao'
CMD_ALSA_ARG2 = 'alsa:device=hw=0'
CMD_TAIL = '</dev/null >/dev/null 2>&1'

SOUND_FILE_ROOT_PATH = '/home/pi/Documents/white-noise/'
WHITE_NOISES = {
    'range_hood': 'range-hood-white-noise.mp3',
    'microwave': 'microwave-white-noise.mp3',
    'thunderstorm': 'thunderstorm-white-noise.mp3',
    'brook': 'brook-white-noise.mp3',
    'forest': 'forest-white-noise.mp3',
    'ocean_waves': 'ocean-waves-white-noise.mp3'
}

class WhiteNoiseControl:
  class __PlayerProcess:
    def __init__(self):
      self._proc = None


    def set_proc(self, proc=None):
      self._proc = proc


    def terminate(self):
      if self._proc:
        self._proc.terminate()


    
    def poll(self):
      if self._proc:
        self._proc.poll()



    def __str__(self):
        return f'{repr(self)} - {self._proc.pid if self._proc else None}'


  player_process = None


  def __init__(self):
    if not WhiteNoiseControl.player_process:
      WhiteNoiseControl.player_process = WhiteNoiseControl.__PlayerProcess()


  def start(self, noise_type=None, loop=1):
    if WhiteNoiseControl.player_process and not WhiteNoiseControl.player_process.poll():
      WhiteNoiseControl.player_process.terminate()

    WhiteNoiseControl.player_process.set_proc(proc=subprocess.Popen(
        [
            CMD_MPLAYER,
            CMD_ALSA_ARG1,
            CMD_ALSA_ARG2,
            f"{SOUND_FILE_ROOT_PATH}/{WHITE_NOISES[noise_type]}",
            '-loop',
            f'{loop}',
            CMD_TAIL
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    ))



  def stop(self):
    WhiteNoiseControl.player_process.terminate()


if __name__ == '__main__':
  wn = WhiteNoiseControl()
  wn.start(noise_type='microwave', loop=1)

