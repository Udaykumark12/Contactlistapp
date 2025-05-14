from oops_practice import M

class TestB:
    z = M()

    def test_b(self):
       self.n = self.z.a()
       assert self.n == 20



    def test_c(self):
        self.test_b()
        print(self.n)


