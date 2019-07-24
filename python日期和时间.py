from datetime import datetime
from datetime import date
from datetime import time as time_datetime
import time
from datetime import timedelta

# ------------------1、获得当前时间-------------#

# 得到当前时间戳
print(time.time())

# 时间戳转换为时间元组
print(time.localtime(time.time()))
print(time.gmtime(time.time()))

# 将时间元组格式化输出成字符串时间
print(time.strftime("%Y-%m-%d", time.localtime(time.time())))
print(time.strftime("%Y-%m-%d", time.gmtime(time.time())))

# 不带参数默认输出当前时间
print(time.strftime("%Y-%m-%d"))

# 通过datetime模块来实现
print(datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d"))
print(datetime.now().strftime("%Y-%m-%d"))
print(datetime.today().strftime("%Y-%m-%d"))

# ------------------2、获取时间差，计算执行时间-------------#

# time 模块获取时间戳
start = time.time()
time.sleep(1)
print(time.time() - start)

# datetime模块
start = datetime.now()
time.sleep(1)
print((datetime.now() - start).seconds)

# 计算昨天的日期
print(datetime.now() - timedelta(days=1))

# 时间元组转化为时间戳
print(time.mktime(time.localtime()))  # localtime获取时间元组
print(time.mktime(time.gmtime()))  # gmtime获取时间元组，格林威治时间
print(time.mktime(datetime.now().timetuple()))  # datetime里获取时间元组

# 将时间字符串转换为时间元组
print(time.strptime("2019-07-14 11:23:33", "%Y-%m-%d %H:%M:%S"))

# 表示时间的两种方式：
# 1. 时间戳(相对于1970.1.1 00:00:00以秒计算的偏移量),时间戳是惟一的
# 2. 时间元组 即(struct_time),共有九个元素，分别表示，同一个时间戳的struct_time会因为时区不同而不同

# ------------------3、time时间模块-------------#
# time.clock方法
# 这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是“进程时间”，它是用秒表示的浮点数（时间
# 戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。
# （实际上是以WIN32 上QueryPerformanceCounter()
# 为基础，它比毫秒表示更为精确）

start = time.clock()
time.sleep(1)
print(time.clock() - start)

# 返回本地时间元组
print(time.localtime())
print(time.localtime(time.time()))

# 从时间元组按照格式进行格式化输出字符串
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 从时间元组转换为时间戳
print(time.mktime(time.localtime()))
print(time.mktime(time.gmtime()))
print(time.mktime(datetime.now().timetuple()))

# ------------------4、datetime时间模块-------------#
# 1.datetime.date: 是指年月日构成的日期(相当于日历)
# 2.datetime.time: 是指时分秒微秒构成的一天24小时中的具体时间(相当于手表)
# 3.datetime.datetime: 上面两个合在一起，既包含时间又包含日期
# 4.datetime.timedelta: 时间间隔对象(timedelta)。一个时间点(datetime)加上一个时间间隔(timedelta)
# 可以得到一个新的时间点(datetime)。比如今天的上午3点加上5个小时得到今天的上午8点。同理，两个时间点相减会得到一个时间间隔。
# 获取当天日期
print(date.today())

# 构造函数构造日期
print(date(2018, 1, 1))

# 格式化日期输出
print(date.today().strftime("%Y%m%d"))

# 日期转换成时间元组，其中时分秒都是0
print(date.today().timetuple())

# 按照时间戳转换为日期
print(date.fromtimestamp(time.time()))

# datetime中的time模块，构造时间
t = time_datetime(8, 11, 11)
print(t)

# 格式化时间
print(t.strftime("%H-%M-%S"))

# 新建一个datetime对象，日期为今天，既可以直接调用datetime.datetime.today()，
# 也可以直接向datetime.datetime()传值，如下：
print(datetime.today())
print(datetime.now())
print(datetime(2014, 8, 15, 8, 12, 34, 790945))

# datetime.datetime.now([tz]) 当不指定时区时，和datetime.datetime.today()是一样的结果
# 格式化时间
print(datetime.now().strftime("%H-%M-%S"))

# 返回时间元组
print(datetime.now().timetuple())
print(time.mktime(datetime.now().timetuple()))

# 数据替换
d1 = datetime(2014, 8, 15, 8, 12, 34, 790945)
print(d1.replace(year=2000))

# ------------------5、timedelta-------------#
print(datetime.today())
print(datetime.today() - timedelta(days=1))