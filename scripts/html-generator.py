import fileinput

episode_number = raw_input("Enter episode number: ")
page_title = raw_input("Enter a title for the page: ") + " | Fantasy Hockey Podcast"
page_description = raw_input("Enter a description for the page: ")
youtube_link = raw_input("Enter YouTube link (optional): ")
page_image = raw_input("Enter an image for the page: ")
pod_url = raw_input("Add a url for the cast: ")
pod_length = raw_input("Length of pod (in minutes): ")
daydict = {
        "monday":{"show_notes":["Grammar School", "Week Review", "Injury News", "Drop Candidates", "Long Term Pickup Suggestions", "Schedule Info", "Short Term Pickup Suggestions"], "titles":["Grammar School", "Week's Notable Players", "Injury News", "Drop Candidates", "Long Term Pickup Suggestions", "Short Term Pickup Suggestions"]},
        "wednesday":{"show_notes":["Unsustainably High", "Unsustainably Low", "Sustainably High", "Sustainably Low"], "titles":["Unsustainably High Picks", "Unsustainably Low Picks", "Sustainably High Picks", "Sustainably Low Picks (Trade or Drop Options)"]},
        "friday":{"show_notes":["Ten Takes", "Schedule Info", "Weekend Pickup Suggestions"], "titles":["Ten Takes", "Weekend Pickup Suggestions"]},
        "saturday":{"show_notes":["Game Previews", "Goalie Ranking", "Sit/Start Picks"], "titles":["Top Goalies", "Start Picks", "Sit Picks"]}
        }
podcast_type = raw_input("Enter a podcast type (monday, tuesday, etc) or leave blank for custom: ").lower()
show_notes_list = []
if podcast_type:
    show_notes_list = daydict[podcast_type]["show_notes"]

if not show_notes_list:
    show_notes_list = []
    while True:
        note = raw_input("Enter a show note (ie: Grammar School) or leave empty to complete show notes: ")
        if not note:
            break
        show_notes_list.append(note)

show_notes = ""
for note in show_notes_list:
    time_string = raw_input("Enter a time for note " + note + ": ")
    if not time_string:
        continue
    time_array = time_string.split(":")
    if show_notes == "":
        show_notes = "\n    "
    else:
        show_notes += "\n    <br>"
    time_int = 0
    array_length = len(time_array)
    for i in range(0, array_length):
        magnitude = array_length-1 - i
        time_section = time_array[i]
        if magnitude == 0:
            time_int += int(time_section)
        elif magnitude == 1:
            time_int += int(time_section)*60
        else:
            time_int += int(time_section)*3600
    show_notes += note + " - " + "<a href=\"#\" onclick=\"audioTime(" + str(time_int) + ");return false;\">" + time_string + "</a>"

gambi_script = raw_input("Enter Gambi's script link: ")
brandon_script = raw_input("Enter Brandon's script link: ")

html = """<!doctype html>
<html>
<head>
    <meta charset=\"utf-8\">
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
    <meta name=\"keywords\" content=\"Hockey, Fantasy, Podast, David Gamboa, NHL, Stanley Cup Playoffs, Playoffs, advice, help, drop, trade, add, waiver wire, Fantasy Hockey Pod, daily, season long, espn, yahoo, sell high, buy low, candidates, best\">
    <meta name=\"author\" content=\"Fantasy Hockey Podcast\">
    <meta name=\"description\" content=""" + "\"" + page_description + """\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <meta name=\"title\" content=\" """ + page_title + """\">
    <meta name=\"image\" content=""" + "\"" + page_image + """\">
    <title>""" + page_title + """</title>
    <!---- FB OPEN GRAPH ---->
    <meta property=\"og:type\"               content=\"article\" />
    <meta property=\"og:description\"        content=""" + "\"" + page_description + """\">
    <meta property=\"og:image\"              content=""" + "\"" + page_image + """\"/>
    <!-- Disable tap highlight on IE -->
    <meta name=\"msapplication-tap-highlight\" content=\"no\">


    <!-- Add to homescreen for Chrome on Android -->
    <meta name=\"mobile-web-app-capable\" content=\"yes\">
    <meta name=\"Hockey On Stats\" content=\"\">
    <link rel=\"icon\" sizes=\"192x192\" href=\"images/fhp.png\">

    <!-- Add to homescreen for Safari on iOS -->
    <meta name=\"Fantasy Hockey Podcast\" content=\"\">
    <link rel=\"apple-touch-icon\" href=\"images/fhp.png\">

    <!-- Tile icon for Win8 (144x144 + tile color) -->
    <meta name=\"msapplication-TileImage\" content=\"images/fhp.png\">
    <meta name=\"msapplication-TileColor\" content=\"#444443\">

    <!-- Color the status bar on mobile devices -->
    <meta name=\"theme-color\" content=\"#444443\">

    <link rel=\"stylesheet\" href=\"https://code.getmdl.io/1.3.0/material.indigo-pink.min.css\">
    <link href='https://fonts.googleapis.com/css?family=Product+Sans' rel='stylesheet' type='text/css'>
    <!-- Material Design icons -->
    <link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/icon?family=Material+Icons\">

    <!-- Your styles -->
    <link rel=\"stylesheet\" href=\"styles/main.css\">
    <link rel=\"stylesheet\" href=\"styles/styles.css\">
    <script defer src=\"https://code.getmdl.io/1.3.0/material.min.js\"></script>

</head>
<body class=\"mdl mdl-color--grey-100 mdl-color-text--grey-700 mdl-base\">
      
    <!---TOP HEADER-->
   <!-- Always shows a header, even in smaller screens. -->
    <div class=\"mdl-layout mdl-js-layout mdl-layout--fixed-header\">
        <header class=\"mdl-layout__header mdl-layout__header--transparent \">
            <div  class=\"mdl-layout__header-row mdl-shadow--4dp\" style=\"padding-left:10px\">
                <!-- Title -->
                <a href=\"http://www.fantasyhockeypodcast.com\"><img src=\"/images/fhp.png\" width=\"40px\" style=\"padding-left:5px\"></a><span class=\"mdl-layout-title\" style=\"padding-left:10px\"> """ + page_title + """</span>
      <!-- Add spacer, to align navigation to the right -->
      <div class=\"mdl-layout-spacer\"></div>
      <!-- Navigation. We hide it in small screens. -->
    </div>
  </header>
   
  <main  style=\"background:white;\" class=\"mdl-layout__content\">
      
      
      
    <div class=\"page-content\">
        <img style=\"max-width:100%; opacity:.8; margin:auto; display:block\" src=""" + "\"" + page_image + """\">
        <div class=\"container mdl-grid\">
        <div class=\"mdl-cell mdl-cell--2-col mdl-cell--hide-tablet mdl-cell--hide-phone\"></div>
        <div  class=\"content mdl-color--white mdl-shadow--4dp content mdl-color-text--grey-800 mdl-cell mdl-cell--8-col\">
        <div class=\"opener\">
        
        <p style=\"font-style:italic;opacity:.5;\">Episode """ + episode_number + """ - """ + page_title + """</p>

        <p> 
            <audio id=\"audio\" controls style=\"width:70%;opacity:1;\">
            <source src=""" + "\"" + pod_url + """\" type=\"audio/mpeg\">
                Your browser does not support the audio element.
            </audio>
            <button id="speed-button" class="mdl-button mdl-js-button" onclick="changeAudioSpeed();return false;">1.0x</button>
            """
if len(youtube_link) > 0:
    html += "<a style=\"color:black;\" href=\"" + youtube_link + "\"><img style=\"width: 15%; padding-left: 10px;\" src=\"images/yt_logo_mono.png\"></a>"

html += """
        </p>
        <!----ITUNES--->
        <a href=\"https://itunes.apple.com/us/podcast/fantasy-hockey-podcast/id1198704323\">
        <img src=\"http://matepodcast.com/wp-content/uploads/2016/05/get-it-on-itunes-badge-440x160.png\" width='20%'></a> 
                  
        <!-----GOOGLE PLAY---->
        <a href=\"https://goo.gl/app/playmusic?ibi=com.google.PlayMusic&isi=691797987&ius=googleplaymusic&link=https://play.google.com/music/m/Igp5eo4jiymytfxf3uyffggtbyq?t%3DFantasy_Hockey_Podcast%26pcampaignid%3DMKT-na-all-co-pr-mu-pod-16\">
        <img src=\"https://play.google.com/intl/en_us/badges-music/images/badges/en_badge_web_music.png\" width='20%'></a>
        <a href=\"https://www.patreon.com/fantasyhockeypodcast\"><img src=\"/images/patreon.png\" width=\"20%\"/></a>
        <a href=\"https://discord.gg/pWjCv3g\"><img src=\"/images/discord.png\" width=\"20%\"/></a>
        </div>    
        <div class=\"ellipses\"><iron-icon  icon=\"filter-list\" stylue></iron-icon></div>
        <div class=\"interlude fb\">
        <div class=\"article-content\">
        
        <!------ ARTICLE BEGINS -----> 
        
        <p class=\"interlude\">
            Summary
        </p>

        <p class=\"main-paragraphs\"><text class=\"first-letter\">""" + page_description[0] + """</text>""" + page_description[1:] + """</p>
        <p class=\"interlude\">
            Show Notes
        </p>

        <p class=\"main-paragraphs notes\">
        """ + show_notes + """
        </p>
        
        <p class=\"interlude\">
            Scripts
        </p>

        <p class=\"main-paragraphs notes\">"""
html += "<a href=\"" + gambi_script + "\" target=\"_blank\">Gambi's script</a><br>"
html += "<a href=\"" + brandon_script + "\" target=\"_blank\">Brandon's script</a><br>"
html += """
        </p>

        <p class=\"interlude\">
            Players Talked About
        </p>
"""

html_close = """
</div>
</div>
</div>
</main>
<div style=\"position:relative;\">
    <div id=\"view-source\">
    <button id=\"menu-top-right\" class=\"mdl-button mdl-js-button mdl-button--fab mdl-color--grey-300\">
    <i id=\"fab\" class=\"material-icons share\">share</i>
    </button>
    <ul class=\"mdl-menu mdl-menu--top-right mdl-js-menu mdl-js-ripple-effect\" for=\"menu-top-right\">
        <li class=\"mdl-menu__item\"><div style=\"left:50px;\" class=\"fb-share-button\" data-href=\"http://fantasyhockeypodcast.com\" data-layout=\"button\"></div></li>
        <li class=\"mdl-menu__item\"><div style=\"margin-left:53%;margin-top:10%;\"><a href=\"https://twitter.com/share\" class=\"twitter-share-button\" data-via=\"FantasyHockeyPD\" data-related=\"Daveedgamboa\">Tweet</a>
        <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script></div></li>
    </ul>
    </div>
</div>
    <!-- build:js(app/) ../../scripts/main.min.js -->
    <script src=\"scripts/main.js\"></script>
    <!-- endbuild -->
    
    <script>
        function audioTime(audioTime) {
            var audio = document.getElementById("audio");
            audio.currentTime = audioTime;
            audio.play();
        }

        function changeAudioSpeed() {
            var audio = document.getElementById("audio");
            var speedButton = document.getElementById("speed-button");
            switch(audio.playbackRate) {
                case 1.0:
                    audio.playbackRate = 1.5;
                    speedButton.innerText = "1.5x"
                    break;
                case 1.5:
                    audio.playbackRate = 2.0;
                    speedButton.innerText = "2.0x"
                    break;
                default:
                    audio.playbackRate = 1.0;
                    speedButton.innerText = "1.0x"
                    break;
            }
        }
    </script>
     
    <script>

        (function(document){
              var div = document.getElementById('menu-top-right');
              var icon = document.getElementById('fab');
              var open = false;

              div.addEventListener('click', function(){
                if(open){
                  icon.className = 'material-icons share';  
                } else{
                  icon.className = 'material-icons share open';
                }

                open = !open;
              });
            })(document);
    </script>
      
    <div id=\"fb-root\"></div>
      <script>(function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = \"//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.5&appId=129264100505161\";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));</script>
      
      
      
    
    <!-- build:js(app/) ../../scripts/main.min.js -->
    <script src=\"scripts/main.js\"></script>
    <!-- endbuild -->

    <!-- Google Analytics: change UA-XXXXX-X to be your site's ID -->
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-61894957-3', 'auto');
  ga('send', 'pageview');

</script>
    <!-- Built with love using Web Starter Kit -->
      </div></main></div>
  </body>
</html>
"""

