# import logging
#
# # logger 实例化
# logger = logging.getLogger()
#
# # 创建一个 handler
# fh = logging.FileHandler('test.log', encoding='utf8')
# # 再创建一个 handler，用于输出到控制台
# ch = logging.StreamHandler()
# # 设置输出格式
# formatter = logging.Formatter(
#     '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
# )
# # 设置 level
# fh.setLevel(logging.DEBUG)
#
# # 文件（屏幕）操作符 绑定一个输出格式
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
#
# # logger 对象和 文件（屏幕）操作符 相连
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# # 输出警告
# logger.warning('报警')
