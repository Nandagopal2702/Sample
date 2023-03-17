import logging


def test_loggingDemo():

    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler("logFile.log")
    logger.addHandler(fileHandler)   # fileHandler object
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)

    logger.debug("A Debug statement is executed")
    logger.info("Information executed")
    logger.warning("Someting wrong in our code")
    logger.error("An error occured")
    logger.critical("Critical issue")