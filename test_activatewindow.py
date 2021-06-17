import gi

gi.require_version('Wnck', '3.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Wnck

# import pygtk
# pygtk.require('2.0')
# import gtk
# import wnck
import re
import sys
import time

screen = Wnck.Screen.get_default()
while Gtk.events_pending():
    Gtk.main_iteration()
win_name='Win'
titlePattern = re.compile(f'.*{win_name}.*')

windows = screen.get_windows()
for w in windows:
    if titlePattern.match(w.get_name()):
        print(w.get_name())
        w.activate(int(time.time()))

