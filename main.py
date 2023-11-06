import cProfile
import pstats

from src.classes.alien import Alien

def main():
    for _ in range(0, 100000):
        alien = Alien.generate_random(False)

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('tottime')
    stats.print_stats()