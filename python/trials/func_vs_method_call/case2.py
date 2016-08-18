import func
import time


class Base:
    def homeMethod(self):
        # return func.complex_function()
        pass

    def proxy(self, i):
        self.homeMethod()


class Derived(Base):
    def homeMethod(self):
        return func.complex_function()
# s_time = time.time()
d = Derived()
for i in range(20):
    d.proxy(i)
# e_time = time.time()
# print(e_time - s_time)


# s_time = time.time()

# for _ in range(20):
# func.complex_function()

# e_time = time.time()
# print(e_time - s_time)
