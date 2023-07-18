import numpy as np
from random import *
import random
import pandas as pd


class Hanwoo:
    def __init__(self):
        print("Game Started")

        name = input("Please Enter your name : ")
        self.name = name
        print(f"Hello! {self.name}")

        number = input("Please Enter your animal number : ")
        self.number = number

    def Generation(self):
        My_animal_number = self.number
        name = self.name
        sex_list = ["Male", "Female"] * int(My_animal_number / 2)
        random.shuffle(sex_list)
        pheno = list(
            map(
                lambda x: round(x, 1),
                list(np.random.normal(340, 2, My_animal_number)),
            )
        )
        data_set = pd.DataFrame(
            zip(sex_list, pheno),
            columns=["sex", "pheno"],
            index=My_animal_number,
        )
        print(f"{name}'s hanwoo farm mede. You got these cows.")
        print(data_set)
        return data_set


Hanwoo()
