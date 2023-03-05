import matplotlib.pyplot as plt

def main():
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Построить линейный график

    plt.plot(x_coords, y_coords)
    plt.xlabel("что-то по оси Х")
    plt.ylabel("Что-то по оси У")
    plt.grid(True)
    plt.title("Просто линейный график чего-то там")

    # Показать линейный график

    plt.show()


if __name__ == '__main__':
    main()