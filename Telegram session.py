import os
from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
api_id = 123456
api_hash = 'bbbbb'
session_dir = 'sessions'
if not os.path.exists(session_dir):
    os.makedirs(session_dir)

def create_session():
    phone = input("请输入手机号 (带国家码，如 +86138xxx): ")
    session_name = input("请输入保存的文件名 (不带后缀): ")
   
    session_path = os.path.join(session_dir, session_name)
    client = TelegramClient(session_path, api_id, api_hash)
    
    client.connect()
    
    if not client.is_user_authorized():
        sent = client.send_code_request(phone)
        code = input(f'验证码已发送至 {phone}，请输入: ')
        
        try:
            client.sign_in(phone, code)
        except SessionPasswordNeededError:
            password = input('该账号开启了两步验证，请输入2FA密码: ')
            client.sign_in(password=password)
    
    print(f"\n✅ 协议转换成功！")
    print(f"文件位置: {os.path.abspath(session_path)}.session")
    client.send_message('me', '协议转换成功！作者 @ccking1337')
    client.disconnect()
if __name__ == '__main__':
    try:
        create_session()
    except Exception as e:+17019876417