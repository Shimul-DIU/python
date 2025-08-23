class students:
    def info(self,rl,nm='mustafa'):
        self.name=nm
        self.roll=rl
        self.country='Banglasesh'
    def show(self):
        print(self.__dict__)
shimul=students()
shimul.info(7)
shimul.show()