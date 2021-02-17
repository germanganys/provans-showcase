import vk_api
import secrets

from vk_api.utils import get_random_id


class VKNotifier:
    def __init__(self):
        self.api_key = '*****'
        self.user_id = '*****'
        self.vk = vk_api.VkApi(token=self.api_key)

    def notify(self, message):
        self.vk.method('messages.send', {'user_id': self.user_id, 'message': message, 'random_id': get_random_id()})


def generate_coupon_code(lenght: int) -> str:
    ALPHABET = '**************'
    return ''.join([secrets.choice(ALPHABET) for _ in range(lenght)])


