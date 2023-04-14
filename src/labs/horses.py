# Encapsulation Homework


class Horse:
    def __init__(self, hair_length: str, breed: str, horse_markings: str):
         self._hair_length = hair_length
         self._breed = breed
         self._horse_markings = horse_markings


    @property
    def hair_length(self) -> str:
        return self._hair_length


    @hair_length.setter
    def hair_length(self, hair_length: str):
        self._hair_length = hair_length

    @property
    def breed_type(self) -> str:
        return self._breed

    @breed_type.setter
    def breed_type(self, breed: str):
        self._breed = breed


    @property
    def horse_markings(self) -> str:
        return self._horse_markings


    @horse_markings.setter
    def horse_markings(self, horse_markings: str):
        self._horse_markings = horse_markings



def main():
    horses_attributes = Horse('long haired', 'Thoroughbred', 'interrupted stripe')
    print(horses_attributes.hair_length)
    print(horses_attributes.breed_type)
    print(horses_attributes.horse_markings)



if __name__ == '__main__':
    main()
