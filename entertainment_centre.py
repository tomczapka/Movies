import fresh_tomatoes
import media

# contructor for each movie
heat = media.Movie("Heat",
                   ("A group of professional bank robbers"
                    " feel the heat from police when they"
                    " unknowingly leave a clue at their"
                    " latest heist."),
                   ("http://www.graffitiwithpunctuation.net/"
                    "wp-content/uploads/2012/07/Heat.jpg"),
                   "https://www.youtube.com/watch?v=0xbBLJ1WGwQ")
american_beauty = media.Movie("American Beauty",
                              ("A sexually frustrated suburban"
                               " father has a mid-life crisis after"
                               " becoming infatuated with his"
                               " daughter's best friend."),
                              ("http://cdn.traileraddict.com/content/"
                               "dreamworks-pictures/americanbeauty.jpg"),
                              "https://www.youtube.com/watch?v=hIq9Zjw0mm8")
night_on_earth = media.Movie("Night on Earth",
                             ("An anthology of 5 different cab drivers"
                              " in 5 American and European cities and"
                              " their remarkable fares on the same "
                              " eventful night."),
                             ("https://upload.wikimedia.org/wikipedia/"
                              "en/thumb/f/f9/Nightonearth.jpg/2"
                              "20px-Nightonearth.jpg"),
                             "https://www.youtube.com/watch?v=F1m6GlPyOSU")
manhattan = media.Movie("Manhattan",
                        ("The life of a divorced television"
                         " writer dating a teenage girl is further"
                         " complicated when he falls in love with his"
                         " best friend's mistress."),
                        ("https://tammytourguide.files.wordpress.com/"
                         "2015/07/manhattan_bridge.jpg"),
                        "https://www.youtube.com/watch?v=Ck0ENY4eawQ")

# creat list with all movies to insert to fresh_tomatoes.py
movies = (heat, american_beauty, night_on_earth, manhattan)
# call "open_movies_page" function of fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies)
