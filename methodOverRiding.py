class hotel:
    def day1(self):
        print("13 members")
    def day2(self):
        print("Day2: 15 members")
    def day3(self):
        print("16 members")
class franchise1(hotel):
    def day2(self):
        print("Day2: 18 members")
class franchise2(hotel):
    def day2(self):
        print("Day2: 25 members")

work=franchise1()
work.day1()
work.day2()
work.day3()
work1=franchise2()
work1.day1()
work1.day2()
work1.day3()
