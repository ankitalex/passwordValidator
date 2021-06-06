import logging

def getmylogger(name):
        logger = logging.getLogger(name)
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s', datefmt='%y-%b-%d %H:%M:%S')
        fileHandler = logging.FileHandler(filename=r'C:/Users/user/PycharmProjects/pythonProject/passwordValidator/Validator/logs/PasswordValidator.log')
        fileHandler.setFormatter(formatter)
        logger.setLevel(level=logging.DEBUG)
        logger.addHandler(fileHandler)
        return logger;