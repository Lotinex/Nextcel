class Counter(list):
    def __init__(self):
        super().__init__([])

    def __repr__(self):
        R = ""
        for e in self:
            R += f"{e['name']}   {e['count']}\n"

        return R