import scrapy
import regex as re
import logging

logger = logging.Logger("main")
logger.setLevel(logging.DEBUG)

MY_BEZIRK = set([6])
MY_NEARBY_BEZIRKS = set([3, 5, 15, 7])
OTHER_BEZIRKS = set(list(range(1, 24))).difference(MY_BEZIRK.union(MY_NEARBY_BEZIRKS))


class Bezirk:
    BEZIRK_LOOKUP = {
        1: "Mitte",
        2: "Leopoldstadt",
        3: "Landstra.{1,2}e",
        4: "Wieden",
        5: "Margareten",
        6: "Mariahilf",
        7: "Neubau",
        8: "Josefstadt",
        9: "Alsergrund",
        10: "Favoriten",
        11: "Simmering",
        12: "Meidling",
        13: "Hietzing",
        14: "Penzing",
        15: "F.{1,2}nfhaus",
        16: "Ottakring",
        17: "Hernals",
        18: "W.{1,2}hring",
        19: "D.{1,2}bling",
        20: "Brigittenau",
        21: "Floridsdorf",
        22: "Donaustadt",
        23: "Liesing",
    }
    BEZIRK_REGEX = [
        "(?i)((mitte|innere)( stadt)?)",
        "(?i)(leopoldstadt)",
        "(?i)(landstra.{1,2}e)",
        "(?i)(wieden)",
        "(?i)(margareten)",
        "(?i)(mariahilf)",
        "(?i)(neubau)",
        "(?i)(josefstadt)",
        "(?i)(alsergrund)",
        "(?i)(favoriten)",
        "(?i)(simmering)",
        "(?i)(meidling)",
        "(?i)(hietzing)",
        "(?i)(penzing)",
        "(?i)(f.{1,2}nfhaus)",
        "(?i)(ottakring)",
        "(?i)(hernals)",
        "(?i)(w.{1,2}hring)",
        "(?i)(d.{1,2}bling)",
        "(?i)(brigittenau)",
        "(?i)(floridsdorf)",
        "(?i)(donaustadt)",
        "(?i)(liesing)",
    ]

    def __init__(self, name=None, number=None, postleitzahl=None):
        if name is None and number is None and postleitzahl is None:
            raise NameError("needs some identification!")
        elif name is not None:
            if name not in self.bezirk_lookup.values():
                raise NameError("doesnt exist, sorry")
            self.name = name
            self.number = self.get_number_from_name(name)
            self.postleitzahl = self.make_postleitzahl(self.number)
        elif number is not None:
            if number not in range(1, 24):
                raise NameError("that bezirk doesnt exist!")
            self.name = self.get_name_from_number(number)
            self.number = number
            self.postleitzahl = self.make_postleitzahl(self.number)
        elif postleitzahl is not None:
            self.number = self.extract_number_from_postleitzahl(postleitzahl)
            if self.number not in range(1, 24):
                raise NameError("that bezirk doesn't exist!")
            self.name = self.get_name_from_number(self.number)
            self.postleitzahl = postleitzahl
        self.neighbors = set()

    def get_number_from_name(self, name):
        for id, name_regex in enumerate(self.BEZIRK_REGEX):
            if re.findall(name_regex, name):
                self.number = id + 1
                break

    def make_postleitzahl(self, number):
        return "1{!s:0>2}0".format(number)

    def get_name_from_number(self, number):
        return self.bezirk_lookup[number]

    def extract_number_from_postleitzahl(self, postleitzahl):
        return int(postleitzahl[1:3])

    def connect_bezirks(self, bezirk):
        self.neighbors.add(bezirk)

    def get_bezirk_names(self, bezirks):
        return [bezirk.name for bezirk in bezirks]

    def get_next_neighbors(self):
        collect = set()
        for bezirk in self.neighbors:
            collect = collect.union(bezirk.neighbors)
        return collect


class WienNetworkManager:
    def __init__(self):
        self.wien = self.make_network()

    def make_network(self):
        pass


class PfarrScraper:
    def __init__(self):
        self.site_address = "flohmark site"
        self.results = []

    def xpath_extractor(self):
        """
        details for extracting the info from the website
        """
        # return extraction
        pass

    def pfarr_finder(self, extraction):
        class _: pass                           # noqa
        result = _()
        for listing in extraction:
            if self.listing_is_pffarflohmarkt(listing):
                result.bezirk = self.get_bezirk(listing)
                result.address = self.get_address(listing)
                result.time = self.get_time(listing)
            self.results.append(result)

    def listing_is_pffarflohmarkt(self, listing):
        if re.findall("(?i)pfarr", listing.title):
            return True
        else:
            return True

    def get_bezirk(self, listing):
        bezirks = []
        bezirks.append(re.findall("1[0-9]{2}0", listing.title))
        bezirks.append(re.findall("1[0-9]{2}0", listing.body))
        bezirks.append(re.findall(Bezirk.BEZIRK_REGEX, listing.title))
        bezirks.append(re.findall(Bezirk.BEZIRK_REGEX, listing.body))
        self.assert_single_bezirk()
        return set(bezirks)

    def assert_single_bezirk(self, listing, bezirks):
        try:
            assert len(set(bezirks)) is 1
        except:
            logging.debug("Location error: listing {} had bad location data.".format(listing.index))

    def get_address(self, listing):
        pass

    def get_time(self, listing):
        pass

    def order_list(self):
        class _(): pass                         # noqa
        ordered_results = _()
        for listing in self.results:
            if listing.bezirk in MY_BEZIRK:
                ordered_results.my_markts.append(listing)
            elif listing.bezirk in MY_NEARBY_BEZIRKS:
                ordered_results.near_markts.append(listing)
            elif listing.bezirk in OTHER_BEZIRKS:
                ordered_results.other_markts.append(listing)


if __name__ == "__main__":
    mit = Bezirk("mitte")
