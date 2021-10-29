""" python C:/Users/Анна/Desktop/Аня/Учеба/Python/Pr1/"Introduction to Python"/final_task/rss_reader.py https://news.yahoo.com/rss/"""
import reader_obj
import logging


def main():
    parser = reader_obj.Parser1()
    # create a logger which work if verbose is true
    logging.basicConfig(level=logging.DEBUG if parser.args.verbose else logging.disable())
    logger = logging.getLogger()
    logger.debug(' '.join([f'{k}={v}' for k, v in vars(parser.args).items()]))

    try:
        if parser.args.url is not None:
            if parser.args.limit <= 0:
                raise ValueError("Limit must be positive and more then zero")
            parser.__print_info__(logger)
            logger.info("The program was completed successfully")
        elif parser.args.url is None:
            logger.info("The URL isn't defined")
    except Exception as exception:
        logger.error(exception)


if __name__ == "__main__":
    main()
