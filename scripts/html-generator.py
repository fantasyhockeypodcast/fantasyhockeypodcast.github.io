html = ""

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

        html += "    <div class=\"tooltip\">\n        <img class=\"img-circle\" style=\"height:5em;\" src=\"\">\n        <br>\n        <span class=\"tooltiptext\">" + player + "</span>\n    </div>\n"
    html += "</div>\n\n"
    print "Completed section " + title + "\n"
print html
