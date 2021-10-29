import argparse
import logging
import os
import sys
import json
import datetime
import xml.etree.ElementTree as ELTree
import requests as requests


class Parser1:
    args = None

    def __init__(self):
        # initialize the object, add the necessary parameters
        parser = argparse.ArgumentParser()
        parser.add_argument("url", type=str, nargs="?", help="URL")
        parser.add_argument("--version", action="version", version="Version 1.1", help="Prints version info")
        parser.add_argument("--json", action="store_true", help="Prints result as JSON in stdout")
        parser.add_argument("--verbose", action="store_true", help="Outputs verbose status messages")
        parser.add_argument("--limit", dest="limit", default=sys.maxsize, type=int,
                            help="Limit news topics if this parameter provided")
        self.args = parser.parse_args()

    def __get_info__(self, logger: logging):  # receive information from the site and return info_list
        info_list = list()
        response = requests.get(self.args.url)
        root = ELTree.fromstring(requests.utils.get_unicode_from_response(response))
        cnt = 0
        feed = None
        for item in root[0]:
            if item.tag == "title":
                feed = item.text
            if item.tag == "item" and cnt < self.args.limit:  # limit the number of news
                cnt += 1
                info_dict = dict()  # create a dictionary and fill it with news
                info_dict.update({"Feed": feed})
                for child in item:
                    if child.tag == "title":
                        info_dict.update({"Title": child.text})
                    elif child.tag == "pubDate":
                        date = datetime.datetime.strptime(child.text, "%Y-%m-%dT%H:%M:%SZ")
                        info_dict.update(
                            {"Date": date.strftime("%a, %d %b %Y %H:%M:%S")})
                    elif child.tag == "link":
                        info_dict.update({"Link": child.text})
                    # elif "content" in child.tag:  # can be used if necessary
                    #     info_dict.update({"Media": child.attrib["url"]})
                    elif child.tag == "source":
                        info_dict.update({"Source": child.text})
                        info_dict.update({"Source URL": child.attrib["url"]})
                info_list.append(info_dict)
        logger.info("The information received successfully")
        return info_list

    def __print_info__(self, logger: logging):  # the method outputs the information in the specific format
        info_list = self.__get_info__(logger)  # get a list of news from __get_info__ method
        if self.args.json:  # output the news to a json file
            # get the root folder to write a json file there
            root = str(os.path.dirname(sys.modules['__main__'].__file__)) + "\\news.json"
            try:
                file = open(root, "w", encoding='utf8')
                logger.info("File is open")
                json.dump(info_list, file, ensure_ascii=False)
                file.close()
            except OSError:
                logger.error("File write error")
            # print("The file was successfully written")
        if not self.args.json:  # output the news to the console
            for item in info_list:
                print("")
                for key in item.keys():
                    print(key + ": " + item[key])
                print("")
