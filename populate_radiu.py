import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'radiu_webapp.settings')

import django
django.setup()
from radiu.models import Artist, Song, UserProfile, Comment, Like
from django.contrib.auth.models import User
from random import randint

def populate():

    ratm_songs = [
        {"title": "Killing In The Name",
         "url": "https://www.youtube.com/watch?v=bWXazVhlyxQ",
         "genre": "Metal"},
        {"title": "Testify",
         "url": "https://www.youtube.com/watch?v=Q3dvbM6Pias",
         "genre": "Metal"},
        {"title": "Sleep Now In The Fire",
         "url": "https://www.youtube.com/watch?v=w211KOQ5BMI",
         "genre": "Metal"},
        {"title": "Bulls On Parade",
         "url": "https://www.youtube.com/watch?v=3L4YrGaR8E4",
         "genre": "Metal"},
        {"title": "No Shelter",
         "url": "https://www.youtube.com/watch?v=6NEoesmnYU4",
         "genre": "Metal"} ]

    megadeth_songs = [
        {"title": "Holy Wars",
         "url": "https://www.youtube.com/watch?v=hcjN5BNU9CY",
         "genre": "Metal"},
        {"title": "Hangar 18",
         "url": "https://www.youtube.com/watch?v=4iCn1BVBiTM",
         "genre": "Metal"},
        {"title": "Tornado Of Souls",
         "url": "https://www.youtube.com/watch?v=44iFZzV6y_o",
         "genre": "Metal"},
        {"title": "Peace Sells",
         "url": "https://www.youtube.com/watch?v=Z8Q4Z04076M",
         "genre": "Metal"},
        {"title": "Wake Up Dead",
         "url": "https://www.youtube.com/watch?v=bN-0_ErU-wU",
         "genre": "Metal"} ]

    metallica_songs = [
        {"title": "Ride The Lightning",
         "url": "https://www.youtube.com/watch?v=Zysx9U2uKOk",
         "genre": "Metal"},
        {"title": "Master Of Puppets",
         "url": "https://www.youtube.com/watch?v=lPjP0jbxBXw",
         "genre": "Metal"},
        {"title": "And Justice For All...",
         "url": "https://www.youtube.com/watch?v=qaOMT_dyxAM",
         "genre": "Metal"},
        {"title": "Blackened",
         "url": "https://www.youtube.com/watch?v=DU_ggFovJNo",
         "genre": "Metal"},
        {"title": "Battery",
         "url": "https://www.youtube.com/watch?v=md3B3I7Nmvw",
         "genre": "Metal"} ]

    vanhalen_songs = [
        {"title": "Hot For Teacher",
         "url": "https://www.youtube.com/watch?v=6M4_Ommfvv0",
         "genre": "Rock"},
        {"title": "Unchained",
         "url": "https://www.youtube.com/watch?v=xx86CxKYtg0",
         "genre": "Rock"},
        {"title": "Mean Street",
         "url": "https://www.youtube.com/watch?v=U2R2KXNQR1M",
         "genre": "Rock"},
        {"title": "In N' Out",
         "url": "https://www.youtube.com/watch?v=tIILCKeLtuM",
         "genre": "Rock"},
        {"title": "Runaround",
         "url": "https://www.youtube.com/watch?v=XSDYCGIXxvI",
         "genre": "Rock"} ]

    ledzepp_songs = [
        {"title": "When The Levee Breaks",
         "url": "https://www.youtube.com/watch?v=b97hqSDRspw",
         "genre": "Rock"},
        {"title": "Kashmir",
         "url": "https://www.youtube.com/watch?v=3W6mDUmPZ0Y",
         "genre": "Rock"},
        {"title": "Stairway To Heaven",
         "url": "https://www.youtube.com/watch?v=D9ioyEvdggk",
         "genre": "Rock"},
        {"title": "Rock N' Roll",
         "url": "https://www.youtube.com/watch?v=4bv_ALKkTjQ",
         "genre": "Rock"},
        {"title": "The Battle Of Evermore",
         "url": "https://www.youtube.com/watch?v=7_3yDImIQYU",
         "genre": "Rock"} ]

    glenngould_songs = [
        {"title": "Turkish March",
         "url": "https://www.youtube.com/watch?v=eTZ33EVK3Ug",
         "genre": "Classical"},
        {"title": "32 Variations In C Minor",
         "url": "https://www.youtube.com/watch?v=bVrUaiL2gz8",
         "genre": "Classical"},
        {"title": "Piano Sonata No. 23 In F Minor",
         "url": "https://www.youtube.com/watch?v=0KaThPVPj-c",
         "genre": "Classical"},
        {"title": "Symphony No. 7 - Allegretto",
         "url": "https://www.youtube.com/watch?v=AnS1i9bVGHU",
         "genre": "Classical"},
        {"title": "Concerto No. 1 In D Minor",
         "url": "https://www.youtube.com/watch?v=ljLi9A0H8H4",
         "genre": "Classical"} ]

    reignofkindo_songs = [
        {"title": "Nightingale",
         "url": "https://www.youtube.com/watch?v=LkcZdhamaew",
         "genre": "Rock"},
        {"title": "Romancing A Stranger",
         "url": "https://www.youtube.com/watch?v=6rVEy0zDh6E",
         "genre": "Rock"},
        {"title": "Dust",
         "url": "https://www.youtube.com/watch?v=FRxt1tX-8VE",
         "genre": "Rock"},
        {"title": "Hold Out",
         "url": "https://www.youtube.com/watch?v=BD9IT9a63RM",
         "genre": "Rock"},
        {"title": "October's Storm",
         "url": "https://www.youtube.com/watch?v=wHAik4Z07M0",
         "genre": "Rock"} ]

    johncoltrane_songs = [
        {"title": "Equinox",
         "url": "https://www.youtube.com/watch?v=5m2HN2y0yV8",
         "genre": "Jazz"},
        {"title": "Blue Train",
         "url": "https://www.youtube.com/watch?v=XpZHUVjQydI",
         "genre": "Jazz"},
        {"title": "I'm Old Fashioned",
         "url": "https://www.youtube.com/watch?v=HNnM2iRwHLE",
         "genre": "Jazz"},
        {"title": "In A Sentimental Mood",
         "url": "https://www.youtube.com/watch?v=r594pxUjcz4",
         "genre": "Jazz"},
        {"title": "Body And Soul",
         "url": "https://www.youtube.com/watch?v=8z-dDWrIKDQ",
         "genre": "Jazz"} ]

    charlesmingus_songs = [
        {"title": "Moanin'",
         "url": "https://www.youtube.com/watch?v=__OSyznVDOY",
         "genre": "Jazz"},
        {"title": "Goodbye Pork Pie Hat",
         "url": "https://www.youtube.com/watch?v=sxz9eZ1Aons",
         "genre": "Jazz"},
        {"title": "Work Song",
         "url": "https://www.youtube.com/watch?v=heVcGt7qWns",
         "genre": "Jazz"},
        {"title": "Duke Ellington's Sound Of Love",
         "url": "https://www.youtube.com/watch?v=xaFNHjqqWnc",
         "genre": "Jazz"},
        {"title": "Septemberly",
         "url": "https://www.youtube.com/watch?v=d7FdnCHtLys",
         "genre": "Jazz"} ]

    frankturner_songs = [
        {"title": "I Still Believe",
         "url": "https://www.youtube.com/watch?v=sZ-D4jmkUiQ",
         "genre": "Rock"},
        {"title": "The Way I Tend To Be",
         "url": "https://www.youtube.com/watch?v=Cf5O2M5GaEA",
         "genre": "Rock"},
        {"title": "Love Ire And Song",
         "url": "https://www.youtube.com/watch?v=YaLmmE2hVI4",
         "genre": "Rock"},
        {"title": "Long Live The Queen",
         "url": "https://www.youtube.com/watch?v=_RbNdwY4ujw",
         "genre": "Rock"},
        {"title": "Peggy Sang The Blues",
         "url": "https://www.youtube.com/watch?v=KUl_yKRXlNE",
         "genre": "Rock"} ]

    khalid_songs = [
        {"title": "Love Lies",
        "url": "https://www.youtube.com/watch?v=xYtsL9znopI",
        "genre": "R&B"},
        {"title": "Young Dumb & Broke",
        "url": "https://www.youtube.com/watch?v=IPfJnp1guPc",
        "genre": "R&B"},
        {"title": "Location",
        "url": "https://www.youtube.com/watch?v=by3yRdlQvzs",
        "genre": "R&B"},
        {"title": "Saved",
        "url": "https://www.youtube.com/watch?v=Dyg32hMf7Fk",
        "genre": "R&B"},
        {"title":"American Teen",
        "url":"https://www.youtube.com/watch?v=0NChtZCDCsY",
        "genre": "R&B"} ]

    postmalone_songs = [
        {"title": "Rockstar",
        "url": "https://www.youtube.com/watch?v=UceaB4D0jpo",
        "genre": "Hip-hop"},
        {"title": "Congratulations",
        "url": "https://www.youtube.com/watch?v=SC4xMk98Pdc",
        "genre": "Hip-hop"},
        {"title": "White Iverson",
        "url": "https://www.youtube.com/watch?v=SLsTskih7_I",
        "genre": "Hip-hop"},
        {"title": "I Fall Apart",
        "url": "https://www.youtube.com/watch?v=7a66clRobKI",
        "genre": "R&B"},
        {"title": "Go Flex",
        "url": "https://www.youtube.com/watch?v=tQjsAJhsSw8",
        "genre": "Hip-hop"} ]

    imaginedragons_songs = [
        {"title": "Thunder",
        "url": "https://www.youtube.com/watch?v=fKopy74weus",
        "genre": "Rock"},
        {"title": "Believer",
        "url": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
        "genre": "Rock"},
        {"title": "Whatever It Takes",
        "url": "https://www.youtube.com/watch?v=gOsM-DYAEhY",
        "genre": "Rock"},
        {"title": "Radioactive",
        "url": "https://www.youtube.com/watch?v=ktvTqknDobU",
        "genre": "Rock"},
        {"title": "Demons",
        "url": "https://www.youtube.com/watch?v=mWRsgZuwf_8",
        "genre": "Rock"} ]

    kendricklamar_songs = [
        {"title": "Humble",
        "url": "https://www.youtube.com/watch?v=tvTRZJ-4EyI",
        "genre": "Hip-hop"},
        {"title": "Love",
        "url": "https://www.youtube.com/watch?v=ox7RsX1Ee34",
        "genre": "Hip-hop"},
        {"title": "DNA",
        "url": "https://www.youtube.com/watch?v=NLZRYQMLDW4",
        "genre": "Hip-hop"},
        {"title": "I",
        "url": "https://www.youtube.com/watch?v=8aShfolR6w8",
        "genre": "Hip-hop"},
        {"title": "Loyalty",
        "url": "https://www.youtube.com/watch?v=Dlh-dzB2U4Y",
        "genre": "Hip-hop"} ]

    porterrobinson_songs = [
        {"title": "Shelter",
        "url": "https://www.youtube.com/watch?v=fzQ6gRAEoy0",
        "genre": "Electronic"},
        {"title": "Sad Machine",
        "url": "https://www.youtube.com/watch?v=HAIDqt2aUek",
        "genre": "Electronic"},
        {"title": "Goodbye To A World",
        "url": "https://www.youtube.com/watch?v=W2TE0DjdNqI",
        "genre": "Electronic"},
        {"title": "Sea Of Voices",
        "url": "https://www.youtube.com/watch?v=lSooYPG-5Rg",
        "genre": "Electronic"},
        {"title": "Lionhearted",
        "url": "https://www.youtube.com/watch?v=hgKDu5pp_fU",
        "genre": "Electronic"} ]

    pantera_songs = [
        {"title": "Walk",
         "url": "https://www.youtube.com/watch?v=AkFqg5wAuFk",
         "genre": "Metal"},
        {"title": "Cowboys From Hell",
         "url": "https://www.youtube.com/watch?v=i97OkCXwotE",
         "genre": "Metal"},
        {"title": "I'm Broken",
         "url": "https://www.youtube.com/watch?v=2-V8kYT1pvE",
         "genre": "Metal"},
        {"title": "Cemetery Gates",
         "url": "https://www.youtube.com/watch?v=RVMvART9kb8",
         "genre": "Metal"},
        {"title": "5 Minutes Alone",
         "url": "https://www.youtube.com/watch?v=7m7njvwB-Ks",
         "genre": "Metal"} ]

    rammstein_songs = [
        {"title": "Keine Lust",
         "url": "https://www.youtube.com/watch?v=1M4ADcMn3dA",
         "genre": "Metal"},
        {"title": "Mein Teil",
         "url": "https://www.youtube.com/watch?v=PBvwcH4XX6U",
         "genre": "Metal"},
        {"title": "Ich Tu Dir Weh",
         "url": "https://www.youtube.com/watch?v=IxuEtL7gxoM",
         "genre": "Metal"},
        {"title": "Haifisch",
         "url": "https://www.youtube.com/watch?v=GukNjYQZW8s",
         "genre": "Metal"},
        {"title": "Mein Land",
         "url": "https://www.youtube.com/watch?v=6iaxDxHUWP8",
         "genre": "Metal"} ]

    martyfriedman_songs = [
        {"title": "Undertow",
         "url": "https://www.youtube.com/watch?v=9LidVKHqC4c",
         "genre": "Instrumental"},
        {"title": "Inferno",
         "url": "https://www.youtube.com/watch?v=hFdP5uFNocs",
         "genre": "Instrumental"},
        {"title": "Amagigoe",
         "url": "https://www.youtube.com/watch?v=wJ05aMzcP7I",
         "genre": "Instrumental"},
        {"title": "Tears Of An Angel",
         "url": "https://www.youtube.com/watch?v=0DIDSsnshl4",
         "genre": "Instrumental"},
        {"title": "Devil Take Tomorrow",
         "url": "https://www.youtube.com/watch?v=9-QQwN5nHr8",
         "genre": "Instrumental"} ]

    acdc_songs = [
        {"title": "Thunderstruck",
         "url": "https://www.youtube.com/watch?v=v2AC41dglnM",
         "genre": "Rock"},
        {"title": "Back In Black",
         "url": "https://www.youtube.com/watch?v=pAgnJDJN4VA",
         "genre": "Rock"},
        {"title": "Hells Bells",
         "url": "https://www.youtube.com/watch?v=etAIpkdhU9Q",
         "genre": "Rock"},
        {"title": "Highway To Hell",
         "url": "https://www.youtube.com/watch?v=l482T0yNkeo",
         "genre": "Rock"},
        {"title": "Rock And Roll Ain't Noise Pollution",
         "url": "https://www.youtube.com/watch?v=X_IWlPHMziU",
         "genre": "Rock"} ]

    gunsnroses_songs = [
        {"title": "Welcome To The Jungle",
         "url": "https://www.youtube.com/watch?v=o1tj2zJ2Wvg",
         "genre": "Rock"},
        {"title": "Sweet Child O' Mine",
         "url": "https://www.youtube.com/watch?v=1w7OgIMMRc4",
         "genre": "Rock"},
        {"title": "Paradise City",
         "url": "https://www.youtube.com/watch?v=Rbm6GXllBiw",
         "genre": "Rock"},
        {"title": "You Could Be Mine",
         "url": "https://www.youtube.com/watch?v=_U5IhEAFGwQ",
         "genre": "Rock"},
        {"title": "November Rain",
         "url": "https://www.youtube.com/watch?v=8SbUC-UaAxE",
         "genre": "Rock"} ]

    artists = {"Rage Against The Machine": {"songs": ratm_songs,
                "description": """Rage Against the Machine is an American rap metal band from Los Angeles, California.
                                  Formed in 1991, the group consists of vocalist Zack de la Rocha, bassist and backing vocalist Tim Commerford, guitarist Tom Morello, and drummer Brad Wilk.
                                  Rage Against the Machine is well known for the members' revolutionary political views, which are expressed in many of the band's songs.
                                  As of 2010, they had sold over 16 million records worldwide.
                                  In 2017, they were nominated for induction into the Rock & Roll Hall of Fame in their first year of eligibility."""},
            "Metallica": {"songs": metallica_songs,
                "description": """Metallica is an American heavy metal band from Los Angeles, California.
                                  The band was formed in 1981 by drummer Lars Ulrich and vocalist/guitarist James Hetfield.
                                  The band's fast tempos, instrumentals and aggressive musicianship made them one of the founding "big four" bands of thrash metal, alongside Megadeth, Anthrax and Slayer.
                                  Metallica's current lineup comprises founding members Hetfield and Ulrich, longtime lead guitarist Kirk Hammett and bassist Robert Trujillo.
                                  Metallica ranks as one of the most commercially successful bands of all time, having sold over 120 million records worldwide as of 2014.
                                  In 2009, Metallica was inducted into the Rock and Roll Hall of Fame.
                                  """},
            "Megadeth": {"songs": megadeth_songs,
                "description": """Megadeth is an American heavy metal band from Los Angeles, California.
                                  Guitarist Dave Mustaine and bassist David Ellefson formed the band in 1983 shortly after Mustaine's dismissal from Metallica.
                                  A pioneer of the American thrash metal scene, Megadeth is credited as one of the genre's "big four," along with Metallica, Anthrax, and Slayer, responsible for thrash metal's development and popularization.
                                  Megadeth plays in a technical style, featuring complex arrangements and fast rhythm sections.
                                  Themes of death, war, politics, and religion are prominent in the song lyrics.
                                  Megadeth has sold over 38 million records worldwide, earned platinum certification in the United States for five of its fifteen studio albums, and received twelve Grammy nominations."""},
            "Van Halen": {"songs": vanhalen_songs,
                "description": """Van Halen is an American hard rock band formed in Pasadena, California, in 1972.
                                  From 1974 until 1985, the band consisted of guitarist Eddie Van Halen, vocalist David Lee Roth, drummer Alex Van Halen, and bassist Michael Anthony.
                                  The band went on to become major stars, and by the early 1980s they were one of the most successful rock acts of all time.
                                  Van Halen achieved worldwide fame for their many popular songs and larger-than-life stage performances.
                                  Van Halen charted the most number-one hits in the history of Billboard's Mainstream Rock chart and they are one of the world's best-selling bands of all time, having sold more than 80 million records.
                                  In 2007, Van Halen was inducted into the Rock and Roll Hall of Fame."""},
            "Led Zeppelin": {"songs": ledzepp_songs,
                "description": """Led Zeppelin were an English rock band formed in London in 1968.
                                  The group consisted of guitarist Jimmy Page, singer Robert Plant, bassist and keyboardist John Paul Jones, and drummer John Bonham.
                                  The band's heavy, guitar-driven sound has led them to be cited as one of the progenitors of hard rock.
                                  Their style drew from a wide variety of influences, including blues, psychedelia, and folk music.
                                  Led Zeppelin are widely considered one of the most successful, innovative, and influential rock groups in history.
                                  They are one of the best-selling music artists in the history of audio recording; various sources estimate the group's record sales at 200 to 300 million units worldwide.
                                  They were inducted into the Rock and Roll Hall of Fame in 1995."""},
            "Glenn Gould": {"songs": glenngould_songs,
                "description": """Glenn Herbert Gould was a Canadian pianist who became one of the best-known and celebrated classical pianists of the 20th century.
                                  He was renowned as an interpreter of the keyboard works of Johann Sebastian Bach.
                                  His playing was distinguished by remarkable technical proficiency and capacity to articulate the polyphonic texture of Bach's music.
                                  Gould rejected most of the standard Romantic piano literature by Chopin, Liszt, and others, in favor of Baroque, Renaissance, late Romantic, and modernist composers.
                                  Gould was also a writer, broadcaster, and conductor. He was a prolific contributor to musical journals, in which he discussed music theory and outlined his musical philosophy."""},
            "Reign Of Kindo": {"songs": reignofkindo_songs,
                "description": """Reign of Kindo is a rock band originating from Buffalo, New York, currently based out of New York City.
                                  According to the band's Facebook page, the members describe themselves simply as, "makers of music".
                                  Though most easily labeled as a branch of Indie Rock, their style is altogether jazzier than most in the genre, mixing complex jazz harmonies and dissonances with a Pop music and Latin influence."""},
            "John Coltrane": {"songs": johncoltrane_songs,
                "description": """John William Coltrane was an American jazz saxophonist and composer.
                                  Working in the bebop and hard bop idioms early in his career, Coltrane helped pioneer the use of modes in jazz and was later at the forefront of free jazz.
                                  He led at least fifty recording sessions during his career, and appeared as a sideman on many albums by other musicians, including trumpeter Miles Davis and pianist Thelonious Monk.
                                  As his career progressed, Coltrane and his music took on an increasingly spiritual dimension.
                                  Coltrane influenced innumerable musicians, and remains one of the most significant saxophonists in music history."""},
            "Charles Mingus": {"songs": charlesmingus_songs,
                "description": """Charles Mingus was an American jazz double bassist, pianist, composer and bandleader.
                                  His compositions retained the hot and soulful feel of hard bop, drawing heavily from black gospel music and blues, while sometimes containing elements of Third Stream, free jazz, and classical music.
                                  Mingus espoused collective improvisation, similar to the old New Orleans jazz parades, paying particular attention to how each band member interacted with the group as a whole.
                                  As a performer, Mingus was a pioneer in double bass technique, widely recognized as one of the instrument's most proficient players."""},
            "Frank Turner": {"songs": frankturner_songs,
                "description": """Francis Edward "Frank" Turner is an English folk singer-songwriter from Meonstoke, Hampshire.
                                  He began his career as the vocalist of post-hardcore band Million Dead, then embarked upon a primarily acoustic-based solo career following the band's split in 2005.
                                  In the studio and during live performances, Turner is accompanied by his backing band, The Sleeping Slugs.
                                  To date, Turner has released six solo albums, three compilation albums, one split album and five EPs."""},
            "Khalid": {"songs": khalid_songs,
                "description": """Khalid Donnel Robinson, known mononymously as Khalid, is an American singer and songwriter.
                                  His debut single, "Location", was released in July 2016 and peaked at number 16 on the US Billboard Hot 100 chart.
                                  His debut studio album, American Teen, was released on March 3, 2017."""},
            "Post Malone": {"songs": postmalone_songs,
                "description": """Austin Richard Post, known professionally as Post Malone, is an American singer, rapper, songwriter, record producer, and guitarist.
                                  He first gained major recognition in August 2015, after the release of his debut single "White Iverson".
                                  He released his debut studio album Stoney in December 2016 with the single "Congratulations" peaking at number eight on the Billboard Hot 100.
                                  His upcoming album, Beerbongs and Bentleys, is set to be released in 2018."""},
            "Imagine Dragons": {"songs": imaginedragons_songs,
                "description": """Imagine Dragons is an American rock band from Las Vegas, Nevada, consisting of lead vocalist Dan Reynolds, lead guitarist Wayne Sermon, bassist and keyboardist Ben McKee, and drummer Daniel Platzman.
                                  The band first gained exposure with the release of single "It's Time", followed by their award-winning debut studio album Night Visions, which resulted in the chart topping singles "Radioactive" and "Demons".
                                  Imagine Dragons has won three American Music Awards, five Billboard Music Awards, one Grammy Award, and one World Music Award.
                                  In May 2014, the band was nominated for fourteen Billboard Music Awards, including Top Artist of the Year and a Milestone Award, which recognizes innovation and creativity of artists across different genres.
                                  Imagine Dragons have sold 12 million albums and 35 million singles worldwide."""},
            "Kendrick Lamar": {"songs": kendricklamar_songs,
                "description": """Kendrick Lamar Duckworth is an American rapper and songwriter.
                                  Raised in Compton, California, Lamar embarked on his musical career as a teenager under the stage name K-Dot, releasing a mixtape that garnered significant attention.
                                  He began to gain recognition in 2010, after his first retail release, Overly Dedicated.
                                  The following year, he independently released his first studio album, Section.80, which included his debut single, "HiiiPoWeR".
                                  By that time, he had amassed a large online following and collaborated with several prominent artists in the hip hop industry, including The Game, Busta Rhymes, and Snoop Dogg.
                                  Lamar has received a number of accolades over the course of his career, including twelve Grammy Awards."""},
            "Porter Robinson": {"songs": porterrobinson_songs,
                "description": """Porter Weston Robinson is an American DJ, record producer and musician from Chapel Hill, North Carolina.
                                  He has released multiple number one singles across different electronic genres.
                                  His debut full-length studio album, Worlds, was released on August 12, 2014.
                                  In 2017, Robinson began releasing music as Virtual Self, with his self-titled EP Virtual Self released on October 25, 2017."""},
            "Pantera": {"songs": pantera_songs,
                "description": """Pantera was an American heavy metal band from Arlington, Texas.
                                  The group was formed in 1981 by the Abbott brothers – drummer Vinnie Paul and guitarist Dimebag Darrell.
                                  With its fifth album, 1990's Cowboys from Hell, Pantera introduced a groove metal sound.
                                  Its seventh album, 1994's Far Beyond Driven, debuted at number one on the Billboard 200.
                                  The band has sold more than 6 million records as of August 2017."""},
            "Rammstein": {"songs": rammstein_songs,
                "description": """Rammstein is a German metal band, formed in 1994 in Berlin.
                                  Rammstein's six-man lineup consists of lead guitarist Richard Kruspe, bassist Oliver Riedel, drummer Christoph Schneider, lead vocalist Till Lindemann, rhythm guitarist Paul Landers, and keyboardist Christian Lorenz.
                                  The majority of their songs are in German, but they have also performed songs entirely or partially in other languages including English, Spanish, French, and Russian.
                                  Rammstein's award-winning live shows are known for their pyrotechnic elements and both on and off-stage theatrics."""},
            "Marty Friedman": {"songs": martyfriedman_songs,
                "description": """Marty Friedman is an American guitarist, known for his tenure as the lead guitarist for heavy metal band Megadeth which spanned nearly the full decade of the 1990s.
                                  He is also known for playing alongside Jason Becker in Cacophony until 1989, as well as his 12 solo albums and tours.
                                  Friedman is known for his improvisation and for fusing Eastern musical with Western music and other styles, such as neoclassical, thrash metal and later progressive rock.
                                  When playing, he often uses arpeggiated chords and various customized scales and arpeggios, most of which relate to Chinese, Japanese, Middle Eastern and other exotic scales."""},
            "AC/DC": {"songs": acdc_songs,
                "description": """AC/DC are an Australian rock band, formed in Sydney in 1973 by brothers Malcolm and Angus Young.
                                  Although they play a mixture hard rock and blues rock, they refer to themselves as "a rock and roll band, nothing more, nothing less".
                                  AC/DC have sold more than 200 million records worldwide, including 71.5 million albums in the United States, adding them to the list of best-selling music artists of all time.
                                  AC/DC were inducted into the Rock and Roll Hall of Fame on 10 March 2003."""},
            "Guns N' Roses": {"songs": gunsnroses_songs,
                "description": """Guns N' Roses is an American hard rock band from Los Angeles, California, formed in 1985.
                                  The band was formed by vocalist Axl Rose, lead guitarist Slash, rhythm guitarist Izzy Stradlin, bassist Duff McKagan, and drummer Steven Adler.
                                  Guns N' Roses has released six studio albums, accumulating sales of more than 100 million records worldwide, including 45 million in the United States, making them the 41st best-selling artist of all time.
                                  Guns N' Roses' late 1980s and early 1990s years have been described as the period in which the group brought forth a "hedonistic rebelliousness" reminiscent of the early Rolling Stones, a reputation that had earned the group the nickname "the most dangerous band in the world".
                                  The band's classic lineup was inducted into the Rock and Roll Hall of Fame in 2012, its first year of eligibility."""}
            }

    print("Creating Artist and Song objects...")
    for artist, artist_data in artists.items():
        new_artist = add_artist(artist, artist_data["description"])
        for song in artist_data["songs"]:
            add_song(new_artist, song["title"], song["url"], song["genre"])

    for artist in Artist.objects.all():
        for song in Song.objects.filter(artist=artist):
            print("- {0} - {1}".format(str(artist), str(song)))

    users = [
        {"username": "TestUser1",
         "password": "abcdefghij",
         "email": "TestUser1@gmail.com"},
        {"username": "TestUser2",
         "password": "abcdefghij",
         "email": "TestUser2@gmail.com"},
        {"username": "TestUser3",
         "password": "abcdefghij",
         "email": "TestUser3@gmail.com"},
        {"username": "TestUser4",
         "password": "abcdefghij",
         "email": "TestUser4@gmail.com"},
        {"username": "TestUser5",
         "password": "abcdefghij",
         "email": "TestUser5@gmail.com"},
        {"username": "TestUser6",
         "password": "abcdefghij",
         "email": "TestUser6@gmail.com"},
        {"username": "TestUser7",
         "password": "abcdefghij",
         "email": "TestUser7@gmail.com"},
        {"username": "TestUser8",
         "password": "abcdefghij",
         "email": "TestUser8@gmail.com"},
        {"username": "TestUser9",
         "password": "abcdefghij",
         "email": "TestUser9@gmail.com"},
        {"username": "TestUser10",
         "password": "abcdefghij",
         "email": "TestUser10@gmail.com"},
        {"username": "TestUser11",
         "password": "abcdefghij",
         "email": "TestUser11@gmail.com"},
        {"username": "TestUser12",
         "password": "abcdefghij",
         "email": "TestUser12@gmail.com"},
        {"username": "TestUser13",
         "password": "abcdefghij",
         "email": "TestUser13@gmail.com"},
        {"username": "TestUser14",
         "password": "abcdefghij",
         "email": "TestUser14@gmail.com"},
        {"username": "TestUser15",
         "password": "abcdefghij",
         "email": "TestUser15@gmail.com"},
        {"username": "TestUser16",
         "password": "abcdefghij",
         "email": "TestUser16@gmail.com"},
        {"username": "TestUser17",
         "password": "abcdefghij",
         "email": "TestUser17@gmail.com"},
        {"username": "TestUser18",
         "password": "abcdefghij",
         "email": "TestUser18@gmail.com"},
        {"username": "TestUser19",
         "password": "abcdefghij",
         "email": "TestUser19@gmail.com"},
        {"username": "TestUser20",
         "password": "abcdefghij",
         "email": "TestUser20@gmail.com"} ]

    user_profiles = {"TestUser1": {"favourite_song": Song.objects.filter(title="Testify")[0]},
                  "TestUser2": {"favourite_song": Song.objects.filter(title="Holy Wars")[0]},
                  "TestUser3": {"favourite_song": Song.objects.filter(title="And Justice For All...")[0]},
                  "TestUser4": {"favourite_song": Song.objects.filter(title="Hot For Teacher")[0]},
                  "TestUser5": {"favourite_song": Song.objects.filter(title="When The Levee Breaks")[0]},
                  "TestUser6": {"favourite_song": Song.objects.filter(title="Turkish March")[0]},
                  "TestUser7": {"favourite_song": Song.objects.filter(title="Nightingale")[0]},
                  "TestUser8": {"favourite_song": Song.objects.filter(title="Equinox")[0]},
                  "TestUser9": {"favourite_song": Song.objects.filter(title="Work Song")[0]},
                  "TestUser10": {"favourite_song": Song.objects.filter(title="I Still Believe")[0]},
                  "TestUser11": {"favourite_song": Song.objects.filter(title="Love Lies")[0]},
                  "TestUser12": {"favourite_song": Song.objects.filter(title="Rockstar")[0]},
                  "TestUser13": {"favourite_song": Song.objects.filter(title="Thunder")[0]},
                  "TestUser14": {"favourite_song": Song.objects.filter(title="Humble")[0]},
                  "TestUser15": {"favourite_song": Song.objects.filter(title="Shelter")[0]},
                  "TestUser16": {"favourite_song": Song.objects.filter(title="I'm Broken")[0]},
                  "TestUser17": {"favourite_song": Song.objects.filter(title="Keine Lust")[0]},
                  "TestUser18": {"favourite_song": Song.objects.filter(title="Tears Of An Angel")[0]},
                  "TestUser19": {"favourite_song": Song.objects.filter(title="Back In Black")[0]},
                  "TestUser20": {"favourite_song": Song.objects.filter(title="Welcome To The Jungle")[0]}}

    print("Creating dummy users...")
    for userdata in users:
        add_user(userdata["username"], userdata["password"], userdata["email"])

    for user in User.objects.all():
        for username, userdata in user_profiles.items():
            if user.username == username:
                add_user_profile(user, userdata["favourite_song"])

    for user_profile in UserProfile.objects.all():
        print("- {0}".format(str(user_profile)))

    comments = ["boring", "funny", "great", "superb", "horrible", "annoying", "interesting", "amazing", "terrific", "awful"]

    num_songs = Song.objects.all().count()
    num_comments = num_songs // 5
    num_likes = 2 * num_songs // 5

    print("Creating dummy comments and likes...")
    for user in User.objects.all():
        for count in range(num_comments):
            index = randint(0, num_songs - 1)
            song = Song.objects.all()[index]
            index = randint(0, len(comments) - 1)
            text = comments[index]
            add_comment(user, song, text)

    for user in User.objects.all():
        likedsongs_list = []
        for count in range(num_likes):
            while True:
                check = 0
                index = randint(0, num_songs - 1)
                song = Song.objects.all()[index]
                for likedsong in likedsongs_list:
                    if song.title == likedsong:
                        check = 1
                        break
                if check == 0:
                    break
            add_like(user, song)
            likedsongs_list.append(song.title)

def add_song(artist, title, url, genre):
    song = Song.objects.get_or_create(artist=artist, title=title, url=url, genre=genre)[0]
    song.save()
    return song

def add_artist(name, description):
    artist = Artist.objects.get_or_create(name=name, description=description)[0]
    artist.save()
    return artist

def add_user(username, password, email):
    user = User.objects.get_or_create(username=username, password=password, email=email)[0]
    user.save()
    return user

def add_user_profile(user, favourite_song):
    user_profile = UserProfile.objects.get_or_create(user=user, favourite_song=favourite_song)[0]
    user_profile.save()
    return user_profile

def add_comment(user, song, text):
    comment = Comment.objects.get_or_create(user=user, song=song, text=text)[0]
    comment.save()
    return comment

def add_like(user, song):
    like = Like.objects.get_or_create(user=user, song=song)[0]
    like.save()
    return like

if __name__ == '__main__':
    print("Starting Radi-U population script...")
    populate()
