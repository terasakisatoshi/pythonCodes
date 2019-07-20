from kivy.app import App
from kivy.clock import Clock
import subprocess
import threading
import psutil
import time
"""
reference:
https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
"""
def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


class SubprocessThread(threading.Thread):

    def __init__(self, app, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.app = app
        self.stop_event = False

    def run(self):
        def get_line(proc):
            while True:
                line = proc.stdout.readline()
                if line:
                    yield line.decode('utf-8')

                if not line and proc.poll() is not None:
                    break

        proc = subprocess.Popen(
                self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        
        for line in get_line(proc):
            if self.stop_event:
                kill(proc.pid)
                break
            self.app.root.ids.output.text += line
        self.app.state = TerminalApp.DONE

    def stop(self):
        self.stop_event = True


class TerminalApp(App):
    STOP, COMPUTING, DONE, CANCELED = 0, 1, 2, 3
    thread_start = False
    state = STOP

    def check_state(self, nap):
        if self.state == TerminalApp.DONE:
            print("DONE")
            self.thread_start = not self.thread_start
            print("try to stop thread")
            self.cmd_thread.stop()
            self.state = TerminalApp.STOP

        if self.state == TerminalApp.CANCELED:
            print("CANCELED")
            self.thread_start = not self.thread_start
            print("try to stop thread")
            self.cmd_thread.stop()
            time.sleep(1)
            self.state = TerminalApp.STOP

        if self.state == TerminalApp.COMPUTING:
            print("COMPUTING")
            self.root.ids.button.text = 'Stop'

        if self.state == TerminalApp.STOP:
            print("STOP")
            self.root.ids.button.text = 'Exec'
            Clock.unschedule(self.check_state)

    def start_command(self):
        if not self.thread_start:
            cmd = self.root.ids.command.text
            self.cmd_thread = SubprocessThread(self, cmd)
            self.cmd_thread.start()
            self.thread_start = not self.thread_start
            self.state = TerminalApp.COMPUTING
            Clock.schedule_interval(self.check_state, 0.1)
        else:
            self.state = TerminalApp.CANCELED


def main():
    TerminalApp().run()

if __name__ == '__main__':
    main()
