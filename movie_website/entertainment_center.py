import media
import fresh_tomatoes

# Instances
frozen = media.Movie("Frozen",
                     "A story of princess Elsa and princess Anna",
                     "https://upload.wikimedia.org/wikipedia/zh/0/05/Frozen_%282013_film%29_poster.jpg",
                     "http://v.youku.com/v_show/id_XNjYxNDM4Mjc2.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
the_dark_knight_rises = media.Movie("The Dark Knight Rises",
                                    "Batman rises",
                                    "https://upload.wikimedia.org/wikipedia/zh/8/8f/TheDarkKnightRise.png",
                                    "http://v.youku.com/v_show/id_XNDM2NzEwNjcy.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
interstellar = media.Movie("Interstellar",
                           "In the mid-21st century, crop blights and dust storms threaten humanity's survival. Joseph Cooper, a widowed former NASA pilot",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "http://v.youku.com/v_show/id_XNzk1MjIxMzI4.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")
sing = media.Movie("Sing",
                   "In a world of anthropomorphic animals, koala Buster Moon owns a theater, about new Moon theater",
                   "https://upload.wikimedia.org/wikipedia/zh/8/84/Sing-poster.jpg",
                   "http://v.youku.com/v_show/id_XMTc1MjQ2MzgxMg==.html?spm=a2h0k.8191407.0.0&from=s1.8-3-1.1")


movies = [frozen, the_dark_knight_rises, interstellar, sing]
fresh_tomatoes.open_movies_page(movies)

#testing
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__, ", Name: " + media.Movie.__name__, ", Module: " + media.Movie.__module__)