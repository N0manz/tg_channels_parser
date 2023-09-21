import subprocess
command = "snscrape --max-results 5 --jsonl telegram-channel rybar > rybar.json"

try:
    subprocess.run(command, shell=True, check=True)
    print("Команда успешно выполнена.")
except subprocess.CalledProcessError as e:
    print(f"Произошла ошибка при выполнении команды: {e}")
except Exception as e:
    print(f"Произошла неожиданная ошибка: {e}")


