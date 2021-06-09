from loguru import logger


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """

    def __init__(self, logger, level="INFO"):
        self.logger = logger
        self._level = level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            #   self.logger.log(self._level, line.rstrip())
            self.logger.opt(depth=1).log(self._level, line.rstrip())

    def flush(self):
        pass


def build_logger(log_file, default_level='INFO'):
    """To setup your log_file and log level

    :param log_file: set your log file path
    :type log_file: str, optional
    :param default_level: log level, defaults to 'INFO'
    :type default_level: str, optional
    """
    fmt = "{time} | {level: <8} | {name}:{function}:{line} | {message}"
    fmt = "{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    fmt = "{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} | {message}"

    logger.add(
        log_file,
        level=default_level,
        format=fmt,
        rotation="30 days",
        filter=None,
        colorize=False,
        serialize=False,
        backtrace=False,
        enqueue=False,
        catch=False,
        encoding='utf-8',
        diagnose=False,  # This should be set to False in production to avoid leaking sensitive data.
    )
