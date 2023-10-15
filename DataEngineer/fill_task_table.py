from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
import os

def connect_to_database():
    url = f'postgresql+psycopg2://cnrprod-team-58619:gaicaeh3mea7ooza1Ohcozachai6Itei@rc1b-m17jig7pms2njiie.mdb.yandexcloud.net:6432/cnrprod-team-58619'
    engine = create_engine(url)
    conn = engine.connect()
    return conn


def log_operation(connection, operation_type, additional_info, task_id):
    current_time = datetime.now()
    query = f"INSERT INTO lg.log_table (start_time, operation_type, additional_info, task_id) " \
            f"VALUES ('{current_time}', '{operation_type}', '{additional_info}', {task_id})"
    connection.execute(query)


def import_data_from_csv(delta_dir):
    connection = connect_to_database()
    # Получаем список всех поддиректорий в директории delta_dir
    subdirs = [subdir for subdir in os.listdir(delta_dir) if os.path.isdir(os.path.join(delta_dir, subdir)) and subdir != 'all_tasks']

    # Сортируем поддиректории по номеру
    subdirs.sort(key=lambda x: int(x[5:]))
    for subdir in subdirs:
        subdir_path = os.path.join(delta_dir, str(subdir))
        project_number = int(subdir.replace("tasks", ""))
        files = sorted([file for file in os.listdir(subdir_path) if file.endswith('.csv')])
        # проходим по файлам с тасками в формате csv
        for file in files:
            file_path = os.path.join(subdir_path, file)
            # Читаем CSV файл как DataFrame
            df_task = pd.read_csv(file_path)

            df_task = df_task.rename(columns={'issue_id': 'id',
                                              'created_on': 'date_creation',
                                              'closed_on': 'due_date',
                                              'status_id': 'status',
                                              'subject': 'name',
                                              'description': 'description',
                                              'assigned_to_id': 'assignee_id',
                                              'parent_id': 'parent_task_id'
                                              })
            df_task.info()
            df_task.fillna(0, inplace=True)
            nan_counts = df_task.isna().sum()
            null_counts = df_task.isnull().sum()
            if sum(nan_counts+null_counts) != 0:
                print("не удалось удалить NaN и NULL")
                break

            # задаем правильные типы данных для загрузки в бд
            df_task['id'] = df_task['id'].astype(int)
            df_task['date_creation'] = pd.to_datetime(df_task['date_creation'], format='%Y-%m-%d %H:%M:%S',
                                                      errors='coerce')
            df_task['due_date'] = pd.to_datetime(df_task['due_date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
            df_task['status'] = df_task['status'].astype(int)
            df_task['name'] = df_task['name'].astype(object)
            df_task['description'] = df_task['description'].astype(object)
            df_task['assignee_id'] = df_task['assignee_id'].astype(int)
            df_task['parent_task_id'] = df_task['parent_task_id'].astype(int)
            df_task['parent_task_id'] = df_task['parent_task_id'].replace(0, pd.NA)
            df_task['project_id'] = project_number
            try:
                # Импорт данных в БД
                df_task.to_sql('task', con=connection, if_exists='append', index=False, schema='prjct')
                print('Data imported to new table')
            except Exception as e:
                print(f'Error importing data to table: {str(e)}')

            log_time = datetime.now()
            log_data = {'start_time': [log_time], 'operation_type': ['import'],
                        'additional_info': [f'Imported data from {file_path}'], 'task_id': [project_number]}
            try:
                df_log = pd.DataFrame(log_data)
                df_log.to_sql('log_table', con=connection, if_exists='append', index=False, schema='lg')
                print('Info appended to log_table')
            except Exception as e:
                print(f'Error info appended to log_table: {str(e)}')
    connection.close()

import_data_from_csv('data_tasks')




