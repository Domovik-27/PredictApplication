#!/usr/bin/python
# -*- coding: UTF-8 -*-

from model import Match
from datetime import datetime, date, time

class DataPreloader():
	def create_matches(self):

		return [
		Match(
			group = "A",
			home_team = "Бразилия",
			guest_team = "Хорватия",
			start = datetime.combine(date(2014,06,12),time(23,0))
		),
		Match(
			group = "A",
			home_team="Мексика",
			guest_team = "Камерун",
			start = datetime.combine(date(2014,06,13),time(19,0))
		),
		Match(
			group = "B",
			home_team="Испания",
			guest_team = "Нидерланды",
			start = datetime.combine(date(2014,06,13),time(22,0))
		),
		Match(
			group = "B",
			home_team="Чили",
			guest_team = "Австралия",
			start = datetime.combine(date(2014,06,14),time(1,0))
		),
		Match(
			group = "C",
			home_team="Колумбия",
			guest_team = "Греция",
			start = datetime.combine(date(2014,06,14),time(19,0))
		),
		Match(
			group = "D",
			home_team="Уругвай",
			guest_team = "Коста-Рика",
			start = datetime.combine(date(2014,06,14),time(22,0))
		),
		Match(
			group = "D",
			home_team="Англия",
			guest_team = "Италия",
			start = datetime.combine(date(2014,06,15),time(1,0))
		),
		Match(
			group = "C",
			home_team="Кот д'Ивуар",
			guest_team = "Япония",
			start = datetime.combine(date(2014,06,15),time(4,0))
		),
		Match(
			group = "E",
			home_team="Швейцария",
			guest_team = "Эквадор",
			start = datetime.combine(date(2014,06,15),time(19,0))
		),
		Match(
			group = "E",
			home_team="Франция",
			guest_team = "Гондурас",
			start = datetime.combine(date(2014,06,15),time(22,0))
		),
		Match(
			group = "F",
			home_team="Аргентина",
			guest_team = "Босния и Герцеговина",
			start = datetime.combine(date(2014,06,16),time(1,0))
		),
		Match(
			group = "G",
			home_team="Германия",
			guest_team = "Португалия",
			start = datetime.combine(date(2014,06,16),time(19,0))
		),
		Match(
			group = "F",
			home_team="Иран",
			guest_team = "Нигерия",
			start = datetime.combine(date(2014,06,16),time(22,0))
		),
		Match(
			group = "G",
			home_team="Гана",
			guest_team = "США",
			start = datetime.combine(date(2014,06,17),time(1,0))
		),
		Match(
			group = "H",
			home_team="Бельгия",
			guest_team = "Алжир",
			start = datetime.combine(date(2014,06,17),time(19,0))
		),
		Match(
			group = "A",
			home_team="Бразилия",
			guest_team = "Мексика",
			start = datetime.combine(date(2014,06,17),time(22,0))
		),
		Match(
			group = "H",
			home_team="Россия",
			guest_team = "Южная Корея",
			start = datetime.combine(date(2014,06,18),time(1,0))
		),
		Match(
			group = "B",
			home_team="Австралия",
			guest_team = "Нидерланды",
			start = datetime.combine(date(2014,06,18),time(19,0))
		),
		Match(
			group = "B",
			home_team="Испания",
			guest_team = "Чили",
			start = datetime.combine(date(2014,06,18),time(22,0))
		),
		Match(
			group = "A",
			home_team="Камерун",
			guest_team = "Хорватия",
			start = datetime.combine(date(2014,06,19),time(1,0))
		),
		Match(
			group = "C",
			home_team="Колумбия",
			guest_team = "Кот д'Ивуар",
			start = datetime.combine(date(2014,06,19),time(19,0))
		),
		Match(
			group = "D",
			home_team="Уругвай",
			guest_team = "Англия",
			start = datetime.combine(date(2014,06,19),time(22,0))
		),
		Match(
			group = "C",
			home_team="Япония",
			guest_team = "Греция",
			start = datetime.combine(date(2014,06,20),time(1,0))
		),
		Match(
			group = "D",
			home_team="Италия",
			guest_team = "Коста-Рика",
			start = datetime.combine(date(2014,06,20),time(19,0))
		),
		Match(
			group = "E",
			home_team="Швейцария",
			guest_team = "Франция",
			start = datetime.combine(date(2014,06,20),time(22,0))
		),
		Match(
			group = "E",
			home_team="Гондурас",
			guest_team = "Эквадор",
			start = datetime.combine(date(2014,06,21),time(1,0))
		),
		Match(
			group = "F",
			home_team="Аргентина",
			guest_team = "Иран",
			start = datetime.combine(date(2014,06,21),time(19,0))
		),
		Match(
			group = "G",
			home_team="Германия",
			guest_team = "Гана",
			start = datetime.combine(date(2014,06,21),time(22,0))
		),
		Match(
			group = "F",
			home_team="Нигерия",
			guest_team = "Босния и Герцеговина",
			start = datetime.combine(date(2014,06,22),time(1,0))
		),
		Match(
			group = "H",
			home_team="Бельгия",
			guest_team = "Россия",
			start = datetime.combine(date(2014,06,22),time(19,0))
		),
		Match(
			group = "H",
			home_team="Южная Корея",
			guest_team = "Алжир",
			start = datetime.combine(date(2014,06,22),time(22,0))
		),
		Match(
			group = "G",
			home_team="США",
			guest_team = "Португалия",
			start = datetime.combine(date(2014,06,23),time(1,0))
		),
		Match(
			group = "B",
			home_team="Австралия",
			guest_team = "Испания",
			start = datetime.combine(date(2014,06,23),time(19,0))
		),
		Match(
			group = "B",
			home_team="Нидерланды",
			guest_team = "Чили",
			start = datetime.combine(date(2014,06,23),time(19,0))
		),
		Match(
			group = "A",
			home_team="Камерун",
			guest_team = "Бразилия",
			start = datetime.combine(date(2014,06,23),time(23,0))
		),
		Match(
			group = "A",
			home_team="Хорватия",
			guest_team = "Мексика",
			start = datetime.combine(date(2014,06,23),time(23,0))
		),
		Match(
			group = "D",
			home_team="Коста-Рика",
			guest_team = "Англия",
			start = datetime.combine(date(2014,06,24),time(19,0))
		),
		Match(
			group = "D",
			home_team="Италия",
			guest_team = "Уругвай",
			start = datetime.combine(date(2014,06,24),time(19,0))
		),
		Match(
			group = "C",
			home_team="Греция",
			guest_team = "Кот д'Ивуар",
			start = datetime.combine(date(2014,06,24),time(23,0))
		),
		Match(
			group = "C",
			home_team="Япония",
			guest_team = "Колумбия",
			start = datetime.combine(date(2014,06,24),time(23,0))
		),
		Match(
			group = "F",
			home_team="Нигерия",
			guest_team = "Аргентина",
			start = datetime.combine(date(2014,06,25),time(19,0))
		),
		Match(
			group = "F",
			home_team="Босния и Герцеговина",
			guest_team = "Иран",
			start = datetime.combine(date(2014,06,25),time(19,0))
		),
		Match(
			group = "E",
			home_team="Гондурас",
			guest_team = "Швейцария",
			start = datetime.combine(date(2014,06,25),time(23,0))
		),
		Match(
			group = "E",
			home_team="Эквадор",
			guest_team = "Франция",
			start = datetime.combine(date(2014,06,25),time(23,0))
		),
		Match(
			group = "G",
			home_team="США",
			guest_team = "Германия",
			start = datetime.combine(date(2014,06,26),time(19,0))
		),
		Match(
			group = "G",
			home_team="Португалия",
			guest_team = "Гана",
			start = datetime.combine(date(2014,06,26),time(19,0))
		),
		Match(
			group = "H",
			home_team="Алжир",
			guest_team = "Россия",
			start = datetime.combine(date(2014,06,26),time(23,0))
		),
		Match(
			group = "H",
			home_team="Южная Корея",
			guest_team = "Бельгия",
			start = datetime.combine(date(2014,06,26),time(23,0))
		)]