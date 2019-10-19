import scrapy
import regex as re
import logging

logger.setLevel(logging.DEBUG)

MY_BEZIRK = set([6])
MY_NEARBY_BEZIRKS = set([3, 5, 15, 7])
OTHER_BEZIRKS = set(list(range(1, 23))).difference(MY_BEZIRK, MY_NEARBY_BEZIRKS)

class PfarrScraper:
    def __init__(self):
        self.site_address = "flohmark site"
        self.results = []

    def xpath_extractor(self):
        """
        Details for extracting the info from the website
        """
        # return extraction
        pass

    def pfarr_finder(self, extraction):
        class _: pass
        result = _()
        for listing in extraction:
            if self.listing_is_pffarflohmarkt(listing):
                result.bezirk = self.get_bezirk(listing)
                result.address = self.get_address(listing)
                result.time = self.get_time(listing)
            self.results.append(result)


    def listing_is_pffarflohmarkt(self, listing):
        if re.findall("[Pp]farr", listing.title):
            return True
        else:
            return False


    def get_bezirk(self, listing):
        bezirks.append(re.findall("1[0-9]{2}0", listing.title))
        bezirks.append(re.findall("1[0-9]{2}0", listing.body))
        bezirks.append(re.findall(BEZIRK_REGEX, listing.title))
        bezirks.append(re.findall(BEZIRK_REGEX, listing.body))
        self.assert_single_bezirk()
        return set(bezirks)

    def assert_single_bezirk(self, listing, bezirks):
        try:
            assert len(set(bezirks)) is 1
        except:
            logging.debug("LOCATION ERROR: Listing {} had bad location data.".format(listing.index))

    def get_address(self, listing):
        pass

    def get_time(self, listing):
        pass

    def order_list(self):
        class _(): pass
        ordered_results = _()
        for listing in self.results:
            if listing.bezirk in MY_BEZIRK:
                ordered_results.my_markts.append(listing)
            elif listing.bezirk in MY_NEARBY_BEZIRKS:
                ordered_results.near_markts.append(listing)
            elif listing.bezirk in OTHER_BEZIRKS:
                ordered_results.other_markts.append(listing)


BEZIRK_LOOKUP = {
    1: "Mitte",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "Mariahilf",
    7: "",
    8: "",
    9: "",
    10: "Favoriten",
    11: "Simmering",
    12: "",
    13: "",
    14: "",
    15: "",
    16: "",
    17: "",
    18: "",
    19: "",
    20: "",
    21: "",
    22: "",
}
BEZIRK_REGEX="""
mitte



mariahilf
"""
