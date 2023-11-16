"""生成假数据并写入数据库"""
import time
from utils.faker_data import fake_data_generator
from utils.db_utils import oracle_db


def generate_fake_data(num):
    """获取假数据"""
    return fake_data_generator.generate_demo_fake_data(num)


def init_sql(path=r'C:\Users\19096\Desktop\develop_utils\conf\fjgz_clom.txt', table='"ETL"."fjgz"'):
    with open(path, 'r', encoding='utf-8') as f:
        clom = f.readlines()
        cloms = [f'"{clom}"'.replace('\n', '') for clom in clom]
    # val = [f":{index}" for index in range(1, len(clom) + 1)]
        sql = 'INSERT INTO {}  {}  VALUES  {}'.format(table, tuple(cloms), '{}').replace("'", '')
        # print(sql)
        return sql


def excute_insert(data):
    """
    传入单条假数据，执行插入
    :param data:
    :return:
    """
    sql = init_sql(path=r'C:\Users\19096\Desktop\develop_utils\conf\demo.txt', table='"ETL"."demo"')
    task_data = tuple(data[0].values())
    insert_data(sql, task_data)


def insert_data(sql, data_tuple):
    """
    组装sql，插入数据
    :param sql:数据库插入sql语句
    :param data_tuple:数据元组
    :return:
    """
    data = str(data_tuple).replace('"', '')
    time.sleep(0.1)
    sql = sql.format(data)
    oracle_db.insert_data(sql)


def input_oracle():
    fake_data = list(map(generate_fake_data, list(range(1, 1001))))
    list(map(excute_insert, fake_data))


if __name__ == '__main__':
    input_oracle()
    # for _ in range(5):
    #     thread = threading.Thread(target=input_oracle)
    #     # thread2 = threading.Thread(target=input_oracle)
    #     # thread3 = threading.Thread(target=input_oracle)
    #     # thread4 = threading.Thread(target=input_oracle)
    #     # thread5 = threading.Thread(target=input_oracle)
    #     thread.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    # thread5.start()
