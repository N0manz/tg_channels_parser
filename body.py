import reforming_data
import subprocess
import os
import time
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import asyncio


bot = Bot(token='5896988779:AAEHmIs5L7PvVh_QTPjPu8n5ZIxiJFYZVaU')
dp = Dispatcher()
channels_names = []


@dp.message(F.text == '/start')
async def cmd_start(message:Message):
    await message.answer('Добро пожаловать этот бот предназначен для создания аналога ленты из ВК в Телеге, но это только гига-раняя альфа так что сосите')


from aiogram.filters import CommandObject, Command
@dp.message(Command("add"))
async def cmd_name(message: Message, command: CommandObject):
    if command.args:
        await message.answer(f"вы добавили канал {command.args}")
        channel_name = command.args
        channel_name = channel_name[channel_name.find('me/') + len('me/'):]
        print(channel_name)
        channels_names.append(channel_name)
    else:
        await message.answer("еблан укажи тг-канал после add")


@dp.message(F.text == '/parse')
async def send_message_to_user(message:Message):


    channel_dict = {}
    posts = set()

    while True:

        for channel_name in channels_names:

            parse(channel_name=channel_name)
            file_root = rf'..\tg_channels_parser\{channel_name}.json'
            channel_dict = reforming_data.file(file_root)
            contents = list(channel_dict.keys())
            url = list(channel_dict.values())


            if (contents[0] not in posts) and (contents[0] != 'null'):
                posts.add(contents[0])
                print(contents[0])
                print(url[0])
                text = f"Новый пост в канале {channel_name}:\n{contents[0]}\nСсылка на исходный пост: {url[0]}"
                await message.answer(text)

        time.sleep(5)
    os.remove(file_root)

    


def parse(channel_name):
    command = f"snscrape --max-results 1 --jsonl telegram-channel {channel_name} > {channel_name}.json"

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка при выполнении команды: {e}")
    except Exception as e:
        print(f"Произошла неожиданная ошибка: {e}")


#inputs_channels = list(map(str, input().split()))


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())