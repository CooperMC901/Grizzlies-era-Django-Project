from typing_extensions import dataclass_transform
from django.shortcuts import render
from dataclasses import dataclass
from typing import List
# Create your views here.

@dataclass
class eras:
    name: str
    roster: list
    desc: str

teams = {
    "The Pyramid": eras("The Pyramid", ["Shane Battier", "Troy Bell", "Pau Gasol", "Ryan Humphrey", "Dahntay Jones"], "When the grizzlies originally moved to Memphis from Vancouver Canada their first arena was the pyramid (now known today as bass pro shops). This Pyramid era of Grizzlies basketball was highlighted with ups and downs, from winning 52 games in 2004 all the way down to 20 in 2008. This team had historical roster composition issues and really lacked identity, which was solved in the Grit and Grind era."),
    "Grit and Grind": eras("Grit and Grind", ["Mike Conley", "Zach Randolph", "Marc Gasol", "Tony Allen", "TayShaun Prince"], "After moving to the FedexForum from the Pyramid in 2010, the Grizzlies started focusing on the draft more and more after coming to the reality that attracting A-list free agents to Memphis would be next to impossible. The Grizzlies started this impeccable drafting run with Mike Conley and Zach Randolph in 2011, both were key figures in this era of tough and (gritty) grizzlies basketball. Tony Allen brought fierce defense while Marc Gasol was a stretch bigman that could shoot the three, put the ball on the floor, as well as defend. These teams were very successful, making it all the way to the Western Conference Finals in 2015 and paved the way for where the Grizzlies are today and headed to over the next decade."),
    "Today": eras("Today", ["Ja Morant", "Desmond Bane", "Dillon Brooks", "Jaren Jackson JR", "Steven Adams"], "Today the Grizzlies have positioned themselves as well as they ever have to be a winning team and possibly bring a championship to Memphis. Finishing 2nd in the Western Conference last season and making the playoffs, todays' Grizzlies are led by superstar guard Ja Morant and supporting case Desmond Bane and Dillon Brooks, continuing on the Grizzlies tradition of drafting well and building players into their culture. At the time of this website being made, the 2022-2023 season starts in 20 days and the future is looking as bright as ever for the Grizzlies.")

}

def homescreen(request):
    return render(request, "homepage.html")

def view(request, era):
    era = teams[era]

    context = {
        "name": era.name,
        "roster": era.roster,
        "desc": era.desc
    }

    

    return render(request, "resultspage.html", context)