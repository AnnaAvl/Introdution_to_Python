import reader_obj
import logging


def main():
    parser = reader_obj.Parser1()
    # create a logger which work if verbose is true
    logging.basicConfig(level=logging.DEBUG if parser.args.verbose else logging.disable())
    logger = logging.getLogger()
    logger.debug(" ".join([f"{k}={v}" for k, v in vars(parser.args).items()]))

    try:
        if parser.args.limit <= 0:
            raise ValueError("Limit must be positive and more then zero")
        if parser.args.url is not None:
            parser.__get_info__(logger)
            parser.__print_info__(logger)
        elif parser.args.url is None and parser.args.date is not None:
            parser.__print_info__(logger)
        elif parser.args.url is None and parser.args.date is None:
            raise Exception("The URL isn't defined")
        logger.info("The program was completed successfully")
    except Exception as exception:
        logger.error(exception) if parser.args.verbose else print(exception)


if __name__ == "__main__":
    main()
