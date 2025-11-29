# CISC121_final_project

# Algorithm Name 
Bubble sort

## Demo video/gif/screenshot of test 
https://github.com/user-attachments/assets/6a9a145d-811d-421b-b817-081974b9e85c

*this video is at 4x speed

## Problem Breakdown & Computational Thinking 
Bubble sort works by repeatedly going over each value in the unsorted part list and swapping values which are larger then the value at the next index forward, this leads to the highest value being moved to the right-side of the list, which is then considered sorted and not included in the next swapping operation. This code provides a gradio based GUI/visualizer to show how bubble sort works of a list of "Array Size" integer entries of 0 to "Array Max" size.

## Steps to Run 
Algorithm Steps:

Initialize: Start with an unsorted array of integers

Outer Loop: For each element position from the beginning to the end of the array:

Inner Loop: Compare adjacent elements from the start up to the last unsorted position:
  1. If the current element is greater than the next element, swap them
  2. Continue comparing and swapping until reaching the end of the unsorted section  
  3. After each complete pass, the largest unsorted element is now in its correct final position, reduce the unsorted section by one element

Steps for running the Application:
  1. Access the hugging face space through the provided link
  2. Set "Array Size" to specify how many elements to sort
  3. Set "Array Max" to define the maximum value for generated numbers
  4. Click "Generate and Sort" to watch the visualization

## Hugging Face Link 
https://huggingface.co/spaces/AlexKurinaQueens/BubbleSortApp

## Author & Acknowledgment 
Alexander Kurina

Assistance from claude 4.5 sonnet was used to help in programming the GUI
