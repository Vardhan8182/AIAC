class emp:
    def _init_(self, n, s):  # Corrected constructor name
        self.n = n
        self.s = s

    def inc(self, p):
        self.s = self.s + (self.s * p / 100)

    def pr(self):
        print("emp:", self.n, "salary:", self.s)

# Create an employee object and test
e1 = emp("Alice", 50000)
e1.pr()
e1.inc(10)
e1.pr()