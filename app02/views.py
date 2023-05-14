from django.shortcuts import render

# Create your views here.
from app02 import models
from django.db.models import Avg, Max, Min, Count, Sum  # 引入函数
from django.db.models import F
from django.db.models import Q

# Create your views here.


# def add_book(request):
#     book = models.Book(title="菜鸟教程", price=300,publish="菜鸟出版社",pub_date="2008-8-8")
#     book.save()
#     return HttpResponse("<p>数据添加成功！</p>")

# def add_book(request):
#     books = models.Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10")
#     print(books, type(books)) # Book object (18)
#     return HttpResponse("<p>数据添加成功！</p>")

# def add_book(request):
#     books = models.Book.objects.all()
#     print(books, type(books))  # QuerySet类型，类似于list，访问 url 时数据显示在命令行窗口中。
#     for i in books:
#         print(i.title)
#     return HttpResponse("<p>查找成功！</p>")

# def add_book(request):
#     books = models.Book.objects.exclude(pk=5)
#     print(books)
#     print("//////////////////////////////////////")
#     books = models.Book.objects.exclude(publish='菜鸟出版社', price=300)
#     print(books, type(books))  # QuerySet类型，类似于list。
#     return HttpResponse("<p>查找成功！</p>")


# def add_book(request):
#     books = models.Book.objects.get(pk=1)
#     books = models.Book.objects.get(pk=18)  # 报错，没有符合条件的对象
#     # books = models.Book.objects.get(price=200)  # 报错，符合条件的对象超过一个
#     print(books, type(books))  # 模型类的对象
#     return HttpResponse("<p>查找成功！</p>")


# def add_book(request):
#     # books = models.Book.objects.order_by("price") # 查询所有，按照价格升序排列
#     # books = models.Book.objects.order_by("-price") # 查询所有，按照价格降序排列
#     # 按照价格升序排列：降序再反转
#     books = models.Book.objects.order_by("-price").reverse()
#     for i in books:
#         print(i.title, i.price)
#     return HttpResponse("<p>查找成功！</p>")

# def add_book(request):
#     books = models.Book.objects.count() # 查询所有数据的数量
#     books = models.Book.objects.filter(price=300).count() # 查询符合条件数据的数量
#     print(books)
#     return HttpResponse("<p>查找成功！</p>")


# def add_book(request):
#     #  获取出版社对象
#     pub_obj = models.Publish.objects.filter(pk=1).first()
#     #  给书籍的出版社属性publish传出版社对象
#     book = models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2010-10-10", publish=pub_obj)
#     print(book, type(book))
#     return HttpResponse(book)


# def add_book(request):
#     #  获取出版社对象
#     pub_obj = models.Publish.objects.filter(pk=1).first()
#     #  获取出版社对象的id
#     pk = pub_obj.pk
#     #  给书籍的关联出版社字段 publish_id 传出版社对象的id
#     book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
#     print(book, type(book))
#     return HttpResponse(book)


# 多对多(ManyToManyField)：在第三张关系表中新增数据
# def add_book(request):
#     #  获取作者对象
#     chong = models.Author.objects.filter(name="令狐冲").first()
#     ying = models.Author.objects.filter(name="任盈盈").first()
#     #  获取书籍对象
#     book = models.Book.objects.filter(title="菜鸟教程").first()
#     #  给书籍对象的 authors 属性用 add 方法传作者对象
#     book.authors.add(chong, ying)
#     return HttpResponse(book)

# def add_book(request):
#     #  获取作者对象
#     chong = models.Author.objects.filter(name="令狐冲").first()
#     #  获取作者对象的id
#     pk = chong.pk
#     #  获取书籍对象
#     book = models.Book.objects.filter(title="冲灵剑法").first()
#     #  给书籍对象的 authors 属性用 add 方法传作者对象的id
#     book.authors.add(pk)


# def add_book(request):
#     # 方式一：传对象
#     book_obj = models.Book.objects.get(id=10)
#     author_list = models.Author.objects.filter(id__gt=2)
#     book_obj.authors.add(*author_list)  # 将 id 大于2的作者对象添加到这本书的作者集合中
#     # 方式二：传对象 id
#     # book_obj.authors.add(*[1,3]) # 将 id=1 和 id=3 的作者对象添加到这本书的作者集合中
#     return HttpResponse("ok")


