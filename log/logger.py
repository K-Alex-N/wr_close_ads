import logging

# logger = logging.getLogger(__name__)

# stream_handler = logging.StreamHandler()
# file_handler = logging.FileHandler('game.log', encoding='utf-8')
#
# logger.addHandler(stream_handler)
# logger.addHandler(file_handler)

# Конфигурация логгера
# todo cleanup logger
class ColoredFormatter(logging.Formatter):
    COLORS = {'DEBUG': '\033[94m',
              'INFO': '\033[92m',
              'WARNING': '\033[93m',
              'ERROR': '\033[91m',
              'CRITICAL': '\033[95m'}

    def format(self, record):
        log_fmt = f"{self.COLORS.get(record.levelname, '')}%(message)s\033[0m"
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

# logging.getLogger().handlers[0].setFormatter(ColoredFormatter())
logging.basicConfig(level=logging.DEBUG,
                    # filename='app.log',
                    # encoding='utf-8',
                    format='%(asctime)s - %(levelname)s - %(message)s')
                    # format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


logger = logging.getLogger(__name__)
