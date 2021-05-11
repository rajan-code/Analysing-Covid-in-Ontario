import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple


def get_all_ratios() -> List[Tuple[str, float]]:
    """
    Return (Date,covid_cases/num_centres) for all days.
    """
    with open('all_data.txt') as file:
        lines = file.readlines()
        appending_file = open('data.txt', 'a')
        lst = []
        for line in lines[2:]:
            if line != '\n':
                parts = line.split(',')
                date = parts[0]
                num_centres = int(parts[2])
                covid_cases = int(parts[3])
                lst.append((date, covid_cases/num_centres))
        appending_file.close()
    return lst


def append_to_txt_file():
    """
    Note: data.txt should be empty when this function is called.
    For each stat in all_data.txt, append (Number of days since June 2020,number of covid cases/number of testing
    centres) to data.txt.
    """
    with open('all_data.txt') as file:
        lines = file.readlines()
        appending_file = open('data.txt', 'a')
        for line in lines[2:]:
            if line != '\n':
                parts = line.split(',')
                days_since = int(parts[1])
                num_centres = int(parts[2])
                covid_cases = int(parts[3])
                appending_file.write(f'{days_since},{covid_cases/num_centres}\n')
        appending_file.close()


def draw_graph():
    all_ratios = get_all_ratios()
    all_ratios = sorted(all_ratios, key=lambda x: x[1])
    print('Minimum covid cases/number of testing centres:', all_ratios[0])
    print('Maxiumum covid cases/number of testing centres:', all_ratios[-1])
    data = np.genfromtxt("data.txt", delimiter=",", names=["x", "y"])
    dates = ['June 1', 'July 6', 'August 4', 'September 2', 'October 7', 'November 4', 'December 2', 'January 6', 'February 3', 'March 3']
    ticks = [0, 35, 64, 93, 128, 156, 184, 219, 247, 275]
    plt.xticks(ticks, dates)
    plt.plot(data['x'], data['y'])
    plt.ylabel('Number of cases per testing center')
    plt.xlabel('Date')
    plt.title('Coronavirus in Ontario')
    plt.show()


if __name__ == '__main__':
    # append_to_txt_file()
    draw_graph()

