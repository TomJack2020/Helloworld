from time import timezone

from django.db import models


# Create your models here.


class Department(models.Model):
    """部门表"""
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# 新建数据
# 本质insert into app01_department(title)values('销售部')
# Department.objects.create(title='销售部')


class UserInfo(models.Model):
    """用户信息表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, unique=True, verbose_name="姓名")
    password = models.CharField(max_length=64, verbose_name="密码")
    age = models.IntegerField(null=True, blank=True, verbose_name="年龄")
    # 新增列字段
    size = models.IntegerField(default=2)
    data = models.IntegerField(null=True, blank=True)

    account = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")

    # 1有约束
    # -to：与那一张表关联
    # -to_filed: 与表中的哪一个列相关
    # django 自动
    # 2写的depart
    # 生成数据列 depart_id
    # 3.1 部门被删除时
    # depart = models.ForeignKey(to="Department", to_field='id', on_delete=models.CASCADE)
    # 级联删除 删除部门  数据删除
    # 3.2 置空
    # depart = models.ForeignKey(to="Department", to_field='id', null=True, blank=True, on_delete=models.CASCADE)

    depart = models.ForeignKey(to="Department", to_field='id', on_delete=models.CASCADE, verbose_name='部门')

    # 在django中做约束
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, null=True)


class PrettyNum(models.Model):
    """靓号表"""
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    price = models.IntegerField(verbose_name="价格")
    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )

    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)

    status_choice = (
        (1, '已占用'),
        (2, '未使用'),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choice, default=2)
