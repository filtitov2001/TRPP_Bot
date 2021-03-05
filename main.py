import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import re
import locale




def main():
    nomer = 0
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')  # для получения даты на русском
    vk_session = vk_api.VkApi(
        token='943d976fd89420888a69ccdeba641e48f71dc04095ca8efe0d77dc72f37574298c4e50dbc517bbb63bf8e')
    vk = vk_session.get_api()