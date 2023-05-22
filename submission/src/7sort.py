import json
import os
import random
import time
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import csv

class VisualizeSorting(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Visualize Sorting Algorithms")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.bubble_button = QPushButton("bubble Sorting")
        self.bubble_button.clicked.connect(self.visualize_bubble_sort)
        self.selection = QPushButton("selection Sorting")
        self.selection.clicked.connect(self.visualize_selection_sort)
        self.insertion = QPushButton("insertion Sorting")
        self.insertion.clicked.connect(self.visualize_insertion_sort)
        self.merge = QPushButton("merge Sorting")
        self.merge.clicked.connect(self.visualize_merge_sort)
        self.quick = QPushButton("quick Sorting")
        self.quick.clicked.connect(self.visualize_quick_sort)
        self.counting = QPushButton("counting Sorting")
        self.counting.clicked.connect(self.visualize_counting_sort)
        self.radix = QPushButton("radix Sorting")
        self.radix.clicked.connect(self.visualize_radix_sort)

        # Add counter for time in top of the frame
        self.time = QLabel(
            "Time: " + str(datetime.datetime.now().strftime("%H:%M:%S")), self
        )
        self.time.move(10, 10)
        self.time.resize(100, 20)


        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.bubble_button)
        layout.addWidget(self.selection)
        layout.addWidget(self.insertion)
        layout.addWidget(self.merge)
        layout.addWidget(self.quick)
        layout.addWidget(self.counting)
        layout.addWidget(self.radix)
        
        self.central_widget.setLayout(layout)
        # Add counter for time in top of the frame
        self.time = QLabel(
            "Time: " + str(datetime.datetime.now().strftime("%H:%M:%S")), self
        )
        self.time.move(10, 10)
        self.time.resize(100, 20)
        self.time.show()
        # Array is the list of numbers to be sorted
        # hard code the array for now 
        # set directory to the file location
        
        filename = "Salaries.csv"
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            data = []

            for row in csv_reader:
                name = row[0]
                salary = int(float(row[1].replace(",", "").replace("$", "")))
                data.append((salary))        
        self.array = data
        name_data = []
        with open(filename, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                name = row[0]
                name_data.append(name)
        self.name = name_data
        # Match the array to the name
        self.name_array = dict(zip(self.name, self.array))
        # Sort the name array
        self.name_array = dict(sorted(self.name_array.items(), key=lambda item: item[1]))
        # Get the sorted name

    def  visualize_quick_sort(self):
        # Calculate the running time of the algorithm
        print("quick_sort")
        start_time = time.time()
        array = list(self.array)
        n = len(array)
        def partition(array, low, high):
            i = (low - 1)
            pivot = array[high]
            for j in range(low, high):
                if array[j] <= pivot:
                    i = i + 1
                    array[i], array[j] = array[j], array[i]

                    
                    self.update_plot(array)
                    QApplication.processEvents()
            array[i + 1], array[high] = array[high], array[i + 1]
            return (i + 1)
        def quick_sort(array, low, high):
            if len(array) == 1:
                return array
            if low < high:
                pi = partition(array, low, high)
                quick_sort(array, low, pi - 1)
                quick_sort(array, pi + 1, high)
        quick_sort(array, 0, n - 1)
        end_time = time.time()
        print("Running time: ", end_time - start_time)
        sorted_array = array
        self.store_sorted_data(sorted_array)        
    def visualize_merge_sort(self):
        # Calculate the running time of the algorithm
        print("merge_sort")
        start_time = time.time()
        array = list(self.array)
        n = len(array)
        def merge_sort(array):
            if len(array) > 1:
                mid = len(array) // 2
                left = array[:mid]
                right = array[mid:]
                merge_sort(left)
                merge_sort(right)
                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        array[k] = left[i]
                        i += 1
                    else:
                        array[k] = right[j]
                        j += 1
                    k += 1
                while i < len(left):
                    array[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    array[k] = right[j]
                    j += 1
                    k += 1
                self.update_plot(array)
                QApplication.processEvents()
        merge_sort(array)
        end_time = time.time()
        print("Running time: ", end_time - start_time)
        sorted_array = array
        self.store_sorted_data(sorted_array)        

    def visualize_bubble_sort(self):
        # Calculate the running time of the algorithm
        print("bubble_sort")
        start_time = time.time()
        array = list(self.array[:50])
        n = len(array)
        for i in range(n):
            swap_flag = False
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swap_flag = True

                self.update_plot(array)
                QApplication.processEvents()

            if not swap_flag:
                break

        end_time = time.time()
        print("Running time: ", end_time - start_time)
        sorted_array = array
        self.store_sorted_data(sorted_array)
    def visualize_selection_sort(self):
    # Calculate the running time of the algorithm
        print("selection_sort")
        start_time = time.time()
        array = list(self.array[:50])
        n = len(array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if array[min_index] > array[j]:
                    min_index = j

            array[i], array[min_index] = array[min_index], array[i]

            self.update_plot(array)
            QApplication.processEvents()
        end_time = time.time()
        print("Running time: ", end_time - start_time)
        sorted_array = array
        self.store_sorted_data(sorted_array)

    def visualize_insertion_sort(self):
        # Calculate the running time of the algorithm
        print("insertion_sort")
        start_time = time.time()
        array = list(self.array)
        n = len(array)
        for i in range(1, n):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

            self.update_plot(array)
            QApplication.processEvents()
        end_time = time.time()
        print("Running time: ", end_time - start_time)
        sorted_array = array
        self.store_sorted_data(sorted_array)        
    def visualize_counting_sort(self):
    # Calculate the running time of the algorithm
        print("counting_sort")
        start_time = time.time()

        # Initialize variables
        array = (list(self.array))
        max_value = max(array)
        counts = ([0] * (max_value + 1))
        result = [0] * len(array)

        # Count the occurrences of each element in the input array
        for value in array:
            counts[value] += 1

        # Calculate the running sums of the counts
        for i in range(1, len(counts)):
            counts[i] += counts[i - 1]

        # Place each element in its correct position in the output array
        for i in range(len(array)):
            value = array[i]
            index = counts[value] - 1
            result[index] = value
            counts[value] -= 1

            self.update_plot(result)
            QApplication.processEvents()

        end_time = time.time()
        print("Running time: ", end_time - start_time)
        sorted_array = array
        self.store_sorted_data(sorted_array)
    def visualize_radix_sort(self):
        # Calculate the running time of the algorithm
        print("radix_sort")
        start_time = time.time()

        # Initialize variables
        array = list(self.array)
        RADIX = 10
        placement = 1
        max_digit = max(array)

        # Loop until we reach the largest significant digit
        while placement < max_digit:
            # Declare and initialize buckets
            buckets = [list() for _ in range(RADIX)]

            # Split array between lists
            for i in array:
                tmp = int((i / placement) % RADIX)
                buckets[tmp].append(i)

            # Empty lists into input array
            a = 0
            for b in range(RADIX):
                buck = buckets[b]
                for i in buck:
                    array[a] = i
                    a += 1

            # Move to next significant digit
            placement *= RADIX

            self.update_plot(array)
            QApplication.processEvents()

        end_time = time.time()
        

        print("Running time: ", end_time - start_time)
        sorted_array = array
        self.store_sorted_data(sorted_array)
    def store_sorted_data(self, sorted_array):
        # Write the sorted array to a JSON 
        # Create file 
        filename = "sorted_data.json"
        # Check if the file exists
        if os.path.exists(filename):
            # Ask the user if they want to overwrite the file
            overwrite = QMessageBox.question(self, "File exists", "File already exists. Overwrite?", QMessageBox.Yes | QMessageBox.No)
            if overwrite == QMessageBox.Yes:
                with open(filename, 'w') as file:
                    json.dump(sorted_array, file)

        else:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(sorted_array, file)

        
    def update_plot(self, array):
        plt.cla()  # Clear the previous plot
        plt.bar(range(len(array)), array)
        self.canvas.draw()
    
    
if __name__ == "__main__":
    app = QApplication([])
    window = VisualizeSorting()
    window.show()
    app.exec_()