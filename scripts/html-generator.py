html = ""

while True:
    title = raw_input("Enter a title for the section, or leave empty to get stored HTML: ")
    if not title:
        break
    
    html += "<p class=\"players-interlude\">\n    " + title + "\n</p>\n\n<div class=\"players\">\n"
    while True:
        player = raw_input("Enter a player name, or leave empty to complete the section: ")
        if not player:
            break

        html += "    <div class=\"tooltip\">\n        <img class=\"img-circle\" style=\"height:5em;\" src=\"\">\n        <br>\n        <span class=\"tooltiptext\">" + player + "</span>\n    </div>\n"
    html += "</div>\n\n"
print html
