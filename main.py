from college import getUniversityinfo

major = input("What major do you want? ex) computer-science : ")

internationalStudents = input(
    "Are you looking for a university that is good for international students? y or n : ")

price = input("Put minprice and maxprice ex) 0,12000 : ")

if internationalStudents == "y":
    internationalStudents = "goodFor = internationalStudents"
elif internationalStudents == "n":
    internationalStudents = ""


url = f"https://www.niche.com/colleges/search/best-colleges-for-{major}/?{internationalStudents}&netPrice={price}"


starter = getUniversityinfo(url)
starter.start()
