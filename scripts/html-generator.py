html = ""

imagedict = {
        "Alex Ovechkin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3101.png&w=350&h=254",
        "Brent Burns": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2300.png&w=350&h=254",
        "Evgeni Malkin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3124.png&w=350&h=254",
        "Sidney Crosby": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114.png&w=350&h=254",
        "Brad Marchand": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3852.png&w=350&h=254",
        "Connor McDavid": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3895074.png&w=350&h=254",
        "Joe Pavelski": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3451.png&w=350&h=254",
        "Ryan Kesler": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2175.png",
        "Dustin Byfuglien": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3070.png&w=350&h=254",
        "Nazem Kadri": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5349.png&w=350&h=254",
        "Patrick Kane": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3735.png&w=350&h=254",
        "Wayne Simmonds": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3817.png&w=350&h=254",
        "Nicklas Backstrom": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3666.png&w=350&h=254",
        "Blake Wheeler": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3961.png&w=350&h=254",
        "Tyler Seguin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5430.png&w=350&h=254",
        "Jeff Carter": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2383.png&w=350&h=254",
        "David Pastrnak": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114778.png&w=350&h=254",
        "Nick Foligno": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3535.png&w=350&h=254",
        "Patric Hornqvist": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3699.png&w=350&h=254",
        "Shea Weber": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2278.png&w=350&h=254",
        "Nikita Kucherov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563060.png&w=350&h=254",
        "Cam Atkinson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2501107.png&w=350&h=254",
        "Mark Scheifele": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562632.png&w=350&h=254",
        "Jamie Benn": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3998.png&w=350&h=254",
        "Phil Kessel": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3479.png&w=350&h=254",
        "Matthew Tkachuk": "https://nhl.bamcontent.com/images/photos/281045464/1024x576/cut.jpg",
        "Vladimir Tarasenko": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5837.png&w=350&h=254",
        "Jakub Voracek": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3781.png&w=350&h=254",
        "Max Pacioretty": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4005.png&w=350&h=254",
        "Mikael Granlund": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5831.png&w=350&h=254",
        "Patrick Maroon": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3853.png&w=350&h=254",
        "Mike Hoffman": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5103.png&w=350&h=254",
        "Artemi Panarin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3891952.png&w=350&h=254",
        "John Tavares": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5160.png&w=350&h=254",
        "Alexander Radulov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3249.png&w=350&h=254",
        "Chris Kreider": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5833.png&w=350&h=254",
        "Corey Perry": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2273.png&w=350&h=254",
        "Nino Niederreiter": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5511.png&w=350&h=254",
        "Drew Doughty": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3995.png&w=350&h=254",
        "Brayden Schenn": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5219.png&w=350&h=254",
        "James van Riemsdyk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3822.png&w=350&h=254",
        "Evgeny Kuznetsov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5647.png",
        "Auston Matthews": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024123.png&w=350&h=254",
        "Ryan Johansen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5434.png&w=350&h=254",
        "Victor Hedman": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5157.png&w=350&h=254",
        "Kyle Pamieri": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5517.png&w=350&h=254",
        "Leon Draisaitl": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114727.png&w=350&h=254",
        "Claude Giroux": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3775.png&w=350&h=254",
        "Patrik Laine": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024820.png&w=350&h=254",
        "Mitch Marner": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899937.png&w=350&h=254",
        "Nikolaj Ehlers": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114741.png&w=350&h=254",
        "Milan Lucic": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3780.png&w=350&h=254",
        "Rasmus Ristolainen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3041999.png&w=350&h=254",
        "Dougie Hamilton": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562605.png&w=350&h=254",
        "Justin Schultz": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2501067.png&w=350&h=254",
        "Evander Kane": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5251.png&w=350&h=254",
        "Mats Zuccarello": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5560.png&w=350&h=254",
        "Erik Karlsson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5164.png&w=350&h=254",
        "Charlie Coyle": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2555315.png&w=350&h=254",
        "Mikael Backlund": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3797.png&w=350&h=254",
        "Jason Zucker": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2593315.png&w=350&h=254",
        "Eric Staal": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2378.png&w=350&h=254",
        "Matt Niskanen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3620.png&w=350&h=254",
        "Mikko Koivu": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2147.png&w=350&h=254",
        "Alexander Wennberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042017.png&w=350&h=254",
        "T.J. Oshie": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5034.png&w=350&h=254",
        "Derek Stepan": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5731.png&w=350&h=254",
        "J.T. Miller": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590852.png&w=350&h=254",
        "Anders Lee": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5793.png&w=350&h=254",
        "Ryan Suter": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3047.png&w=350&h=254",
        "Kevin Shattenkirk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5008.png&w=350&h=254",
        "Vincent Trocheck": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563036.png&w=350&h=254",
        "Jeff Skinner": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5540.png&w=350&h=254",
        "Mike Fisher": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/276.png&w=350&h=254",
        "Kyle Okposo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3859.png&w=350&h=254",
        "Zach Werenski": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899972.png&w=350&h=254",
        "Brandon Dubinsky": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3323.png&w=350&h=254",
        "Logan Couture": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3773.png&w=350&h=254",
        "Patrice Bergeron": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2280.png&w=350&h=254",
        "Andrew Shaw": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2564334.png&w=350&h=254",
        "Matt Dumba": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2970689.png&w=350&h=254",
        "Dmitry Orlov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5646.png&w=350&h=254",
        "Patrick Marleau": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/576.png&w=350&h=254",
        "Viktor Arvidsson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3120307.png&w=350&h=254",
        "Ryan McDonagh": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4954.png&w=350&h=254",
        "Torey Krug": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2952729.png&w=350&h=254",
        "Filip Forsberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2968772.png&w=350&h=254",
        "Sam Gagner": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3808.png&w=350&h=254",
        "Michael Frolik": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3802.png&w=350&h=254",
        "Patrick Eaves": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2864.png&w=350&h=254",
        "William Nylander": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114736.png&w=350&h=254",
        "Jakob Silfverberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590549.png&w=350&h=254",
        "Alex Killorn": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4968.png",
        "Ryan Getzlaf": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2310.png&w=350&h=254",
        "Dion Phaneuf": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2282.png&w=350&h=254",
        "David Backes": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3301.png&w=350&h=254",
        "Mark Giordano": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3006.png&w=350&h=254",
        "Duncan Keith": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2306.png&w=350&h=254",
        "Antoine Roussel": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2524606.png&w=350&h=254",
        "Mark Stone": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5545.png&w=350&h=254",
        "Devan Dubnyk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3242.png&w=350&h=254",
        "Braden Holtby": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5075.png&w=350&h=254",
        "Sergei Bobrovsky": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5571.png&w=350&h=254",
        "Juuse Saros": "http://a.espncdn.com/photo/2014/1223/in_g_sarosj_jv_300x300.jpg",
        "Peter Budaj": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1511.png&w=350&h=254",
        "Philipp Grubauer": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5657.png&w=350&h=254",
        "Cam Talbot": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5734.png&w=350&h=254",
        "Jimmy Howard": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3170.png&w=350&h=254",
        "Pekka Rinne": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3157.png&w=350&h=254",
        "Martin Jones": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5096.png&w=350&h=254",
        "John Gibson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590824.png&w=350&h=254",
        "Aaron Dell": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2501176.png&w=350&h=254",
        "Carey Price": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3231.png&w=350&h=254",
        "Scott Darling": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4972.png&w=350&h=254",
        "Matt Murray": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3067862.png&w=350&h=254",
        "Thomas Greiss": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3375.png&w=350&h=254",
        "Craig Anderson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1929.png&w=350&h=254",
        "Curtis McElhinney": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3187.png&w=350&h=254",
        "Tuukka Rask": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3405.png&w=350&h=254",
        "Robin Lehner": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5283.png&w=350&h=254",
        "Antti Raanta": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3037703.png&w=350&h=254",
        "Corey Crawford": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2339.png&w=350&h=254",
        "Roberto Luongo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/551.png&w=350&h=254",
        "Chad Johnson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5178.png&w=350&h=254",
        "Jonathan Quick": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3634.png&w=350&h=254",
        "James Riemer": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3870.png&w=350&h=254",
        "Anders Nilsson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5514.png&w=350&h=254",
        "Keith Kinkaid": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2557840.png&w=350&h=254",
        "Al Montoya": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3065.png&w=350&h=254",
        "Mike Condon": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3032270.png&w=350&h=254",
        "Ryan Miller": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1549.png&w=350&h=254",
        "Henrik Lundqvist": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3081.png&w=350&h=254",
        "Jacob Markstrom": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5452.png&w=350&h=254",
        "Cam Ward": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1671.png&w=350&h=254",
        "Frederik Andersen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2517899.png&w=350&h=254",
        "Cory Schneider": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3750.png&w=350&h=254"
        }

