import logging


class logclass:
    def getthelogs(self):
        logger = logging.getLogger()
        filehandler = logging.FileHandler("Logs/logfile.log", mode = "w")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
        # logger.debug("Debug message")
        # logger.info("Information regarding the test case")
        # logger.warning("Test case pass but with a Warning message")
        # logger.error("Test case fail")
        # logger.critical("Important test case fail on which other test case depends")

