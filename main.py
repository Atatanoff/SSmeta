
from loguru import logger

from res.values import string



@logger.catch  
def main():
    for key, val in string.QUESTIONS.items():
        vars()[key] = val

    logger.debug(f"{count_angel}")


if __name__ == '__main__':
    main()
