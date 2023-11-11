from faker import Faker
from collections import OrderedDict
from db_utils import OracleHandler
from conf.setting import con_config, fjgz_sql, fjgz_clom

fake = Faker(locale='zh_CN')


class FakeDataGenerator:
    def get_fake_data_list(self):
        """获取飞机故障假数据"""
        data = [
            ("问题id", fake.uuid4()),
            ("问题编号", fake.uuid4()[:8]),
            ("表单格式类型", fake.random_element(["A", "B", "C"])),
            ("问题类型", fake.random_element(["技术问题", "设备问题", "人员问题"])),
            ("问题性质", fake.random_element(["紧急", "一般", "普通"])),
            ("发布日期", fake.date_this_year()),
            ("发布研究室ID", fake.uuid4()[:8]),
            ("发布研究室名称", fake.company()[:20]),
            ("发布部门ID", fake.uuid4()[:8]),
            ("发布部门名称", fake.company()[:20]),
            ("发布人ID", fake.uuid4()[:20]),
            ("发布人名称", fake.name()[:20]),
            ("发布方式", fake.random_element(["邮件", "电话", "会议"])),
            ("适用阶段", fake.random_element(["初期", "中期", "后期"])),
            ("适用阶段补充说明", fake.sentence()[:20]),
            ("处理状态", fake.random_element(["待处理", "处理中", "已解决"])),
            ("问题星级", fake.random_int(min=1, max=5)),  # int
            ("重要度等级", fake.random_element(["高", "中", "低"])),
            ("标题", fake.sentence()[:20]),
            ("机型ID", fake.uuid4()[:8]),
            ("批次", fake.uuid4()[:8]),
            ("机号", fake.uuid4()[:8]),
            ("飞机ID", fake.uuid4()[:20]),
            ("出厂编号", fake.uuid4()[:6]),
            ("架次", fake.random_element(["第一架", "第二架", "第三架"])),
            ("任务课目", fake.word()[:20]),
            ("地区/战区", fake.word()[:20]),
            ("用户/部队", fake.word()[:20]),
            ("发生地点", fake.word()[:20]),
            ("发生日期", fake.date_this_year()),
            ("问题接收人", fake.name()),
            ("收集方式", fake.random_element(["电话", "邮件", "现场"])),
            ("现场问题处理单编号", fake.uuid4()[:8]),
            ("发现时机", fake.random_element(["日常检查", "飞行中发现", "地面维护"])),
            ("判明方式", fake.random_element(["现场检查", "数据分析", "实验验证"])),
            ("故障影响", fake.sentence()[:20]),
            ("故障影响说明", fake.sentence()[:20]),
            ("问题描述", fake.text()[:20]),
            ("所属系统", fake.word()[:20]),
            ("故障件名称", fake.word()[:20]),
            ("故障件型号", fake.word()[:20]),
            ("故障件号", fake.uuid4()[:4]),
            ("故障件安装位置", fake.word()[:20]),
            ("故障件研制状态", fake.word()[:20]),
            ("责任厂家", fake.company()),
            ("厂家责任人", fake.name()),
            ("厂家联系方式", fake.phone_number()),
            ("责任人ID", fake.uuid4()),
            ("责任人名称", fake.name()),
            ("责任部门ID", fake.uuid4()[:8]),
            ("责任部门名称", fake.word()[:20]),
            ("责任专业ID", fake.uuid4()[:8]),
            ("责任专业名称", fake.word()[:20]),
            ("相关专业ID", fake.uuid4()[:8]),
            ("相关专业名称", fake.word()[:20]),
            ("专业会签", fake.word()[:20]),
            ("是否重复相似问题", fake.random_element(["是", "否"])),
            ("重复相似问题分类", fake.word()[:20]),
            ("实际完成时间", fake.date_this_year()),
            ("外场处理情况", fake.text()[:20]),
            ("原因分析", fake.text()[:20]),
            ("专业意见", fake.text()[:20]),
            ("解决措施及说明", fake.text()[:20]),
            ("问题解决方式", fake.word()[:20]),
            ("排故对象分类", fake.word()[:20]),
            ("排故对象描述", fake.text()[:20]),
            ("排故对象处置方法", fake.text()[:10]),
            ("观察时限", fake.random_int(24)),  # int
            ("技术更改文件(ECR/BCO)", fake.word()[:20]),
            ("技术通报号/图件编号", fake.uuid4()[:6]),
            ("软件版本号", fake.word()[:20]),
        ]
        return data

    def generate_fake_data(self, index=1):
        """
        根据index生成id，修改带传入数据库日期格式
        :param index:
        :return:
        """
        data = []
        fake_data_list = self.get_fake_data_list()
        record = OrderedDict(fake_data_list)
        record['问题id'] = index
        record['发布日期'] = f"""TO_DATE('{record["发布日期"]}', 'YYYY-MM-DD')"""
        record['发生日期'] = f"""TO_DATE('{record["发生日期"]}', 'YYYY-MM-DD')"""
        record['实际完成时间'] = f"""TO_DATE('{record["实际完成时间"]}', 'YYYY-MM-DD')"""
        data.append(record)
        if index%100 ==0:
            print(f"正在生成第{index}条数据")
        return data


def input_oracle():
    oracle = OracleHandler(con_config)
    oracle.get_conn()
    fake_data_generator = FakeDataGenerator()
    fake_data = fake_data_generator.generate_fake_data(fake_data_list, num_records=1)
    for data in fake_data:
        task_data =tuple(data.values())
        oracle.execute_insert_many_sql(fjgz_sql, task_data)


fake_data_generator = FakeDataGenerator()
if __name__ == '__main__':
    # 生成假数据
    # fake_data = fake_data_generator.generate_fake_data(fake_data_list, num_records=1)
    input_oracle()
