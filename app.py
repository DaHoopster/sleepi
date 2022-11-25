from flask import Flask
from flask import request, redirect, render_template

from white_noise_control import WhiteNoiseControl

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/control', methods=['POST'])
def control_form():
  control_value = request.form['control_action']
  loop_value = request.form['loop']
  loop = 24 if loop_value == '' else int(loop_value)

  wnc = WhiteNoiseControl()
  
  if control_value == 'stop':
    wnc.stop()
  else:
    noise_type = control_value[6:]
    wnc.start(noise_type=noise_type, loop=int(loop))

  return redirect('/')

