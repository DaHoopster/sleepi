# Sleepi

When my first son was born, we needed a white noise machine to put him to sleep because he was very sensitive to sound. For some odd
reason, I didn't want to spend the money on an off-the-shelf product. It was also during the early days of the COVID lockdown, so a
DIY idea came to me 💡 why not putting my old Raspberry Pi v1, a speaker, and an AUX cable to work and build one myself?

After a few days of tinkering, Sleepi was created and my first son was sleeping soundingly under the soothing(?) sound of a microwave oven 😂.

I'd like to share the code and setup instructions with fellow (new)dads who want to make the baby bonding time a bit more fun.

## What you need

* Raspberry Pi x 1 (though I am using the original Raspberry Pi, newer ones will probably work better)
* a speaker
* an AUX cable

## Prerequisites

You are familiar with Raspberry Pi, Linux, and Python.

You need a couple of packages

```
sudo apt-get update && sudo apt-get install mplayer supervisor
```

You need python3, whether it's a system wide python3 package or a version of python3 managed by a python version manager such as `pyenv`.

## Install Sleepi

1. Check out the code to a directory in your Raspberry Pi (e.g. /home/pi/Projects)

```
cd ~/gadgets
git clone git@github.com:DaHoopster/sleepi.git
```

2. Set up Python virtual env and pull down the dependencies

```
cd ~/Projects/sleepi
python -m venv ~/.virtualenv/sleepi
source ~/.virtualenv/sleepi/bin/activate
pip install -r requirements.txt
```

3. Copy the mp3 files

```
mkdir ~/Documents/sleepi
cp ./media/*.mp3 ~/Documents/sleepi
```

4. Copy the `supervisor` conf for Sleepi to the system supervisor config dir

```
sudo cp sleepi_supervisor.conf /etc/supervisor/conf.d/
```

5. Reload supervisor

```
sudo supervisorctl reload
```

6. You should be able to point your browser(desktop or mobile) to `http://<IP_OR_DOMAIN_NAME_OF_YOUR_PI>:5000` and see the web UI.
7. Each mp3 file is 30 minutes in length. By default, the web UI will play each mp3 file twice which gives you an hour of soothing sleep-inducing
sound. If you press the big red stop sign button, the sound will stop.

