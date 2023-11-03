import cProfile
import pstats

from src.classes.alien import Alien

def main():
    for _ in range(0, 1000):
        alien1 = Alien.generate_random()
        alien1.export_to_json('alien.json')

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats()