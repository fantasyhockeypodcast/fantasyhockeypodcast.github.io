import fileinput

episode_number = raw_input("Enter episode number: ")
page_title = raw_input("Enter a title for the page: ")
page_description = raw_input("Enter a description for the page: ")
show_draft_ad = raw_input("Show DRAFT promo code ad? (Y/N): ")
page_image = raw_input("Enter an image for the page: ")
pod_url = raw_input("Add a url for the cast: ")
pod_length = raw_input("Length of pod (in minutes): ")
daydict = {
        "monday":{"show_notes":["Grammar School", "Weekend Review", "Week Preview and Pickup Suggestions", "Picks of the Night"], "titles":["Grammar School", "Weekend's Best Players", "Weekend's Worst Players", "Long Term Pickup Suggestions", "Potentially Returning From Injury", "Players to Consider This Week", "Our Top Picks of the Night", "Our Value Picks of the Night"]},
        "tuesday":{"show_notes":["Injury News", "Injury Replacements/Buy Low Candidates", "Picks of the Night"], "titles":["New Injuries", "Returning From Injury", "Injury Replacements", "Buy Low Injury Related Players", "Our Top Picks of the Night", "Our Value Picks of the Night"]},
        "wednesday":{"show_notes":["Unsustainable Segment", "Picks of the Night"], "titles":["Last Week's Unsustainably High Picks", "Last Week's Unsustainably Low Picks", "Last Week's Sustainably High Picks", "Last Week's Sustainably Low Picks (Trade or Drop Options)", "Unsustainably High Picks", "Unsustainably Low Picks", "Sustainably High Picks", "Sustainably Low Picks (Trade or Drop Options)", "Our Top Picks of the Night", "Our Value Picks of the Night"]},
        "thursday":{"show_notes":["NHL News", "Picks of the Night"], "titles":["Players in the News", "Our Top Picks of the Night", "Our Value Picks of the Night"]},
        "friday":{"show_notes":["Week in Review", "Weekend Pickup Suggestions", "Picks of the Night"], "titles":["Best Players of the Week", "Worst Players of the Week", "Weekend Pickup Suggestions", "Our Top Picks of the Night", "Our Value Picks of the Night"]},
        "saturday":{"show_notes":["Game Previews", "Goalie Ranking", "Sit/Start Picks"], "titles":["Top Goalies", "Start Picks", "Sit Picks"]}
        }
draft_ad = ""
if show_draft_ad.upper() == "Y":
    draft_ad = "<br><br>Download the DRAFT app on iOS or Android or visit <a href=\"https://draft.com/FHP\" target=\"_blank\">draft.com</a> and use promo code 'FHP' when you sign up for a $3 ticket on your first deposit AND a $100 satisfaction guarantee."
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
    time = raw_input("Enter a time for note " + note + ": ")
    if show_notes == "":
        show_notes = "\n    "
    else:
        show_notes += "\n    <br>"
    show_notes += note + " - " + time

