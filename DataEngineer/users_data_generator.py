import random
import string
import transliterate
import hashlib
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime


def connect_to_database():
    url = f'postgresql+psycopg2://cnrprod-team-58619:gaicaeh3mea7ooza1Ohcozachai6Itei@rc1b-m17jig7pms2njiie.mdb.yandexcloud.net:6432/cnrprod-team-58619'
    engine = create_engine(url)
    conn = engine.connect()
    return conn

# функция для генерации имени
def generate_random_fullname_for_user_table():
    names = ['Иван', 'Александр', 'Михаил', 'Дмитрий', 'Андрей', 'Алексей', 'Сергей', 'Артем', 'Николай', 'Максим', 'Егор', 'Илья', 'Кирилл', 'Даниил', 'Олег', 'Павел', 'Владимир', 'Роман', 'Антон', 'Виктор', 'Глеб', 'Георгий', 'Василий', 'Степан', 'Тимофей', 'Федор', 'Ярослав', 'Вадим', 'Валентин', 'Валерий', 'Виталий', 'Владислав', 'Григорий', 'Денис', 'Евгений', 'Захар']
    surnames = ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Соколов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов', 'Петров', 'Волков', 'Соловьев', 'Васильев', 'Зайцев', 'Павлов', 'Семенов', 'Голубев', 'Виноградов', 'Богданов', 'Воробьев', 'Федоров', 'Михайлов', 'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов', 'Киселев', 'Макаров', 'Андреев', 'Ковалев', 'Ильин', 'Гусев', 'Титов', 'Кузьмин']
    name = random.choice(names)
    surname = random.choice(surnames)
    full_name = name + ' ' + surname
    return full_name

def generate_random_email_for_user_table(random_name):
    name = random_name.split()[0]
    surname = random_name.split()[1]
    latin_name = transliterate.translit(name, reversed=True)
    latin_surname = transliterate.translit(surname, reversed=True)
    email_username = latin_name.lower() + '_' + latin_surname.lower()
    domain = ['gmail.com', 'yahoo.com', 'hotmail.com', 'yandex.ru', 'icloud.com']
    email = email_username + '@' + random.choice(domain)
    email = email.replace("'", "")
    return email

def generate_random_role_for_user_table():
    roles = [1, 2, 3, 4, 5]
    role = random.choice(roles)
    return role

def generate_random_cookie_for_user_table():
    letters = string.ascii_letters + string.digits
    cookie = ''.join(random.choice(letters) for _ in range(8))
    return cookie

def generate_random_password_for_user_table():
    letters = string.ascii_letters
    password = ''.join(random.choice(letters) for _ in range(10))
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    return hash_password


# Создаем пустой датафрейм
df_user = pd.DataFrame(columns=['full_name', 'email', 'role', 'cookie', 'hash_password'])

# Генерируем случайные данные и добавляем их в датафрейм
for i in range(25):
    full_name = generate_random_fullname_for_user_table()
    email = generate_random_email_for_user_table(full_name)
    role = generate_random_role_for_user_table()
    cookie = generate_random_cookie_for_user_table()
    hash_password = generate_random_password_for_user_table()

    df_user.loc[i] = [full_name, email, role, cookie, hash_password]


#%%
def import_user_to_db(df_user):
    conn = connect_to_database()
    try:
        # Импорт данных в БД
        df_user.to_sql('user', con=conn, if_exists='append', index=False, schema='usr')
        print('Data imported to user table')
    except Exception as e:
        print(f'Error importing data to table: {str(e)}')

    log_time = datetime.now()
    log_data = {'start_time': [log_time], 'operation_type': ['import'],
                    'additional_info': [f'Imported user data to db']}
    try:
        df_log = pd.DataFrame(log_data)
        df_log.to_sql('log_table', con=conn, if_exists='append', index=False, schema='lg')
        print('Info appended to log_table')
    except Exception as e:
        print(f'Error info appended to log_table: {str(e)}')
    conn.close()

import_user_to_db(df_user)