imagedict = {
    "Alex Ovechkin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3101.png&w=350&h=254",
    "Brent Burns": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2300.png&w=350&h=254",
    "Evgeni Malkin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3124.png&w=350&h=254",
    "Sidney Crosby": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114.png&w=350&h=254",
    "Brad Marchand": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3852.png&w=350&h=254",
    "Connor McDavid": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3895074.png&w=350&h=254",
    "Joe Pavelski": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3451.png&w=350&h=254",
    "Ryan Kesler": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2175.png&w=350&h=254",
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
    "Matthew Tkachuk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024854.png&w=350&h=254",
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
    "Evgeny Kuznetsov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5647.png&w=350&h=254",
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
    "Alex Killorn": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4968.png&w=350&h=254",
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
    "Juuse Saros": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042109.png&w=350&h=254",
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
    "Cory Schneider": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3750.png&w=350&h=254",
    "Kris Letang": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3539.png&w=350&h=254",
    "Nikita Zaitsev": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4010739.png&w=350&h=254",
    "Calle Jarnkrok": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2555316.png&w=350&h=254",
    "Kenny Agostino": "https://nhl.bamcontent.com/images/headshots/current/168x168/8475844.jpg",
    "Kevin Hayes": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5767.png&w=350&h=254",
    "Ondrej Palat": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590389.png&w=350&h=254",
    "Mike Smith": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1971.png&w=350&h=254",
    "Brett Connolly": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5479.png&w=350&h=254",
    "Tyler Johnson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5706.png&w=350&h=254",
    "Bo Horvat": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042002.png&w=350&h=254",
    "Paul Stastny": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3467.png&w=350&h=254",
    "Tyler Bozak": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5347.png&w=350&h=254",
    "Taylor Hall": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5428.png&w=350&h=254",
    "Max Domi": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042014.png&w=350&h=254",
    "Scott Hartnell": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/346.png&w=350&h=254",
    "Bryan Rust": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2591155.png&w=350&h=254",
    "Andre Burakovsky": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042044.png&w=350&h=254",
    "Nikita Zadorov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042021.png&w=350&h=254",
    "Tyson Barrie": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5181.png&w=350&h=254",
    "Sven Baertschi": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562597.png&w=350&h=254",
    "Brady Skjei": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976856.png&w=350&h=254",
    "Travis Konecny": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3900169.png&w=350&h=254",
    "David Savard": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5427.png&w=350&h=254",
    "Drew Stafford": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3327.png&w=350&h=254",
    "Brendan Gallagher": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5614.png&w=350&h=254",
    "Chris Kunitz": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2179.png&w=350&h=254",
    "Vladislav Namestnikov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562622.png&w=350&h=254",
    "Loui Eriksson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3161.png&w=350&h=254",
    "Thomas Vanek": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3045.png&w=350&h=254",
    "Jake Guentzel": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042083.png&w=350&h=254",
    "Ondrej Pavelec": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3502.png&w=350&h=254",
    "Johnny Gaudreau": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563039.png&w=350&h=254",
    "Cody Eakin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5237.png&w=350&h=254",
    "Brian Elliott": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2865.png&w=350&h=254",
    "Martin Hanzal": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3537.png&w=350&h=254",
    "Jake Muzzin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4906.png&w=350&h=254",
    "Jason Chimera": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1067.png&w=350&h=254",
    "Jonathan Huberdeau": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562606.png&w=350&h=254",
    "Michal Neuvirth": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3705.png&w=350&h=254",
    "David Perron": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3792.png&w=350&h=254",
    "Tomas Hertl": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976844.png&w=350&h=254",
    "Patrik Berglund": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3693.png&w=350&h=254",
    "Patrick Sharp": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2002.png&w=350&h=254",
    "Gustav Nyquist": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5823.png&w=350&h=254",
    "Alex Chiasson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590705.png&w=350&h=254",
    "Nick Leddy": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5447.png&w=350&h=254",
    "Oliver Ekman-Larsson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5488.png&w=350&h=254",
    "Nick Cousins": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563027.png&w=350&h=254",
    "Mikko Rantanen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899938.png&w=350&h=254",
    "Antoine Vermette": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1939.png&w=350&h=254",
    "Nick Bjugstad": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5828.png&w=350&h=254",
    "Sebastian Aho": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3904173.png&w=350&h=254",
    "Dylan Larkin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114755.png&w=350&h=254",
    "Nathan MacKinnon": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3041969.png&w=350&h=254",
    "Josh Leivo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590559.png&w=350&h=254",
    "Brock Nelson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5798.png&w=350&h=254",
    "Cam Fowler": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5495.png&w=350&h=254",
    "Josh Bailey": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5056.png&w=350&h=254",
    "Aleksander Barkov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3041970.png&w=350&h=254",
    "Jonathan Marchessault": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2967072.png&w=350&h=254",
    "Matt Duchene": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5161.png&w=350&h=254",
    "Oliver Bjorkstrand": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042095.png&w=350&h=254",
    "Justin Faulk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5746.png&w=350&h=254",
    "Ryan Strome": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562636.png&w=350&h=254",
    "Connor Hellebuyck": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3020225.png&w=350&h=254",
    "Louis Domingue": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2560083.png&w=350&h=254",
    "Ondrej Kase": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3151430.png&w=350&h=254",
    "Jaromir Jagr": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/405.png&w=350&h=254",
    "Stefan Noesen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562623.png&w=350&h=254",
    "Aaron Ekblad": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114717.png&w=350&h=254",
    "Damon Severson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3068087.png&w=350&h=254",
    "Oscar Klefbom": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562608.png&w=350&h=254",
    "Mika Zibanejad": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562637.png&w=350&h=254",
    "Anthony Mantha": "http://tsnimages.tsn.ca/ImageProvider/PlayerHeadshot?seoId=anthony-mantha&width=620&height=620",
    "Radim Vrbata": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1323.png&w=350&h=254",
    "Derick Brassard": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3506.png&w=350&h=254",
    "Jake Gardiner": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5830.png&w=350&h=254",
    "Josh Morrissey": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042016.png&w=350&h=254",
    "Sami Vatanen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590835.png&w=350&h=254",
    "Connor Brown": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3067951.png&w=350&h=254",
    "Erik Johnson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3649.png&w=350&h=254",
    "Zack Smith": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5025.png&w=350&h=254",
    "Sam Reinhart": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114722.png&w=350&h=254",
    "Bobby Ryan": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3264.png&w=350&h=254",
    "Jacob Trouba": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976839.png&w=350&h=254",
    "Ryan Dzingel": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3070196.png&w=350&h=254",
    "Alex Galchenyuk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2966502.png&w=350&h=254",
    "David Krejci": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3343.png&w=350&h=254",
    "Shayne Gostisbehere": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3025662.png&w=350&h=254",
    "Mathieu Perreault": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3886.png&w=350&h=254",
    "Carter Hutton": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5420.png&w=350&h=254",
    "Richard Panik": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5332.png&w=350&h=254",
    "Reilly Smith": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2500990.png&w=350&h=254",
    "Henrik Zetterberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1964.png&w=350&h=254",
    "Jimmy Vesey": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069397.png&w=350&h=254",
    "Jordan Eberle": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5032.png&w=350&h=254",
    "Ron Hainsey": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2722.png&w=350&h=254",
    "Marc-Andre Fleury": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2346.png&w=350&h=254",
    "Gabriel Landeskog": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562609.png&w=350&h=254",
    "Ben Bishop": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3866.png&w=350&h=254",
    "Michael Stone": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5148.png&w=350&h=254",
    "Jason Spezza": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1183.png&w=350&h=254",
    "Anze Kopitar": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3183.png&w=350&h=254",
    "Alex Petrovic": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5620.png&w=350&h=254",
    "Jonathan Toews": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3669.png&w=350&h=254",
    "Nicholas Baptiste": "http://cdn1-www.hockeysfuture.com/assets/uploads/2013/05/nick_baptiste.jpg",
    "Laurent Brossoit": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3026526.png&w=350&h=254",
    "Travis Zajac": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3321.png&w=350&h=254",
    "Jakob Chychrun": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024950.png&w=350&h=254",
    "Tobias Rieder": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2564163.png&w=350&h=254",
    "Tanner Pearson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976860.png&w=350&h=254",
    "Tyler Toffoli": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5550.png&w=350&h=254",
    "Jason Pominville": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1531.png&w=350&h=254",
    "Ian Cole": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4991.png&w=350&h=254",
    "Andrew Ladd": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3191.png&w=350&h=254",
    "Andrei Markov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/574.png&w=350&h=254",
    "Roman Josi": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5436.png&w=350&h=254",
    "Zach Parise": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2975.png&w=350&h=254",
    "Dan Girardi": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3423.png&w=350&h=254",
    "Calvin Pickard": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5524.png&w=350&h=254",
    "Nick Schmaltz": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114770.png&w=350&h=254",
    "Sam Bennett": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114732.png&w=350&h=254",
    "Andrei Vasilevskiy": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976847.png&w=350&h=254",
    "Colton Parayko": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069341.png&w=350&h=254",
    "Marian Gaborik": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/290.png&w=350&h=254",
    "Alex Burrows": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3259.png&w=350&h=254",
    "Mark Streit": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3256.png&w=350&h=254",
    "Jiri Hudler": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2120.png&w=350&h=254",
    "Ryan White": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3813.png&w=350&h=254",
    "Jyrki Jokipakka": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5813.png&w=350&h=254",
    "Brian Boyle": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3648.png&w=350&h=254",
    "Tomas Jurco": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563055.png&w=350&h=254",
    "Zach Sanford": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042061.png&w=350&h=254",
    "Curtis Lazar": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042023.png&w=350&h=254",
    "Josh Ho-Sang": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114797.png&w=350&h=254",
    "Valtteri Filppula": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3144.png&w=350&h=254",
    "P.A. Parenteau": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2101.png&w=350&h=254",
    "Jarome Iginla": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/401.png&w=350&h=254",
    "Viktor Stalberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5355.png&w=350&h=254",
    "Xavier Ouellet": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563079.png&w=350&h=254",
    "Andreas Athanasiou": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3068035.png&w=350&h=254",
    "Mark Borowiecki": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2555470.png&w=350&h=254",
    "Jaccob Slavin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069836.png&w=350&h=254",
    "Johnny Boychuk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2072.png&w=350&h=254",
    "Radek Faksa": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976842.png&w=350&h=254",
    "P.K. Subban": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4044.png&w=350&h=254",
    "Jack Eichel": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3648002.png&w=350&h=254",
    "Conor Sheary": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3149827.png&w=350&h=254",
    "Mike Cammalleri": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1517.png&w=350&h=254",
    "James Reimer": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3870.png&w=350&h=254",
    "Michael Grabner": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3558.png&w=350&h=254",
    "Morgan Rielly": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976833.png&w=350&h=254",
    "Esa Lindell": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069352.png&w=350&h=254",
    "Micheal Ferland": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5579.png&w=350&h=254",
    "Joe Thornton": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/939.png&w=350&h=254",
    "John Carlson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5118.png&w=350&h=254",
    "Petr Mrazek": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5619.png&w=350&h=254",
    "T.J. Brodie": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5162.png&w=350&h=254",
    "Jake Allen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5111.png&w=350&h=254",
    "Carl Hagelin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2300267.png&w=350&h=254",
    "Kyle Turris": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3892.png&w=350&h=254",
    "Ryan Ellis": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5169.png&w=350&h=254",
    "Jean-Gabriel Pageau": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2593131.png&w=350&h=254",
    "Nick Bonino": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4927.png&w=350&h=254",
    "Jordan Staal": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3541.png&w=350&h=254",
    "Fredrik Claesson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2564148.png&w=350&h=254",
    "Daniel Sedin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/836.png&w=350&h=254",
    "Semyon Varlamov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3759.png&w=350&h=254",
    "Ryan Pulock": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042019.png&w=350&h=254",
    "Steve Mason": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3657.png&w=350&h=254",
    "Alex DeBrincat": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4063433.png&w=350&h=254",
    "Mathew Barzal": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899946.png&w=350&h=254",
    "Brayden Point": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3151187.png&w=350&h=254",
    "Nico Hischier": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233555.png&w=350&h=254",
    "Nolan Patrick": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233544.png&w=350&h=254",
    "Kailer Yamamoto": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233648.png&w=350&h=254",
    "Jakub Vrana": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114747.png&w=350&h=254",
    "Anders Bjork": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3151742.png&w=350&h=254",
    "Zdeno Chara": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/145.png&w=350&h=254",
    "Julius Honka": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114754.png&w=350&h=254",
    "James Neal": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3227.png&w=350&h=254",
    "Brock Boeser": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899979.png&w=350&h=254",
    "Vadim Shipachyov": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Vadim_Shipachev_May_4%2C_2014.jpg/230px-Vadim_Shipachev_May_4%2C_2014.jpg",
    "Evgenii Dadonov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4969.png&w=350&h=254",
    "Clayton Keller": "http://cdn3.sportngin.com/attachments/roster_player_info/6303/7766/USA_KELLER_CLAYTON_medium.jpg",
    "Steven Stamkos": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5037.png&w=350&h=254",
    "Shea Theodore": "https://nhl.bamcontent.com/images/headshots/current/168x168/8477447.jpg",
    "Alex Pietrangelo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4013.png&w=350&h=254",
    "Ryan Hartman": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042063.png&w=350&h=254",
    "John Klingberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590751.png&w=350&h=254",
    "Brandon Saad": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563065.png&w=350&h=254",
    "Mike Green": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3172.png&w=350&h=254",
    "Jake DeBrusk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3900240.png&w=350&h=254",
    "Dustin Brown": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2288.png&w=350&h=254",
    "Ryan Spooner": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5544.png&w=350&h=254",
    "Charlie McAvoy": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3988803.png&w=350&h=254",
    "Leo Komarov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590558.png&w=350&h=254",
    "Kari Lehtonen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2106.png&w=350&h=254",
    "Thomas Chabot": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3900219.png&w=350&h=254",
    "Olli Maatta": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976850.png&w=350&h=254",
    "Will Butcher": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042169.png&w=350&h=254",
    "Kevin Labanc": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3151792.png&w=350&h=254",
    "Vladimir Sobotka": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3714.png&w=350&h=254",
    "Sean Couturier": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562601.png&w=350&h=254",
    "Jesper Bratt": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4268771.png&w=350&h=254",
    "Sonny Milano": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114756.png&w=350&h=254",
    "Martin Frk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3068036.png&w=350&h=254",
    "Jan Rutta": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4230583.png&w=350&h=254",
    "Jaroslav Halak": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3116.png&w=350&h=254",
    "Nail Yakupov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2966500.png&w=350&h=254",
    "Nate Schmidt": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3024798.png&w=350&h=254",
    "Jonathan Drouin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3041971.png&w=350&h=254",
    "Alex Tuch": "http://www.hockeydb.com/ihdb/photos/alex-tuch-2017-2331.jpg",
    "Sven Andrighetto": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042092.png&w=350&h=254",
    "Alec Martinez": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3927.png&w=350&h=254",
    "Chris Stewart": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3526.png&w=350&h=254",
    "Michael Del Zotto": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5062.png&w=350&h=254",
    "Mikhail Sergachev": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024868.png&w=350&h=254",
    "Andrew Cogliano": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3655.png&w=350&h=254",
    "Brandon Montour": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3115032.png&w=350&h=254",
    "Hampus Lindholm": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2968818.png&w=350&h=254",
    "Alex Iafallo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3652598.png&w=350&h=254",
    "Josh Manson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590829.png&w=350&h=254",
    "Christian Djoos": "http://www.hockeydb.com/ihdb/photos/christian-djoos-2017-49.jpg",
    "Rick Nash": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1569.png&w=350&h=254",
    "Boone Jenner": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563054.png&w=350&h=254",
    "Marcus Johansson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5714.png&w=350&h=254",
    "Marc-Edouard Vlasic": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3371.png&w=350&h=254",
    "Jaden Schwartz": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5835.png&w=350&h=254",
    "Jake Virtanen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114734.png&w=350&h=254",
    "Adrian Kempe": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114802.png&w=350&h=254",
    "Oscar Dansk": "https://b.fssta.com/uploads/application/nhl/players/660780.vresize.350.425.medium.37.png",
    "Derek Dorsett": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3641.png&w=350&h=254",
    "William Karlsson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563057.png&w=350&h=254",
    "Elias Lindholm": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3041994.png&w=350&h=254",
    "Kyle Connor": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899952.png&w=350&h=254",
    "Chris DiDomenico": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4917.png&w=350&h=254",
    "Keith Yandle": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3330.png&w=350&h=254",
    "Pavel Buchnevich": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042081.png&w=350&h=254",
    "Teuvo Teravainen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2592095.png&w=350&h=254",
    "Phillip Danault": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562602.png&w=350&h=254",
    "Ivan Provorov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899939.png&w=350&h=254",
    "Kyle Palmieri": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5517.png&w=350&h=254",
    "Colin Miller": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590796.png&w=350&h=254",
    "Adam Larsson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562610.png&w=350&h=254",
    "Joel Edmundson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563034.png&w=350&h=254",
    "Josh Anderson": "http://www.sportsnet.ca/wp-content/uploads/players/nhl/j/josh-anderson.png",
    "Lee Stempniak": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3083.png&w=350&h=254",
    "Tom Wilson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2970615.png&w=350&h=254",
    "Lars Eller": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3946.png&w=350&h=254",
    "Alex Goligoski": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3757.png&w=350&h=254",
    "Artem Anisimov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3756.png&w=350&h=254",
    "Sean Monahan": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3041996.png&w=350&h=254",
    "Anton Khudobin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3760.png&w=350&h=254",
    "Tyler Myers": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5052.png&w=350&h=254",
    "Darnell Nurse": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3041997.png&w=350&h=254",
    "Brent Seabrook": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2389.png&w=350&h=254",
    "David Rittich": "https://b.fssta.com/uploads/application/nhl/players/918210.vresize.350.425.medium.46.png",
    "Malcolm Subban": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976852.png&w=350&h=254",
    "Bryan Little": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3508.png&w=350&h=254",
    "Cody Franson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3422.png&w=350&h=254",
    "Mattias Ekholm": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2558631.png&w=350&h=254",
    "Alexander Edler": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3464.png&w=350&h=254",
    "Justin Williams": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1023.png&w=350&h=254",
    "Jeff Petry": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5407.png&w=350&h=254",
    "Alexander Kerfoot": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069394.png&w=350&h=254",
    "Darcy Kuemper": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2610321.png&w=350&h=254",
    "Tristan Jarry": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042020.png&w=350&h=254",
    "Seth Jones": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3041992.png&w=350&h=254",
    "Anton Forsberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3036851.png&w=350&h=254",
    "Rickard Rakell": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562629.png&w=350&h=254",
    "Adam Henrique": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5074.png&w=350&h=254",
    "Scott Wedgewood": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5622.png&w=350&h=254",
    "Jesse Puljujarvi": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024839.png&w=350&h=254",
    "Craig Smith": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2570752.png&w=350&h=254",
    "Daniel Carr": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3025657.png&w=350&h=254",
    "Pierre-Luc Dubois": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024833.png&w=350&h=254",
    "Michael Raffl": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3037290.png&w=350&h=254",
    "Joonas Korpisalo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069266.png&w=350&h=254",
    "Alexander Steen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3113.png&w=350&h=254",
    "Pierre-Luc Dubois": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024833.png&w=350&h=254",
    "Erik Haula": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2593311.png&w=350&h=254",
    "Kevin Fiala": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114743.png&w=350&h=254",
    "Dmitrij Jaskin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563053.png&w=350&h=254",
    "Justin Abdelkader": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3898.png&w=350&h=254",
    "Trevor van Riemsdyk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3025524.png&w=350&h=254",
    "Radko Gudas": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5502.png&w=350&h=254",
    "Henrik Sedin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/837.png&w=350&h=254",
    "Ryan O'Reilly": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5208.png&w=350&h=254",
    "Danton Heinen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3151741.png&w=350&h=254",
    "Gustav Forsling": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3151784.png&w=350&h=254",
    "Calvin DeHaan": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5266.png&w=350&h=254",
    "Ryan Nugent-Hopkins": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562624.png&w=350&h=254",
    "Jordan Oesterle": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3097115.png&w=350&h=254",
    "Tyler Bertuzzi": "https://nhl.bamcontent.com/images/headshots/current/168x168/8477479.jpg",
    "Jared Spurgeon": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5079.png&w=350&h=254",
    "Vincent Hinostroza": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069613.png&w=350&h=254",
    "Jeff Glass": "https://nhl.bamcontent.com/images/headshots/current/168x168/8471301.jpg",
    "Alex Stalock": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5223.png&w=350&h=254",
    "Daniel Sprong": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3904181.png&w=350&h=254",
    "Yanni Gourde": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3094261.png&w=350&h=254",
    "Jonathan Bernier": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3533.png&w=350&h=254",
    "Trevor Lewis": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3454.png&w=350&h=254",
    "Timo Meier": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899978.png&w=350&h=254",
    "Samuel Girard": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4063401.png&w=350&h=254",
    "Anthony Beauvillier": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3904107.png&w=350&h=254",
    "Casey DeSmith": "http://www.hockeydb.com/ihdb/photos/casey-desmith-2018-50.jpg",
    "Harri Sateri": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5536.png&w=350&h=254",
    "Zach Hyman": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5509.png&w=350&h=254",
    "Greg Pateryn": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4924.png&w=350&h=254",
    "Riley Nash": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5005.png&w=350&h=254",
    "Mike Amadio": "http://www.hockeydb.com/ihdb/photos/mike-amadio-2016-40.jpg",
    "Mikkel Boedker": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3976.png&w=350&h=254",
    "Nikolay Goldobin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114786.png&w=350&h=254",
    "Joe Morrow": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562617.png&w=350&h=254",
    "Tomas Tatar": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5227.png&w=350&h=254",
    "Eric Fehr": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2290.png&w=350&h=254",
    "Tomas Plekanec": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1933.png&w=350&h=254",
    "Chris Wagner": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590833.png&w=350&h=254",
    "Brandon Davidson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5485.png&w=350&h=254",
    "Ryan Reaves": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3683.png&w=350&h=254",
    "Josh Jooris": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3025655.png&w=350&h=254",
    "Frank Vatrano": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3527554.png&w=350&h=254",
    "Nate Thompson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2688.png&w=350&h=254",
    "Nick Shore": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3027836.png&w=350&h=254",
    "Mark Letestu": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3626.png&w=350&h=254",
    "Nikita Soshnikov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3601768.png&w=350&h=254",
    "Greg McKegg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5663.png&w=350&h=254",
    "Mike Reilly": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563077.png&w=350&h=254",
    "Nick Holden": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3884.png&w=350&h=254",
    "Matt Beleskey": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3929.png&w=350&h=254",
    "Tommy Wingels": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4928.png&w=350&h=254",
    "Jussi Jokinen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3164.png&w=350&h=254",
    "Ryan Carpenter": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3096605.png&w=350&h=254",
    "Brian Dumoulin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5738.png&w=350&h=254",
    "Ivan Barbashev": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114985.png&w=350&h=254",
    "Zach Aston-Reese": "http://sportdesigns.com/images/headshots/noem/astonreese_zach.jpg",
    "Jack Roslovic": "http://www.hockeydb.com/ihdb/photos/jack-roslovic-2017-6378.jpg",
    "John Gilmour": "http://www.hockeydb.com/ihdb/photos/john-gilmour-2017-48.jpg",
    "Brendan Leipsic": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3067485.png&w=350&h=254",
    "Erik Gustafsson": "https://vignette.wikia.nocookie.net/chicagoblackhawks/images/2/2b/Gustafsson.png/revision/latest?cb=20160710153213",
    "Neal Pionk": "https://nhl.bamcontent.com/images/headshots/current/168x168/8480145.jpg",
    "Artturi Lehtonen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042050.png&w=350&h=254",
    "Victor Rask": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563085.png&w=350&h=254",
    "Carter Hart": "https://nhl.bamcontent.com/images/headshots/current/168x168/8479394.jpg",
    "Kristian Vesalainen": "https://files.eliteprospects.com/layout/players/kristian_vesalainen_hpk-1.jpg",
    "Eeli Tolvanen": "https://files.eliteprospects.com/layout/players/ep_15_tolvanen,_eeli.jpg",
    "Stephen Johns": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5759.png&w=350&h=254",
    "Austin Watson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5556.png&w=350&h=254",
    "J.T. Compher": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3041995.png&w=350&h=254",
    "Robby Fabbri": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114774.png&w=350&h=254",
    "Vince Dunn": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3904189.png&w=350&h=254",
    "Kris Russell": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3425.png&w=350&h=254",
    "Gabriel Vilardi": "http://sports.windsorsquare.ca/wp-content/uploads/Gabriel-Vilardi-Spitfires-2.jpg",
    "Spencer Foo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4196967.png&w=350&h=254",
    "Ilya Kovalchuk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1175.png&w=350&h=254",
    "Ty Rattie": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563082.png&w=350&h=254",
    "Dylan Strome": "http://www.hockeydb.com/ihdb/photos/dylan-strome-2018-7166.jpg",
    "Elias Pettersson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233566.png&w=350&h=254",
    "Adam Gaudette": "https://pbs.twimg.com/profile_images/884828588922609664/5POnCNmi_400x400.jpg",
    "Niklas Kronwall": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2127.png&w=350&h=254",
    "Filip Zadina": "http://www.hockeydb.com/ihdb/photos/filip-zadina-2017-2083.jpg",
    "Michael Matheson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976851.png&w=350&h=254",
    "Kasperi Kapanen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114775.png&w=350&h=254",
    "Casey Mittelstadt": "https://gogts.net/wp-content/uploads/2017/04/Casey-Mittelstadt-Green-Bay-Gamblers-USHL.jpg",
    "Andreas Johnsson": "http://www.hockeydb.com/ihdb/photos/andreas-johnsson-2018-38.jpg",
    "Rasmus Dahlin": "http://www.hockeydb.com/ihdb/photos/rasmus-dahlin-2018-7049.jpg",
    "Michael Rasmussen": "http://www3.pictures.zimbio.com/gi/Michael+Rasmussen+2017+NHL+Draft+Round+One+F1RIN29YMPBl.jpg",
    "Juuso Riikola": "https://nhl.bamcontent.com/images/headshots/current/168x168/8480945.jpg",
    "Martin Necas": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233586.png&w=350&h=254",
    "Joe Hicketts": "http://www.hockeydb.com/ihdb/photos/joe-hicketts-2017-34.jpg",
    "Brady Tkachuk": "http://www.hockeydb.com/ihdb/photos/brady-tkachuk-2018-449.jpg",
    "Troy Terry": "https://assets.ngin.com/attachments/profiles/6818/5254/Terry.jpg",
    "Antti Suomela": "http://www.sportti.com/kuvapankki2014/antti_suomela_jyp.jpg",
    "Austin Wagner": "http://www.hockeydb.com/ihdb/photos/austin-wagner-2017-40.jpg",
    "Trevor Daley": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/1978.png&w=350&h=254",
    "Urho Vaakanainen": "https://pbs.twimg.com/profile_images/775368335286497280/www0_27H_400x400.jpg",
    "Valentin Zykov": "https://nhl.bamcontent.com/images/headshots/current/168x168/8477458.jpg",
    "Christian Fischer": "https://nhl.bamcontent.com/images/headshots/current/168x168/8478432.jpg",
    "Filip Hronek": "http://www.hockeydb.com/ihdb/photos/filip-hronek-2018-34.jpg",
    "Dennis Cholowski": "http://www.hockeydb.com/ihdb/photos/dennis-cholowski-2018-34.jpg",
    "Jamie Oleksiak": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562625.png&w=350&h=254",
    "Devante Smith-Pelly": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5542.png&w=350&h=254",
    "Andrej Sekera": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3452.png&w=350&h=254",
    "Joel Armia": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562596.png&w=350&h=254",
    "Jesperi Kotkaniemi": "http://www.hockeydb.com/ihdb/photos/jesperi-kotkaniemi-2019-45.jpg",
    "Artturi Lehkonen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042050.png&w=350&h=254",
    "Tyler Ennis": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5069.png&w=350&h=254",
    "Colton Sissons": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2993474.png&w=350&h=254",
    "Mike Matheson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976851.png&w=350&h=254",
    "Henri Jokiharju": "http://www.hockeydb.com/ihdb/photos/henri-jokiharju-2018-35.jpg",
    "Jack Johnson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3583.png&w=350&h=254",
    "Max Comtois": "https://nhl.bamcontent.com/images/headshots/current/168x168/8480031.jpg",
    "Maxime Lajoie": "http://www.hockeydb.com/ihdb/photos/max-lajoie-2018-54.jpg",
    "Chris Tierney": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3067870.png&w=350&h=254",
    "Linus Ullmark": "http://www.hockeydb.com/ihdb/photos/linus-ullmark-2018-33.jpg",
    "Maxime Comtois": "https://nhl.bamcontent.com/images/headshots/current/168x168/8480031.jpg",
    "Matt Grzelcyk": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069448.png&w=350&h=254",
    "Warren Foegele": "https://nhl.bamcontent.com/images/headshots/current/168x168/8477998.jpg",    
    "Adam Lowry": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563066.png&w=350&h=254",
    "Joonas Donskoi": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590379.png&w=350&h=254",
    "Zachary Sanford": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042061.png&w=350&h=254",
    "Derrick Pouliot": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976834.png&w=350&h=254",
    "Jake McCabe": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3020803.png&w=350&h=254",
    "Andrei Svechnikov": "http://www.hockeydb.com/ihdb/photos/andrei-svechnikov-2019-979.jpg",
    "Dominik Simon": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3913226.png&w=350&h=254",
    "Slava Voynov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5028.png&w=350&h=254",
    "Pontus Aberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069396.png&w=350&h=254",
    "Jack Campbell": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5473.png&w=350&h=254",
    "Miro Heiskanen": "http://www.hockeydb.com/ihdb/photos/miro-heiskanen-2018-233.jpg",
    "Drake Caggiula": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3025590.png&w=350&h=254",
    "Oskar Lindblom": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3151326.png&w=350&h=254",
    "Mathieu Joseph": "https://nhl.bamcontent.com/images/headshots/current/168x168/8478472.jpg",
    "Cedric Paquette": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3067906.png&w=350&h=254",
    "Cal Petersen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042182.png&w=350&h=254",
    "Drake Batherson": "http://www.hockeydb.com/ihdb/photos/drake-batherson-2018-54.jpg",
    "Jordan Martinook": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2989376.png&w=350&h=254",
    "Gavin Bayreuther": "http://www.hockeydb.com/ihdb/photos/gavin-bayreuther-2018-233.jpg",
    "Mikko Koskinen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5268.png",
    "Jakob Forsbacka Karlsson": "https://nhl.bamcontent.com/images/headshots/current/168x168/8478417.jpg",
    "Noah Hanifin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3652964.png&w=350&h=254",
    "Anthony Stolarz": "http://www.hockeydb.com/ihdb/photos/anthony-stolarz-2015-53.jpg",
    "Michal Kempny": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4046946.png&w=350&h=254",
    "Brendan Perlini": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114744.png&w=350&h=254",
    "Adin Hill": "https://nhl.bamcontent.com/images/headshots/current/168x168/8478499.jpg",
    "Colin White": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3900259.png&w=350&h=254",
    "William Carrier": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042054.png",
    "Oscar Lindberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590850.png&w=350&h=254",
    "Carl Soderberg": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3387.png",
    "Henrik Borgstrom": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024977.png&w=350&h=254",
    "Jori Lehtera": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2502890.png&w=350&h=254",
    "Paul Byron": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4568.png&w=350&h=254",
    "Adam McQuaid": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3205.png&w=350&h=254",
    "Pheonix Copley": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3095330.png&w=350&h=254",
    "MacKenzie Blackwood": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3904177.png&w=350&h=254",
    "Matt Nieto": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563076.png&w=350&h=254",
    "Brandon Pirri": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5525.png&w=350&h=254",
    "Thatcher Demko": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4392546.png&w=350&h=254",
    "Jordan Binnington": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590874.png&w=350&h=254",
    "Tage Thompson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024988.png&w=350&h=254",
    "Conor Garland": "http://www.hockeydb.com/ihdb/photos/conor-garland-2018-7166.jpg",
    "Jordan Greenway": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3900260.png&w=350&h=254",
    "Blake Coleman": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2563026.png&w=350&h=254",
    "Oskar Sundqvist": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069277.png&w=350&h=254",
    "Derek Grant": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2525884.png&w=350&h=254",
    "Max Jones": "http://www.hockeydb.com/ihdb/photos/max-jones-2019-4312.jpg",
    "Devin Shore": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069353.png&w=350&h=254",
    "Ben Hutton": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3571762.png&w=350&h=254",
    "Luke Schenn": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5092.png&w=350&h=254",
    "Joe Blandisi": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4392639.png&w=350&h=254",
    "Pat Maroon": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3853.png&w=350&h=254",
    "Lawson Crouse": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899951.png&w=350&h=254",
    "Quinn Hughes": "https://mgoblue.com/images/2017/9/26/20170925_IHM_Hughes.jpg?width=300",
    "Erik Cernak": "http://www.hockeydb.com/ihdb/photos/erik-cernak-2018-55.jpg",
    "Filip Chytil": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233643.png&w=350&h=254",
    "Garret Sparks": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590569.png&w=350&h=254",
    "Brandon Tanev": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3096236.png&w=350&h=254",
    "Brock McGinn": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3067868.png&w=350&h=254",
    "Luke Kunin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4271610.png&w=350&h=254",
    "Kevin Boyle": "http://www.hockeydb.com/ihdb/photos/kevin-boyle-2018-4312.jpg",
    "Ryan Donato": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3115033.png&w=350&h=254",
    "Ben Lovejoy": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3993.png",
    "Devon Toews": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3096249.png&w=350&h=254",
    "Alexandar Georgiev": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4239677.png&w=350&h=254",
    "Nick Ritchie": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114742.png&w=350&h=254",
    "Tyler Jost": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024879.png&w=350&h=254",
    "Anthony Duclair": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042086.png&w=350&h=254",
    "Samuel Montembeault": "http://www.hockeydb.com/ihdb/photos/samuel-montembeault-2019-7600.jpg",
    "Tony DeAngelo": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114769.png&w=350&h=254",
    "Travis Sanheim": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114757.png&w=350&h=254",
    "Jared McCann": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114777.png&w=350&h=254",
    "Jamie McGinn": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3652.png&w=350&h=254",
    "Brendan Guhle": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4392199.png&w=350&h=254",
    "Vinnie Hinostroza": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069613.png&w=350&h=254",
    "Zack Kassian": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5194.png&w=350&h=254",
    "Brad Richardson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3154.png&w=350&h=254",
    "Tyson Jost": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024879.png&w=350&h=254",
    "Troy Brouwer": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3394.png",
    "Sam Montembeault": "http://www.hockeydb.com/ihdb/photos/samuel-montembeault-2018-234.jpg",
    "Roope Hintz": "https://nhl.bamcontent.com/images/headshots/current/168x168/8478449.jpg",
    "Kurtis Gabriel": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042087.png&w=350&h=254",
    "Andrew Mangiapane": "http://www.hockeydb.com/ihdb/photos/andrew-mangiapane-2019-43.jpg",
    "Igor Shestyorkin": "http://www.hockeysfuture.com/assets/uploads/2014/03/igor_shestyorkin_spartak.jpg",
    "Vitali Kravtsov": "http://www.khl.ru/images/teamplayers/10205/24801.jpg",
    "Erik Brannstrom": "http://www.hockeydb.com/ihdb/photos/erik-brannstrom-2019-54.jpg",
    "Jason Robertson": "http://www.hockeydb.com/ihdb/photos/jason-robertson-2019-233.jpg",
    "Ilya Sorokin": "http://www.khl.ru/images/teamplayers/10130/17800.jpg",
    "Noah Dobson": "https://b.fssta.com/uploads/application/nhl/headshots/5943.vresize.350.425.medium.65.png",
    "Logan Stanley": "http://www.hockeydb.com/ihdb/photos/logan-stanley-2019-6378.jpg",
    "Cody Glass": "https://nhl.bamcontent.com/images/headshots/current/168x168/8479996.jpg",
    "Dante Fabbro": "https://assets.leaguestat.com/hockeycanada/240x240/974.jpg",
    "Bowen Byram": "http://www.hockeydb.com/ihdb/photos/bowen-byram-2019-2807.jpg",
    "Klim Kostin": "http://www.hockeydb.com/ihdb/photos/klim-kostin-2018-36.jpg",
    "Nick Suzuki": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233594.png&w=350&h=254",
    "Ilya Samsonov": "http://www.hockeydb.com/ihdb/photos/ilya-samsonov-2019-49.jpg",
    "Grigori Denisenko": "https://i1.wp.com/dobberprospects.com/wp-content/uploads/sites/4/2019/03/Grigori-Denisenko.jpg?fit=300%2C300&ssl=1",
    "Morgan Frost": "https://nhl.bamcontent.com/images/headshots/current/168x168/8480028.jpg",
    "Ryan Poehling": "https://cdn.nhlpa.com/img/assets/players/headshots/450x450/56088.jpg",
    "Juuso Valimaki": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233611.png&w=350&h=254",
    "Sam Steel": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024998.png&w=350&h=254",
    "Nico Sturm": "https://nhl.bamcontent.com/images/headshots/current/168x168/8481477.jpg",
    "Jordan Kyrou": "http://www.hockeydb.com/ihdb/photos/jordan-kyrou-2018-36.jpg",
    "Nick Merkley": "http://www.hockeydb.com/ihdb/photos/nick-merkley-2019-7166.jpg",
    "Elvis Merzlikins": "http://www.hockeydb.com/ihdb/photos/elvis-merzlikins-2015-2330.jpg",
    "Kaapo Kakko": "http://www.hockeydb.com/ihdb/photos/kaapo-kakko-2019-1231.jpg",
    "Adam Fox": "http://www.hockeydb.com/ihdb/photos/adam-fox-2018-43.jpg",
    "Pavel Francouz": "http://www.hockeydb.com/ihdb/photos/pavel-francouz-2019-690.jpg",
    "Taro Hirose": "http://www.hockeydb.com/ihdb/photos/taro-hirose-2019-34.jpg",
    "Ty Smith": "http://www.hockeydb.com/ihdb/photos/ty-smith-2019-51.jpg",
    "Barrett Hayton": "https://nhl.bamcontent.com/images/headshots/current/168x168/8480849.jpg",
    "Victor Olofsson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3151096.png&w=350&h=254",
    "Evan Bouchard": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4352722.png&w=350&h=254",
    "Cale Makar": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233563.png&w=350&h=254",
    "Zack MacEwen": "http://www.hockeydb.com/ihdb/photos/zack-macewen-2019-39.jpg",
    "Kirill Kaprizov": "https://i1.wp.com/dobberprospects.com/wp-content/uploads/sites/4/2019/03/Kirill-Kaprizov.jpg?fit=300%2C300&ssl=1",
    "Joel Farabee": "http://www.hockeydb.com/ihdb/photos/joel-farabee-2019-53.jpg",
    "Oliver Wahlstrom": "https://assets.leaguestat.com/ahl/240x240/7575.jpg",
    "Adam Boqvist": "http://www.hockeydb.com/ihdb/photos/adam-boqvist-2019-35.jpg",
    "Logan Brown": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024886.png&w=350&h=254",
    "Dillon Dube": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4063268.png&w=350&h=254",
    "Jack Hughes": "https://nhl.bamcontent.com/images/headshots/current/168x168/8481559.jpg",
    "Owen Tippett": "http://www.hockeydb.com/ihdb/photos/owen-tippett-2018-234.jpg",
    "Ivan Chekhovich": "https://files.eliteprospects.com/layout/players/bc_13_chekovich,_ivan.jpg",
    "Garret Sparks": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2590569.png&w=350&h=254",
    "Melker Karlsson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3109556.png&w=350&h=254",
    "Joel Persson": "https://files.eliteprospects.com/layout/players/bb_joelpersson_2018-10-22.jpeg",
    "Sasha Chmelevski": "http://www.hockeydb.com/ihdb/photos/sasha-chmelevski-2018-44.jpg",
    "Nikolai Prokhorkin": "http://www.khl.ru/images/teamplayers/10133/16478.jpg",
    "Carl Grundstrom": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4392584.png&w=350&h=254",
    "Christian Dvorak": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3115035.png&w=350&h=254",
    "Alexander Nylander": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4392182.png&w=350&h=254",
    "Sami Niku": "http://www.hockeydb.com/ihdb/photos/sami-niku-2019-6378.jpg",
    "Dominik Kubalik": "http://www.hockeysfuture.com/assets/uploads/2013/06/dominik_kubalik.jpg",
    "Adam Boqvist": "http://www.hockeydb.com/ihdb/photos/adam-boqvist-2019-35.jpg",
    "Dylan Sikura": "http://ssref.net/scripts/image_resize.cgi?min=200&url=https://d9kjk42l7bfqz.cloudfront.net/req/201905221/images/headshots/sikurdy01-2018.jpg",
    "John Quenneville": "http://www.hockeydb.com/ihdb/photos/john-quenneville-2017-51.jpg",
    "Alex Formenton": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233882.png&w=350&h=254",
    "Dylan Cozens": "http://www.hockeydb.com/ihdb/photos/dylan-cozens-2019-997.jpg",
    "Denis Malgin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3942715.png&w=350&h=254",
    "Noah Juulsen": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3900504.png&w=350&h=254",
    "Max Veronneau": "http://www.hockeydb.com/ihdb/photos/max-veronneau-2019-54.jpg",
    "Rudolfs Balcers": "http://www.hockeydb.com/ihdb/photos/rudolfs-balcers-2019-54.jpg",
    "Christian Wolanin": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3942106.png&w=350&h=254",
    "Ilya Mikheyev": "https://en.khl.ru/images/teamplayers/10145/17692.jpg",
    "Evgeny Svechnikov": "https://nhl.bamcontent.com/images/headshots/current/168x168/8478431.jpg",
    "Jayce Hawryluk": "https://nhl.bamcontent.com/images/headshots/current/168x168/8477963.jpg",
    "Aleksi Heponiemi": "http://www.hockeydb.com/ihdb/photos/aleksi-heponiemi-2018-234.jpg",
    "Libor Hajek": "http://www.hockeydb.com/ihdb/photos/libor-hajek-2019-48.jpg",
    "Alexandre Texier": "http://www2.pictures.zimbio.com/gi/Alexandre+Texier+Ml5osNRMWoYm.jpg",
    "Jake Bean": "http://www.hockeydb.com/ihdb/photos/jake-bean-2018-979.jpg",
    "Brendan Lemieux": "https://nhl.bamcontent.com/images/headshots/current/168x168/8477962.jpg",
    "Michael Dal Colle": "https://assets.leaguestat.com/ahl/240x240/6355.jpg",
    "Dominik Kahun": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4294651.png&w=350&h=254",
    "Brett Howden": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4024989.png&w=350&h=254",
    "Alex Nedeljkovic": "http://www.hockeydb.com/ihdb/photos/alex-nedeljkovic-2019-979.jpg",
    "Haydn Fleury": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114735.png&w=350&h=254",
    "Nikita Gusev": "http://www.hockeydb.com/ihdb/photos/nikita-gusev-2019-5033.jpg",
    "Lias Andersson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4232875.png&w=350&h=254",
    "Emil Bemstrom": "https://cdn2.shl.se/sports/player/portrait/200/qRm-7DyFIL7kE-1519028169.jpg",
    "Ivan Chekovich": "http://www.hockeydb.com/ihdb/photos/ivan-chekhovich-2019-44.jpg",
    "Philippe Myers": "https://a.espncdn.com/i/headshots/nhl/players/full/3042013.png",
    "Alexander Chmelevski": "http://www.hockeydb.com/ihdb/photos/sasha-chmelevski-2019-44.jpg",
    "Oliver Kylington": "https://nhl.bamcontent.com/images/headshots/current/168x168/8478430.jpg",
    "Ethan Bear": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3941966.png&w=350&h=254",
    "Kirby Dach": "http://www.hockeydb.com/ihdb/photos/kirby-dach-2019-1005.jpg",
    "Ville Heinola": "http://www.hockeydb.com/ihdb/photos/ville-heinola-2019-1221.jpg",
    "Sammy Blais": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3149697.png",
    "Cody Ceci": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2976843.png",
    "Sam Lafferty": "http://www.hockeydb.com/ihdb/photos/sam-lafferty-2019-50.jpg",
    "Tim Schaller": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069290.png",
    "Denis Gurianov": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3900147.png&w=350&h=254",
    "Josh Mahura": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4063504.png&w=350&h=254",
    "Korbinian Holzer": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5507.png&w=350&h=254",
    "Nick Paul": "http://www.hockeydb.com/ihdb/photos/nick-paul-1934-5432.jpg",
    "Justin Dowling": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3067879.png&w=350&h=254",
    "Ben Chiarot": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5246.png&w=350&h=254",
    "John Marino": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3941974.png&w=350&h=254",
    "Calvin de Haan": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5266.png",
    "Chris Driedger": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3067263.png",
    "Josh Archibald": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2591154.png",
    "Jujhar Khaira": "https://a.espncdn.com/i/headshots/nhl/players/full/3068670.png",
    "Brayden McNabb": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5202.png&w=350&h=254",
    "Ryan Graves": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042122.png&w=350&h=254",
    "Valeri Nichushkin": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042003.png&w=350&h=254",
    "Anthony Cirelli": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3941973.png&w=350&h=254",
    "Anthony DeAngelo": "https://a.espncdn.com/i/headshots/nhl/players/full/3114769.png",
    "Filip Gustavsson": "https://lscluster.hockeytech.com/download.php?client_code=ahl&file_path=media/b02abab361e5cdf62157fefad9ae5d0b.jpg",
    "Noel Acciari": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3096237.png",
    "Kaapo Kahkonen": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3151341.png&w=350&h=254",
    "Robert Thomas": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4233637.png&w=350&h=254",
    "Dennis Gilbert": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3942030.png&w=350&h=254",
    "Connor Murphy": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2562618.png&w=350&h=254",
    "Adam Pelech": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069621.png&w=350&h=254",
    "Igor Shesterkin": "http://www.hockeydb.com/ihdb/photos/igor-shesterkin-2020-48.jpg",
    "Matt Martin": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5050.png&w=350&h=254",
    "Rasmus Sandin": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4352803.png&w=350&h=254",
    "Andrew Copp": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3042114.png&w=350&h=254",
    "Michael Hutchinson": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5133.png",
    "Barclay Goodrow": "https://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3069411.png",
}

