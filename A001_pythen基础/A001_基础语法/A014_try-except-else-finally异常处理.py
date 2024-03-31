try:
    print("可能出现异常的代码")
except Exception as e:
    print("异常的代码")
    raise Exception("抛出异常...")
else:
    print("否则")
finally:
      print("最终执行")