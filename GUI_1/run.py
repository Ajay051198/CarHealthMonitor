import os
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
change_dir_cmd = "cd " + current_dir
print(change_dir_cmd)
os.system(change_dir_cmd)
os.system("python tkinter.py")
