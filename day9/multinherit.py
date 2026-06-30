class central_gov:
    def cent(self):
        print("It is central gov")
class state_gov(central_gov):
    def state(self):
        print("It is state gov")
class local_pepl(state_gov):
    def loc(self):
        print("It is loc pepl")
s=local_pepl()
s.loc()
s.state()
s.cent()