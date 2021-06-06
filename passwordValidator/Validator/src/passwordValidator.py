from string import punctuation
import logging

def getmylogger(name):
        logger = logging.getLogger(name)
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(message)s', datefmt='%y-%b-%d %H:%M:%S')
        fileHandler = logging.FileHandler(filename=r'C:/Users/user/PycharmProjects/pythonProject/passwordValidator/Validator/logs/PasswordValidator.log')
        fileHandler.setFormatter(formatter)
        logger.setLevel(level=logging.DEBUG)
        logger.addHandler(fileHandler)
        return logger;

logger = getmylogger(__name__)

class PasswordValidator(object):
    def __init__(self,password=None):
        self._password=password

    def length_check(self):
        logger.debug(f" length check started")
        if len(self._password)<8:
            logger.info(f" length check failed")
            return "Password length should be above or equal to 8"
        else:
            logger.debug(f" length check ended")
            return True


    def isSpaceAvailable(self):
        logger.debug(f" space existence check started")
        if ' ' in self._password:
            logger.info(f" space existence check failed")
            return "Password should not contain Space in password"
        else:
            logger.debug(f" space existence check  ended")
            return True

    def isSpecialCharacterAvaialble(self):
        special_chars = [True for x in self._password if x in punctuation]
        if len(special_chars)==0:
            logger.info(f" Special character check failed")
            return "Password should have atleast 1 special character"
        else:
            return True

    def isDigitAvaialble(self):
        nums = any(x.isdigit() for x in self._password)
        if not nums:
            logger.info(f" Digit check failed")
            return "Password should have atleast 1 number"
        else:
            return True

    def captialCharcterCheck(self):
        #print(self._password)
        if not any(x.isupper() for x in self._password):
            logger.info('String must have 1 upper case character.')
            return "Password should have atleast 1 captial charcter"
        else:
            return True

    def lowerCharcterCheck(self):
        if not any(x.islower() for x in self._password):
            logger.info('String must have 1 lower case character.')
            return "Password should have atleast 1 captial charcter"
        else:
            return True
