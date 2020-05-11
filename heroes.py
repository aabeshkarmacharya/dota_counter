import csv
from difflib import get_close_matches
from typing import Iterator, List

import requests
from scrapy import Selector


def list_heroes(command: Iterator) -> str:
    sort = next(command, None)
    heroes = get_heroes()
    if sort == "sort":
        heroes.sort()
    return "\t".join(heroes)


def get_heroes() -> List[str]:
    response = requests.get("https://dota2.gamepedia.com/Heroes")
    sel = Selector(text=response.text)
    str_heroes = sel.xpath("(//table//tr)[2]//a/@title").getall()
    agi_heroes = sel.xpath("(//table//tr)[4]//a/@title").getall()
    int_heroes = sel.xpath("(//table//tr)[6]//a/@title").getall()
    return str_heroes + agi_heroes + int_heroes


def get_hero_aliases():
    with open("heroes.csv", "r", encoding="utf8") as f:
        dr = csv.DictReader(f)
        heroes_dict = {}
        for row in dr:
            heroes_dict[row.get("alias")] = row.get("full_name")
    return heroes_dict


def get_bad_against(hero_name: str, n: int = 5) -> (List[str], str):
    heroes_dict = get_hero_aliases()
    close_matches = get_close_matches(hero_name, heroes_dict.keys())
    matched_key = next(iter(close_matches), None)
    if matched_key:
        matched_hero = heroes_dict.get(matched_key)
        print("Matched Hero:", matched_hero)
        slug = matched_hero.replace(" ", "_")
        response = requests.get(f"https://dota2.gamepedia.com/{slug}/Counters")
        sel = Selector(text=response.text)
        counters = sel.xpath('//h2[contains(span/text(), "Bad against")]/following-sibling::div/div/a/@title').getall()
        print(counters)
        return counters[:n], matched_hero
    return None, None


def command_list(command: Iterator) -> str:
    what = next(command, None)
    if what:
        if what == "heroes":
            return list_heroes(command)