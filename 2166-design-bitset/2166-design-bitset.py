class Bitset:

    def __init__(self, size: int):
        self.bitset = [0] * size
        self.flip_set = [1] * size
        self.bit_count = 0

    def fix(self, idx: int) -> None:
        if not self.bitset[idx]:
            self.bitset[idx] = 1
            self.flip_set[idx] = 0
            self.bit_count += 1
        
    def unfix(self, idx: int) -> None:
        if self.bitset[idx]:
            self.bitset[idx] = 0
            self.flip_set[idx] = 1
            self.bit_count -= 1

     
    def flip(self) -> None:
       # just exchage the array in O(1) operation
        self.bitset, self.flip_set = self.flip_set, self.bitset
        # also calculate the bit count for flipped version
        self.bit_count = len(self.bitset) - self.bit_count
        
    def all(self) -> bool:
        return self.bit_count == len(self.bitset)
    
    def one(self) -> bool:
        return self.bit_count > 0

    def count(self) -> int:
        return self.bit_count

    def toString(self) -> str:
        return ''.join(str(each) for each in self.bitset)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()