html = """<!doctype html>
<html>
<head>
    <meta charset=\"utf-8\">
    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">
    <meta name=\"Fantasy Hockey Podcast\" content=\"\">
    <meta name=\"keywords\" content=\"Hockey, Fantasy, Podast, David Gamboa, NHL, Stanley Cup Playoffs, Playoffs, advice, help, drop, trade, add, waiver wire, Fantasy Hockey Pod, daily, season long, espn, yahoo, sell high, buy low, candidates, best\">
    <meta name=\"author\" content=\"Fantasy Hockey Podcast\">
    <meta name=\"description\" content=""" + "\"" + page_description + """\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <meta name=\"title\" content=\"Fantasy Hockey Podcast | Episode """ + episode_number + """ - """ + page_title + """\">
    <meta name=\"image\" content=""" + "\"" + page_image + """\">
    <title> Fantasy Hockey Podcast | Episode """ + episode_number + """ - """ + page_title + """</title>
    <!---- FB OPEN GRAPH ---->
    <meta property=\"og:type\"               content=\"article\" />
    <meta property=\"og:description\"        content=""" + "\"" + page_description + """\">
    <meta property=\"og:image\"              content=""" + "\"" + page_image + """\"/>
    <!-- Disable tap highlight on IE -->
    <meta name=\"msapplication-tap-highlight\" content=\"no\">


    <!-- Add to homescreen for Chrome on Android -->
    <meta name=\"mobile-web-app-capable\" content=\"yes\">
    <meta name=\"Hockey On Stats\" content=\"\">
    <link rel=\"icon\" sizes=\"192x192\" href=\"images/Artboard%206.png\">

    <!-- Add to homescreen for Safari on iOS -->
    <meta name=\"Fantasy Hockey Podcast\" content=\"\">
    <meta name=\"Fantasy Hockey Podcast\" content=\"\">
    <meta name=\"Fantasy Hockey Podcast\" content=\"\">
    <link rel=\"apple-touch-icon\" href=\"images/Artboard%206.png\">

    <!-- Tile icon for Win8 (144x144 + tile color) -->
    <meta name=\"msapplication-TileImage\" content=\"images/artboard%206\">
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
            <div  class=\"mdl-layout__header-row mdl-shadow--4dp\">
                <!-- Title -->
                <span class=\"mdl-layout-title\">""" + page_title + """</span>
      <!-- Add spacer, to align navigation to the right -->
      <div class=\"mdl-layout-spacer\"></div>
      <!-- Navigation. We hide it in small screens. -->
    </div>
  </header>
    
    
<!-- DRAWER -->    
    
    
  <div class=\"mdl-layout__drawer\">
    <span class=\"mdl-layout-title\">FHP</span>
    <nav class=\"mdl-navigation\">
        <!--
      <a class=\"mdl-navigation__link\" href=\"\">Interactives</a>
      <a class=\"mdl-navigation__link\" href=\"\">Long Reads</a>
      <a class=\"mdl-navigation__link\" href=\"\">Short Reads</a>
      <a class=\"mdl-navigation__link\" href=\"\">About</a>

-->
    <a class=\"mdl-navigation__link\" href=\"/index.html\">Home</a>
      <a class=\"mdl-navigation__link\" href=\"https://twitter.com/fntasyhockeypod\">Twitter</a>
        <!--
      <a class=\"mdl-navigation__link\" href=\"https://www.facebook.com/hockeyonstats/\">Facebook</a>-->
    <a class=\"mdl-navigation__link\" href=\"about.html\">About</a>
        <a class=\"mdl-navigation__link\" href=\"mailto:fantasyhockeypodcast@gmail.com?Subject=Inquiry\">Contact</a>
        
        <br>
        <!-----BADGES--->
        
         <!----itunes---->
         <a href=\"https://itunes.apple.com/us/podcast/fantasy-hockey-podcast/id1198704323\">
                <img src=\"http://matepodcast.com/wp-content/uploads/2016/05/get-it-on-itunes-badge-440x160.png\" width='70%' style=\"padding-left:10%\"> </a> 
        
        <!-----GPLAY---->
            <a href=\"https://goo.gl/app/playmusic?ibi=com.google.PlayMusic&isi=691797987&ius=googleplaymusic&link=https://play.google.com/music/m/Igp5eo4jiymytfxf3uyffggtbyq?t%3DFantasy_Hockey_Podcast%26pcampaignid%3DMKT-na-all-co-pr-mu-pod-16\">
                      <img src=\"https://play.google.com/intl/en_us/badges-music/images/badges/en_badge_web_music.png\" width='70%' style=\"padding-left:10%\"></a>
                  <br>
         <!--- STITCHER---->
             <a href=\"http://www.stitcher.com/podcast/fantasy-hockey-podcast\">
                      <img src=\"https://wordpress.todaytix.com/wp-content/uploads/2016/10/stitcher-badge.jpg\" width='70%' style=\"padding-left:10%\"> </a>
    </nav>
  </div>

      
    
  <main  style=\"background:white;\" class=\"mdl-layout__content\">
      
      
      
    <div class=\"page-content\">
        <img style=\"width:100%; opacity:.8;\" src=""" + "\"" + page_image + """\">
        <div class=\"container mdl-grid\">
        <div class=\"mdl-cell mdl-cell--2-col mdl-cell--hide-tablet mdl-cell--hide-phone\"></div>
        <div  class=\"content mdl-color--white mdl-shadow--4dp content mdl-color-text--grey-800 mdl-cell mdl-cell--8-col\">
        <div class=\"opener\">
        
        <p style=\"font-style:italic;opacity:.5;\">Episode """ + episode_number + """ - """ + page_title + """</p>

        <p> 
            <audio controls style=\"width:70%;opacity:1;\">
            <source src=""" + "\"" + pod_url + """\" type=\"audio/mpeg\">
                Your browser does not support the audio element.
            </audio> 
        </p>
        
        <!----ITUNES--->
        <a href=\"https://itunes.apple.com/us/podcast/fantasy-hockey-podcast/id1198704323\">
        <img src=\"http://matepodcast.com/wp-content/uploads/2016/05/get-it-on-itunes-badge-440x160.png\" width='20%'></a> 
                  
        <!-----GOOGLE PLAY---->
        <a href=\"https://goo.gl/app/playmusic?ibi=com.google.PlayMusic&isi=691797987&ius=googleplaymusic&link=https://play.google.com/music/m/Igp5eo4jiymytfxf3uyffggtbyq?t%3DFantasy_Hockey_Podcast%26pcampaignid%3DMKT-na-all-co-pr-mu-pod-16\">
        <img src=\"https://play.google.com/intl/en_us/badges-music/images/badges/en_badge_web_music.png\" width='20%'></a>
             
        </div>    
        <div class=\"ellipses\"><iron-icon  icon=\"filter-list\" stylue></iron-icon></div>
        
        <div class=\"interlude fb\">
            <div style=\"padding-bottom:px;\" class=\"fb-like\" data-href=\"http://fantasyhockeypodcast.com\" data-layout=\"button_count\" data-action=\"like\" data-show-faces=\"true\" data-share=\"false\"></div>
        <div class=\"article-content\">
        
        <!------ ARTICLE BEGINS -----> 
        
        <p class=\"interlude\">
            Summary
        </p>

        <p class=\"main-paragraphs\"><text class=\"first-letter\">""" + page_description[0] + """</text>""" + page_description[1:] + draft_ad + """</p>
        <p class=\"interlude\">
            Show Notes
        </p>

        <p class=\"main-paragraphs notes\">
        """ + show_notes + """
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
        <li class=\"mdl-menu__item\"><div style=\"margin-left:53%;margin-top:10%;\"><a href=\"https://twitter.com/share\" class=\"twitter-share-button\" data-via=\"fntasyhockeypod\" data-related=\"Daveedgamboa\">Tweet</a>
        <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script></div></li>
    </ul>
    </div>
</div>
    <!-- build:js(app/) ../../scripts/main.min.js -->
    <script src=\"scripts/main.js\"></script>
    <!-- endbuild -->
      
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
    "Zdeno Chara": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/145./png&w=350&h=254",
    "Julius Honka": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3114754.png&w=350&h=254",
    "James Neal": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3227.png&w=350&h=254",
    "Brock Boeser": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3899979.png&w=350&h=254",
    "Vadim Shipachyov": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Vadim_Shipachev_May_4%2C_2014.jpg/230px-Vadim_Shipachev_May_4%2C_2014.jpg",
    "Evgeny Dadonov": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/4969.png&w=350&h=254",
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
                """ + page_description + draft_ad + """
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
                <a href=""" + "\"" + episode_filename + """\" class=\"mdl-button mdl-color-text--black mdl-js--ripple\">Read more</a>
                 <i style=\"vertical-align:middle;opacity:.7;\" class=\"material-icons\">schedule</i>
                  <text style=\"font-size:.8em;opacity:.6\"> """ + pod_length + """ min.</text>
                
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
