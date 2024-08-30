from random import randint
import random
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer  
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_ability()
        self.change = self.change_name()
        self.power = randint(10, 50)
        self.hp = randint(30, 100)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
    #метод получения способностей
    def get_ability(self):
        abilities = ['fire', 'water', 'poison', 't72av_turms-t']
        random.choice(abilities)
    
    # Метод класса для получения информации
    def info(self):
        return f'''Имя твоего покеомона: {self.name}
    Сила: {self.power}, HP: {self.hp}'''
        

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def abil_inf(self):
        return f"Способность: {self.ability}"
    
    def change_name(self):
        newname = ['podpivaso', 'skufidoni', 'sigmanos', 'buryad_strong']
        self.name = random.choice(newname)
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return f'oh shit! враг применил щит'

        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f'сражение @{self.name} с @{enemy.name}'
        else:
            enemy.hp = 0
            return f'victory!!'
    
class Wizard(Pokemon):
        pass

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(3,10)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f'крит урон - {super_power}'

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))


