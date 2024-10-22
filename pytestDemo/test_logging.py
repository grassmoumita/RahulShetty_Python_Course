import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)     # this will log everything, if not mentioned __name__, i will print root

    fileHandler = logging.FileHandler('logfile.log')     #in this file the log will create

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)    #filehandler object

    # logger.setLevel(logging.INFO)    # as setting from Info, debug will not show, from info it will print
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error happened")
    logger.critical("Critical issue")     # from debug to critical this is the order, we can change the order by setLevel





