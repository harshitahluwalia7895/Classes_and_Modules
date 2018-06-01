class MovieDetails:
    def __init__(self):
        self.moviename='unnamed movie'
        self.artist='unnamed artist'
        self.year=0
        self.ratings=0.0

    def Display(self):
        print("Movie: {}\nFeaturing Artist: {}\nRelease Year:{}\nRatings: {}\n\n".format(self.moviename,self.artist,self.year,self.ratings))

    def Add(self,moviename,artist,year,ratings):
        self.moviename=moviename
        self.artist=artist
        self.year=year
        self.ratings=ratings

m1=MovieDetails()
m1.Display()
m2=MovieDetails()
m2.Add('Fast and Furious','Vein Diesel',2014,4.9)
m2.Display()