new_player_images = {}
titles = ["Players Discussed"]
if podcast_type:
    titles = daydict[podcast_type]["titles"]

unique_players = []
for title in titles:
    print "Starting section " + title
    players = []
    while True:
        player = raw_input("Enter a player name, or leave empty to complete the section: ")
        if not player:
            break
        players.append(player)

    if len(players) > 0:
        html += "<p class=\"players-interlude\">\n    " + title + "\n</p>\n\n<div class=\"players\">\n"
        for player in players:
            if player not in unique_players:
                unique_players.append(player)
            image = ""
            if player in imagedict:
                image = imagedict[player]
            else:
                image = raw_input("Add image for " + player + ": ")
                new_player_images[player] = image
            html += "    <div class=\"tooltip\">\n        <img class=\"img-circle\" src=\"" + image + "\">\n        <span class=\"tooltiptext\">" + player + "</span>\n    </div>\n"
        html += "</div>\n\n"
    print "Completed section " + title + "\n"

html += html_close

episode_filename = "ep-"+episode_number+".html"

html_file = open("../"+episode_filename, "w")
html_file.write(html)
html_file.close()

if len(new_player_images) > 0:
    print "\n\nAdd the following players and images to the database:\n\n" 
    for player, image in new_player_images.iteritems():
        print "\"" + player + "\": \"" + image + "\","