daydict = {
        "monday":["Grammar School", "Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "Players to Consider This Week", "Players Who Will Regress", "Our Top Picks of the Night", "Our Value Picks of the Night"], 
        "tuesday":["Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "New Injuries", "Returning From Injury", "Injury Replacements", "Buy Low Injury Related Players", "Our Top Picks of the Night", "Our Value Picks of the Night"],
        "wednesday":["Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "Unsustainably High Picks", "Unsustainably Low Picks", "Our Top Picks of the Night", "Our Value Picks of the Night"],
        "thursday":["Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "Players in the News", "Our Top Picks of the Night", "Our Value Picks of the Night"],
        "friday":["Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "Best Players of the Week", "Worst Players of the Week", "Weekend Pickup Suggestions", "Our Top Picks of the Night", "Our Value Picks of the Night"]
        }

podcast_type = raw_input("Enter a podcast type (monday, tuesday, etc) or leave blank for custom: ").lower()
titles = []
if podcast_type:
    titles = daydict[podcast_type]

if not titles:
    titles = []
    while True:
        title = raw_input("Enter a title for a section, or leave empty to move on to adding players to your sections: ")
        if not title:
            break
        titles.append(title)

for title in titles:
    print "Starting section " + title
    html += "<p class=\"players-interlude\">\n    " + title + "\n</p>\n\n<div class=\"players\">\n"
    while True:
        player = raw_input("Enter a player name, or leave empty to complete the section: ")
        if not player:
            break
        image = ""
        if player in imagedict:
            image = imagedict[player]
        html += "    <div class=\"tooltip\">\n        <img class=\"img-circle\" style=\"height:5em;\" src=\"" + image + "\">\n        <br>\n        <span class=\"tooltiptext\">" + player + "</span>\n    </div>\n"
    html += "</div>\n\n"
    print "Completed section " + title + "\n"
print html
raw_input()
