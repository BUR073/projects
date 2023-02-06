
def year(year):
    

    rat = [2020, 2008, 1996, 1984, 1972, 1960, 1948, 1946, 1924]
    ox = [2021, 2009, 1997, 1985, 1973, 1961, 1949, 1937, 1925]
    tiger = [2022, 2010, 1998, 1986, 1974, 1962, 1950, 1938, 1926]
    rabbit = [2023, 2011, 1999, 1987, 1975, 1963, 1951, 1939, 1927]
    dragon = [2024, 2012, 2000, 1988, 1976, 1964, 1952, 1940, 1928]
    snake = [2013, 2001, 1989, 1977, 1965, 1953, 1941, 1929]
    horse = [2014, 2002, 1990, 1978, 1966, 1954, 1942, 1930]
    ram = [2015, 2003, 1991, 1979, 1967, 1955, 1943, 1931]
    monkey = [2016, 2004, 1992, 1980, 1968, 1956, 1944, 1932]
    rooster = [2017, 2005, 1993, 1981, 1969, 1957, 1945, 1933]
    dog = [2018, 2006, 1994, 1982, 1970, 1958, 1946, 1934]
    pig = [2019, 2007, 1995, 1983, 1971, 1959, 1947, 1935]

    if year in rat:
        return('rat')
    elif year in ox:
        return('ox')
    elif year in tiger:
        return('tiger')
    elif year in rabbit:
        return('rabbit')
    elif year in dragon:
        return('dragon')
    elif year in snake:
        return('snake')
    elif year in horse:
        return('horse')
    elif year in ram:
        return('ram')
    elif year in monkey:
        return('monkey')
    elif year in rooster:
        return('rooster')
    elif year in dog:
        return('dog')
    elif year in pig:
        return('pig')


def element(yearNumber):
    lastDigit = list(map(int, str(yearNumber)))
    lastDigit = lastDigit[3]

    if lastDigit < 2:
        return "Metal"
    elif lastDigit < 4:
        return "Water"
    elif lastDigit < 6:
        return 'Wood'
    elif lastDigit < 8:
        return 'Fire'
    else:
        return 'Earth'


yearNumber = int(input('Input your year of birth: '))
year = year(yearNumber)
element = element(yearNumber) 
animalTotal = str(element) + ' ' +  str(year)
print(animalTotal)