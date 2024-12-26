import pygame
from src.algorithms import bubble_sort, quick_sort, merge_sort
from src.utils import generate_array, draw_array, COLORS

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Clock and font
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 24)

# Algorithm options
ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}
current_algorithm = "Bubble Sort"

def main():
    global current_algorithm
    running = True
    array = generate_array(50, 10, 100)  # Generate a random array
    sorting = False
    sorted_array = None
    sort_generator = None

    while running:
        SCREEN.fill(COLORS["background"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    # Initialize low and high for quick_sort
                    if current_algorithm == "Quick Sort":
                        low = 0
                        high = len(array) - 1
                        sort_generator = ALGORITHMS[current_algorithm](array, low, high)  # Pass array, low, high
                    else:
                        sort_generator = ALGORITHMS[current_algorithm](array)  # For bubble_sort and merge_sort, just pass the array

                # Cycle through algorithms with arrow keys
                elif event.key == pygame.K_RIGHT:
                    algorithm_names = list(ALGORITHMS.keys())
                    current_algorithm = algorithm_names[(algorithm_names.index(current_algorithm) + 1) % len(algorithm_names)]

        if sorting and sort_generator:
            try:
                sorted_array = next(sort_generator)
            except StopIteration:
                sorting = False
                sorted_array = array

        # Draw the array
        draw_array(SCREEN, sorted_array or array)

        # Draw instructions
        instructions = FONT.render(f"Press SPACE to start sorting", True, COLORS["text"])
        SCREEN.blit(instructions, (20, 20))

        # Display current algorithm
        algorithm_text = FONT.render(f"Algorithm: {current_algorithm}", True, COLORS["text"])
        SCREEN.blit(algorithm_text, (20, 60))

        pygame.display.flip()
        CLOCK.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
