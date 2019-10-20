# import scrapy
# import regex as re
import logging

logger = logging.Logger("main")
logger.setLevel(logging.DEBUG)

MY_BEZIRK = set([6])
MY_NEARBY_BEZIRKS = set([3, 5, 15, 7])
OTHER_BEZIRKS = set(list(range(1, 24))).difference(MY_BEZIRK, MY_NEARBY_BEZIRKS)

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

    BEZIRK_REGEX = \
    """
    (?i)((mitte|innere)( stadt)?)
       (leopoldstadt)
       (landstra.{1,2}e)
       (wieden)
       (margareten)
       (mariahilf)
       (neubau)
       (josefstadt)
       (alsergrund)
       (favoriten)
       (simmering)
       (meidling)
       (hietzing)
       (penzing)
       (f.{1,2}nfhaus)
       (ottakring)
       (hernals)
       (w.{1,2}hring)
       (d.{1,2}bling)
       (brigittenau)
       (floridsdorf)
       (donaustadt)
       (liesing)
    """

    def __init__(self, name=none, number=none, postleitzahl=none):
        if name is none and number is none and postleitzahl is none:
            raise nameerror("needs some identification!")
        elif name is not none:
            if name not in self.bezirk_lookup.values():
                raise nameerror("doesnt exist, sorry")
            self.name = name
            self.number = self.get_number_from_name(name)
            self.postleitzahl = self.make_postleitzahl(self.number)
        elif number is not none:
            if number not in range(1, 24):
                raise nameerror("that bezirk doesnt exist!")
            self.name = self.get_name_from_number(number)
            self.number = number
            self.postleitzahl = self.make_postleitzahl(self.number)
        elif postleitzahl is not none:
            self.number = self.extract_number_from_postleitzahl(postleitzahl)
            if self.number not in range(1, 24):
                raise nameerror("that bezirk doesn't exist!")
            self.name = self.get_name_from_number(self.number)
            self.postleitzahl = postleitzahl
        self.neighbors = set()

    def get_number_from_name(self, name):

        names = list(self.bezirk_lookup.values())
        return names.index(name) + 1

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


class wiennetworkmanager:
    def __init__(self):
        self.wien = self.make_network()

    def make_network(self):





class pfarrscraper:
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
        class _: pass
        result = _()
        for listing in extraction:
            if self.listing_is_pffarflohmarkt(listing):
                result.bezirk = self.get_bezirk(listing)
                result.address = self.get_address(listing)
                result.time = self.get_time(listing)
            self.results.append(result)


    def listing_is_pffarflohmarkt(self, listing):
        if re.findall("[pp]farr", listing.title):
            return true
        else:
            return false


    def get_bezirk(self, listing):
        bezirks.append(re.findall("1[0-9]{2}0", listing.title))
        bezirks.append(re.findall("1[0-9]{2}0", listing.body))
        bezirks.append(re.findall(bezirk_regex, listing.title))
        bezirks.append(re.findall(bezirk_regex, listing.body))
        self.assert_single_bezirk()
        return set(bezirks)

    def assert_single_bezirk(self, listing, bezirks):
        try:
            assert len(set(bezirks)) is 1
        except:
            logging.debug("location error: listing {} had bad location data.".format(listing.index))

    def get_address(self, listing):
        pass

    def get_time(self, listing):
        pass

    def order_list(self):
        class _(): pass
        ordered_results = _()
        for listing in self.results:
            if listing.bezirk in my_bezirk:
                ordered_results.my_markts.append(listing)
            elif listing.bezirk in my_nearby_bezirks:
                ordered_results.near_markts.append(listing)
            elif listing.bezirk in other_bezirks:
                ordered_results.other_markts.append(listing)


if __name__=="__main__":
    mit = bezirk("mitte")

