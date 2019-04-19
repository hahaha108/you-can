import subprocess


def parse(url,video_id,path=None):
    command = ['you-get',str(url)]
    video = {}
    video['url'] = url
    video['video_id'] = video_id
    if path:
        command += ['-O',path]
    print(command)
    stdout,stderr = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,encoding='utf-8').communicate()

    if stderr:
        return False
    return video


def you_get():
    pass