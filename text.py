import subprocess
print(subprocess.run('ls'))
print((subprocess.run(["v4l2-ctl","--list-devices"])))
print('hello')