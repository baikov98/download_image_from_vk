import vk_api
import requests

vk_session = vk_api.VkApi('LOGIN', 'PASSWORD')
vk_session.auth()

vk = vk_session.get_api()

tools = vk_api.VkTools(vk_session)

wall = tools.get_all('wall.get', 100, {'owner_id': 777777})#('-777777' FOR GROUP ID)

print('Posts count:', wall['count'])

for i in range(800):
    try:
        url=wall['items'][i]['attachments'][0]['photo']['sizes'][3]['url']
        image = requests.get(url)
        with open(('d'+'new_image'+str(i)+'.png'), 'wb') as f:
            f.write(image.content)
        print("картинка сохранена")
    except:
        print("ошибка")
print("скачивание завершено")