# def add_book(request):
#     # ying = models.Author.objects.filter(name="任盈盈").first()
#     # book = models.Book.objects.filter(title="冲灵剑法").first()
#     # ying.book_set.add(book)
#     # return HttpResponse("ok")
#
#     # pub = models.Publish.objects.filter(name="明教出版社").first()
#     # wo = models.Author.objects.filter(name="任我行").first()
#     # book = wo.book_set.create(title="吸星大法", price=300, pub_date="1999-9-19", publish=pub)
#     # print(book, type(book))
#     # return HttpResponse("ok")
#
#     # author_obj = models.Author.objects.get(id=1)
#     # book_obj = models.Book.objects.get(id=11)
#     # author_obj.book_set.remove(book_obj)
#     # return HttpResponse("ok")
#
#     #  清空Gtet的所有作者
#     # book = models.Book.objects.filter(title="Gtet").first()
#     # book.authors.clear()
#
#     # book = models.Book.objects.filter(pk=10).first()
#     # res = book.publish.city
#     # print(res, type(res))
#     # return HttpResponse("ok")
#
#     # pub = models.Publish.objects.filter(name="明教出版社").first()
#     # res = pub.book_set.all()
#     # for i in res:
#     #     print(i.title)
#     # return HttpResponse("ok")
#
#     # author = models.Author.objects.filter(name="令狐冲").first()
#     # res = author.au_detail.tel
#     # print(res, type(res))
#     # return HttpResponse("ok")
#
#     # addr = models.AuthorDetail.objects.filter(addr="黑木崖").first()
#     # res = addr.author.name
#     # print(res, type(res))
#     # return HttpResponse("ok")
#
#     # book = models.Book.objects.filter(title="菜鸟教程").first()
#     # res = book.authors.all()
#     # for i in res:
#     #     print(i.name, i.au_detail.tel)
#     # return HttpResponse("ok")
#
#     # author = models.Author.objects.filter(name="任我行").first()
#     # res = author.book_set.all()
#     # for i in res:
#     #     print(i.title)
#     # return HttpResponse("ok")
#
#     # 查询[明教出版社]出版过的所有书籍的名字与价格。
#     # res = models.Publish.objects.filter(name="明教出版社").values_list("book__title", "book__price")
#     # return HttpResponse(res)
#
#     # 查询任我行出过的所有书籍的名字
#     # res = models.Author.objects.filter(name="任我行").values_list("book__title")
#     # return HttpResponse(res)
#
#     # 查询任我行的手机号
#     # res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")
#     # return HttpResponse(res)
#
#     # 计算所有图书的平均价格:
#     # res = models.Book.objects.aggregate(Avg("price"))
#     # print(res, type(res))
#     # return HttpResponse(res)
#
#     # 计算所有图书的数量、最贵价格和最便宜价格
#     # res = models.Book.objects.aggregate(c=Count("id"), max=Max("price"), min=Min("price"))
#     # print(res, type(res))
#     # return HttpResponse("ok")
#
#     # 统计每一个出版社的最便宜的书的价格：
#     # res = models.Publish.objects.values("name").annotate(in_price=Min("book__price"))
#     # print(res)
#     # return HttpResponse("ok")
#
#     # 统计每一本书的作者个数：
#     # res = models.Book.objects.annotate(c=Count("authors__name")).values("title", "c")
#     # print(res)
#     # return HttpResponse("ok")
#
#     # 统计每一本以"菜"开头的书籍的作者个数：
#     # res = models.Book.objects.filter(title__startswith="菜").annotate(c=Count("authors__name")).values("title", "c")
#     # print(res)
#     # return HttpResponse("ok")
#
#     # 统计不止一个作者的图书名称：
#     # res = models.Book.objects.annotate(c=Count("authors__name")).filter(c__gt=1).values("title", "c")
#     # print(res)
#     # return HttpResponse("ok")
#
#     # 根据一本图书作者数量的多少对查询集 QuerySet 进行降序排序:
#     # res = models.Book.objects.annotate(c=Count("authors__name")).order_by("-c").values("title", "c")
#     # print(res)
#     # return HttpResponse("ok")
#
#     # 查询各个作者出的书的总价格:
#     # res = models.Author.objects.annotate(all=Sum("book__price")).values("name", "all")
#     # print(res)
#     # return HttpResponse("ok")
#
#
#     # F 查询
#     # book = models.Emp.objects.filter(salary__gt=F("age")).values("name", "age")
#     # print(book)
#     # return HttpResponse("ok")
#
#     # 将每一本书的价格提高100元
#     #
#
#
#
#     # Q 查询 查询价格大于 350 或者名称以菜开头的书籍的名称和价格。
#
#     res = models.Book.objects.filter(Q(price__gt=350) | Q(title__startswith="菜")).values("title", "price")
#     print(res)
#     return HttpResponse("ok")