episode_number = raw_input("Enter episode number: ")
page_title = raw_input("Enter a title for the page: ")
page_description = raw_input("Enter a description for the page: ")
page_image = raw_input("Enter an image for the page: ")
pod_url = raw_input("Add a url for the cast: ")
show_notes = ""
while True:
    note = raw_input("Enter a show note (ie: Grammar School - 1:00) or leave empty to complete show notes: ")
    if not note:
        break
    show_notes += "\n<br>" + note

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

        <p class=\"main-paragraphs\"><text class=\"first-letter\">""" + page_description[0] + """</text>""" + page_description[1:] + """</p>
        <p class=\"interlude\">
            Show Notes
        </p>

        <p class=\"main-paragraphs notes\">
        """ + show_notes + """
        </p>
        <br>
        <br>

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
        "Cory Schneider": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3750.png&w=350&h=254",
        "Kris Letang": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3539.png&w=350&h=254",
        "Nikita Zaitsev": "http://www.hockeydb.com/ihdb/photos/nikita-zaitsev-2017-38.jpg",
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
        "Taylor Hall": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/5428.png",
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
        "Loui Eriksson": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3161.png",
        "Thomas Vanek": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/3045.png&w=350&h=254",
        "Jake Guentzel": "https://nhl.bamcontent.com/images/headshots/current/168x168/8477404.jpg",
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
        "Patrick Sharp": "http://a.espncdn.com/combiner/i?img=/i/headshots/nhl/players/full/2002.png",
        }

daydict = {
        "monday":["Grammar School", "Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "Players to Consider This Week", "Our Top Picks of the Night", "Our Value Picks of the Night"], 
        "tuesday":["Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "New Injuries", "Returning From Injury", "Injury Replacements", "Buy Low Injury Related Players", "Our Top Picks of the Night", "Our Value Picks of the Night"],
        "wednesday":["Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "Unsustainably High Picks", "Unsustainably Low Picks", "Our Top Picks of the Night", "Our Value Picks of the Night"],
        "thursday":["Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "Players in the News", "Our Top Picks of the Night", "Our Value Picks of the Night"],
        "friday":["Our Top Picks of Last Podcast", "Our Value Picks of Last Podcast", "Best Players of the Week", "Worst Players of the Week", "Weekend Pickup Suggestions", "Our Top Picks of the Night", "Our Value Picks of the Night"]
        }

podcast_type = raw_input("Enter a podcast type (monday, tuesday, etc) or leave blank for custom: ").lower()
new_player_images = {}
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
        else:
            image = raw_input("Add image for " + player + ": ")
            new_player_images[player] = image
        html += "    <div class=\"tooltip\">\n        <img class=\"img-circle\" style=\"height:5em;\" src=\"" + image + "\">\n        <br>\n        <span class=\"tooltiptext\">" + player + "</span>\n    </div>\n"
    html += "</div>\n\n"
    print "Completed section " + title + "\n"

html += html_close
html_file = open("../ep-"+episode_number+".html", "w")
html_file.write(html)
html_file.close()

if len(new_player_images) > 0:
    print "\n\nAdd the following players and images to the database:\n\n" 
    for player, image in new_player_images.iteritems():
        print "\"" + player + "\": \"" + image + "\","
raw_input()
