import datetime as dt
import time

from log.log import logger


# d = dt.datetime.strptime(input(), '%m %d')
# print(d)
# # print((d - dt.timedelta(1)).strftime('%m.%d'), (d + dt.timedelta(1)).strftime('%m.%d'))


def printLog(msg):  # лог в формате: время и информация
    cur_time = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
    print(cur_time + "\t" + msg)

# printLog("asdasd")

# print(time.localtime())




# Использование логгера
def my_function():
    logger.info("Функция my_function вызвана")
    # try:
    #     open("main.pyssss")
    # except Exception as e:
        # logger.error(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    logger.info("Функция my_function вызвана")
    logger.debug("function вызвана")
    # my_function()