if len(unique_players) > 0:
    print "\n\nPlayers discussed in this episode: "
    print ", ".join(unique_players)

episode = """
          <!------ EPISODE """ + episode_number + """----->
          <div class=\"mdl-layout__tab-panel is-active\" id=\"overview\">
          <section class=\"section--center mdl-grid mdl-grid--no-spacing mdl-shadow--2dp\">
            <header class=\"section__play-btn episode mdl-cell mdl-cell--3-col-desktop mdl-cell--2-col-tablet mdl-cell--4-col-phone mdl-color-text--white\" style=\"background: url(""" + page_image + """ ) center/cover;\">
            
            </header>
              
            <div class=\"mdl-card mdl-cell mdl-cell--9-col-desktop mdl-cell--6-col-tablet mdl-cell--4-col-phone\">
              <div class=\"mdl-card__supporting-text\">
                <h4 style=\"font-family:product sans;\">""" + page_title + """</h4>
                """ + page_description + """
                <br>
                  
                  <br>
                  <div style=\"opacity:.9;\">
                   <audio controls style=\"width:100%;\">
                      <source src=""" + "\"" + pod_url + """\" type=\"audio/mpeg\">
                            Your browser does not support the audio element.
                      </audio>
                  </div>
              </div>
              <div class=\"mdl-card__actions\">
                <a href=""" + "\"" + episode_filename + """\" class=\"mdl-button mdl-color-text--black mdl-js--ripple\">Read more</a>"""
if len(youtube_link) > 0:
    episode += "<a href=\"" + youtube_link + "\" class=\"mdl-button mdl-color-text--black mdl-js--ripple\"><img style=\"height:50%;padding-bottom: 3px; padding-right: 10px;\" src=\"images/yt_logo_mono.png\"></a>"
episode += """
                 <span style=\"display:inline-block\"><i style=\"vertical-align:middle;opacity:.7;\" class=\"material-icons\">schedule</i>
                  <text style=\"font-size:.8em;opacity:.6\"> """ + pod_length + """ min.</text></span>
                
              </div>
            </div>
          </section>
          </div>
"""

fi = fileinput.input("../index.html",inplace=True)
for line in fi:
    if "<!----- EPISODES START ----->" in line:
        line=line.replace(line,line+episode)
    print line,
fi.close()

raw_input()
