import gi

gi.require_version('Wnck', '3.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Wnck
from gi.repository import Gtk


def test_do_when_window_opened_simple():
    Gtk.init([])
    screen: Wnck.Screen = Wnck.Screen.get_default()
    screen.force_update()

    def do_window_opened(this_screen: Wnck.Screen, opened_window: Wnck.Window):
        print('hello')
        app: Wnck.Application = opened_window.get_application()
        app_name = app.get_name()
        print('app name -> ' + app_name)
        print('window name -> ' + opened_window.get_name())

    screen.connect('window-opened', do_window_opened)

    Gtk.main()


if __name__ == '__main__':
    test_do_when_window_opened_simple()