import random

class MultimediaIntegration:
    def __init__(self):
        self.media_library = {
            "images": {
                "fantasy": ["forest.jpg", "castle.png", "dragon.jpg"],
                "sci-fi": ["spaceship.png", "alien_world.png", "cyber_city.jpg"],
                "mystery": ["dark_alley.jpg", "mansion.png", "foggy_city.jpg"],
                "adventure": ["desert_island.jpg", "jungle.jpg", "treasure_map.png"]
            },
            "sounds": {
                "fantasy": ["forest_ambience.mp3", "castle_town.mp3"],
                "sci-fi": ["spaceship_hum.mp3", "laser_gun.mp3"],
                "mystery": ["footsteps.mp3", "thunderstorm.mp3"],
                "adventure": ["ocean_waves.mp3", "jungle_sounds.mp3"]
            },
            "animations": {
                "fantasy": ["dragon_flying.gif", "wizard_casting.gif"],
                "sci-fi": ["spaceship_landing.gif", "alien_walking.gif"],
                "mystery": ["shadow_moving.gif", "car_driving.gif"],
                "adventure": ["pirate_ship.gif", "treasure_chest.gif"]
            }
        }

    def suggest_media(self, genre, media_type="images"):
        return random.choice(self.media_library.get(media_type, {}).get(genre, []))

if __name__ == "__main__":
    media = MultimediaIntegration()
    print("Suggested Image:", media.suggest_media("sci-fi", "images"))
    print("Suggested Sound:", media.suggest_media("fantasy", "sounds"))
