import main
import subprocess
import os
import time

def parse(channel_name):
    command = f"snscrape --max-results 1 --jsonl telegram-channel {channel_name} > {channel_name}.json"

    try:
        subprocess.run(command, shell=True, check=True)
        print("Команда успешно выполнена.")
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка при выполнении команды: {e}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")


channel_name = input()
start_time = time.time()
channel_dict = {}
while time.time() - start_time < 60:
    parse(channel_name=channel_name)
    file_root = rf'D:\random_ ML_projects\tg_channels_parser\{channel_name}.json'

    channel_dict = main.file(file_root)
    contents = list(channel_dict.keys())
    print(contents[0])
    time.sleep(5)
os.remove(file_root)
