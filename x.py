class IntTe:
  def __init__(self, data) -> None:
    self.data = data
x = [IntTe(3), IntTe(244), IntTe(2454), IntTe(1)]

print(sorted(x, key=lambda x : x.data, reverse=True))