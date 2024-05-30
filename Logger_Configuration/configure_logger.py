import logging

LOGGER_NAME = "Logger"
FORMATTER = "%(asctime)s - %(name)s - %(levelname)s : %(message)s"
LOGGING_LEVEL = logging.DEBUG


def config_logging(
    logger_name=LOGGER_NAME,
    formatter=FORMATTER,
    log_file_name=None,
    logging_level=LOGGING_LEVEL,
):
    """
    Configures and returns a logger object with the specified parameters.

    Args:
        logger_name (str): The name of the logger. Default is “Logger”.
        formatter (str): The format string for the log messages. Default is “%(asctime)s - %(name)s - %(levelname)s : %(message)s”.
        log_file_name (str): The name of the file where the log messages will be written. Default is None.
        logging_level (int): The level of logging. Default is logging.DEBUG.
    
    Returns:
        logger (logging.Logger): The configured logger object.
    
    """

    logger = logging.getLogger(logger_name)
    logging_format = logging.Formatter(formatter)

    if log_file_name:
        file_handler = logging.FileHandler(filename=log_file_name)
        file_handler.setFormatter(logging_format)
        logger.addHandler(file_handler)
    else:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(logging_format)
        logger.addHandler(console_handler)

    logger.setLevel(logging_level)

    return logger
