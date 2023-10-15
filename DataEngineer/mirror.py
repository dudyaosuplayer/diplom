#%%
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import Window
from pyspark.sql.functions import row_number
from pyspark.sql import functions as F
from datetime import datetime
import logging

# Создание SparkSession
spark = SparkSession.builder.appName('Mirror Builder').getOrCreate()


#%%
def create_directory(directory_path):
    # Проверить, существует ли директория
    if not os.path.exists(directory_path):
        # Если не существует, то создать
        os.makedirs(directory_path)
        print(f"Директория {directory_path} успешно создана.")
    else:
        print(f"Директория {directory_path} уже существует.")


#%%
def write_delta_to_log(file, start_time, end_time):
    # Создаем DataFrame с информацией о дельте
    log_df = spark.createDataFrame([(file, start_time, end_time)], ['file', 'start_time', 'end_time'])
    # Добавляем информацию о дельте в лог-файл
    log_df.write.mode('append').csv('spark_mirrors/logs_deltas/logs_deltas.csv',  sep="\t", header=True)


#%%
def check_if_delta_processed(file):
    # Загружаем DataFrame с данными о ранее обработанных дельтах
    log_path = 'spark_mirrors/logs_deltas/logs_deltas.csv'
    processed_deltas = spark.read.csv(log_path, sep="\t", header=True)
    # Проверяем наличие имени дельты в DataFrame
    if processed_deltas.filter(processed_deltas.file.like(f"%{file}%")).isEmpty():
        return False
    return True

#%%
def check_mirror(mirror):
    mirror_path = mirror
    try:
        mirror = spark.read.csv(mirror_path, sep="\t", header=True)
        # проверяем наличие информации в зеркале
        if mirror.isEmpty():
            return False
        return True
    except:
        print("еще нет файла-зеркала")


#%%
def process_deltas(delta_dir, table_name, key_fields):
    subdirs = sorted(
        [int(subdir) for subdir in os.listdir(delta_dir) if os.path.isdir(os.path.join(delta_dir, subdir))])
    # Получить путь к первой директории дельты
    first_delta_dir = os.path.join(delta_dir, str(subdirs[0]))
    # Получить список CSV-файлов в первой директории дельты
    files = sorted([file for file in os.listdir(first_delta_dir) if file.endswith('.csv')])
    # Получить путь к первому CSV-файлу
    first_file_path = os.path.join(first_delta_dir, files[0])
    # Прочитать первый CSV-файл как датафрейм
    first_df = spark.read.csv(first_file_path, sep=';', header=True, inferSchema=True)
    # Получить схему датафрейма
    schema = first_df.schema
    union_df = spark.createDataFrame([], schema)
    for subdir in subdirs:
        subdir_path = os.path.join(delta_dir, str(subdir))
        files = sorted([file for file in os.listdir(subdir_path) if file.endswith('.csv')])

        for file in files:
            file_path = os.path.join(subdir_path, file)
            # Проверка, была ли обработана эта дельта ранее
            # Проверяем, была ли эта дельта уже обработана
            if check_if_delta_processed(file):
                print(f"Дельта {file} уже обработана, пропускаем")
                continue
            if check_mirror(table_name):
                union_df = spark.read.csv(table_name, sep='\t', header=True)
            # Создание столбца с текущей датой и временем старта загрузки

            start_time = datetime.now()
            # Читаем CSV файл как DataFrame
            df = spark.read.csv(file_path, sep=';', header=True, inferSchema=True)
            print('file: ', file, ' df.count: ', df.count())
            union_df = union_df.unionAll(df)

            # Определить порядок сортировки и окно для числовой нумерации состояний каждой сущности
            window_spec = Window.orderBy(F.desc("DATA_ACTUAL_DATE")).partitionBy(key_fields)
            df_with_row_number = union_df.withColumn("row_number", F.row_number().over(window_spec))
            df_with_row_number.show()
            mirror_df = df_with_row_number.filter(F.col("row_number") == 1)
            mirror_df = mirror_df.drop("row_number")
            mirror_df.show(50)
            mirror_df.write.mode("overwrite").csv(table_name, sep="\t", header=True)
            # Получение текущей даты и времени завершения загрузки
            end_time = datetime.now()
            write_delta_to_log(file, start_time, end_time)
            log_df_check = spark.read.csv('spark_mirrors/logs_deltas/logs_deltas.csv', sep="\t", header=True)
            print('log_df_check.count: ', log_df_check.count())
            log_df_check.show(50)

#%%
write_delta_to_log('check', datetime.now(), datetime.now())
#%%
delta_dir='spark_mirrors/data_deltas'
table_name='spark_mirrors/md_account/mirr_md_account_d.csv'
#key_fields=['ACCOUNT_RK', 'ACCOUNT_NUMBER', 'CHAR_TYPE', 'CURRENCY_RK', 'CURRENCY_CODE', 'CLIENT_ID', 'BRANCH_ID', 'OPEN_IN_INTERNET']
key_fields='ACCOUNT_RK'
#%%
process_deltas(delta_dir, table_name, key_fields)

#%%
log_df_checks = spark.read.csv('spark_mirrors/logs_deltas/logs_deltas.csv', sep="\t", header=True)
print('log_df_check.count: ', log_df_checks.count())
log_df_checks.show(50)

#%%
create_directory('spark_mirrors/logs_deltas')
create_directory('spark_mirrors/md_account')
#%%
check_df = spark.read.csv('spark_mirrors/md_account/mirr_md_account_d.csv', sep="\t", header=True)
print('check_df.count: ', check_df.count())
check_df.show(50)
