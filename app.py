import gradio as gr
import time
import matplotlib.pyplot as plt
import random
import io
from PIL import Image

def bubble_sort_generator(arr):
    n = len(arr) # Track unsorted region size
    swapped = True
    # yield initial array to visualizer
    yield arr, -1, -1, "initial array state"
    while swapped: # Continue until no swaps occur
        i = 0
        swapped = False
        while i < n - 1: # Compare adjacent elements up to unsorted region
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i] # if next value is less than cur value, swap
                # yield array and swap description to visualizer
                yield arr, i, i+1, f"swap {i} <-> {i+1}"
                swapped = True
            else:
                # yield array and window shift description to visualizer
                yield arr, i, i+1, f"move window {i},{i+1} -> {i+1},{i+2}"
                
            i += 1
        n -= 1 # Shrink unsorted region (largest element now in place)

    # yield sorted array to visualizer
    yield arr, -1, -1, "sorted"

def visualize_sort(array_size, array_maximum, delay):
    """
    Generates a list, sorts it with the chosen algorithm generator, 
    and yields matplotlib plots for Gradio to display.
    """
    arr = [random.randint(1, array_maximum) for _ in range(array_size)]
    sort_gen = bubble_sort_generator(arr)

    # iterate through states in bubble sort generator
    for current_arr, idx1, idx2, state in sort_gen:
        
        # Create a matplotlib figure
        fig, ax = plt.subplots()
        
        # Set bar colors based on the current state
        colors = ['blue'] * array_size
        if idx1 != -1:
            colors[idx1] = 'red'
        if idx2 != -1:
            colors[idx2] = 'red'

        # create matplot bar graph
        ax.bar(range(array_size), current_arr, color=colors)
        ax.set_xticks([])

        # set the title of the graph to the current operation in the bubble sort
        ax.set_title(state)

        # disable matplot autoscaling and set plot limits
        ax.set_ylim(0, array_maximum + 5)
        ax.set_xlim(-1, array_size)
        ax.autoscale(False)

        # Convert plot to image
        buffer = io.BytesIO() # create buffer to store image data
        plt.savefig(buffer, format='png', bbox_inches='tight') # save plot as binary data to buffer
        plt.close(fig) # close plot
        img = Image.open(buffer) # load data from buffer as image

        # yield image to gradio
        yield img

        # close image
        buffer.close()

        # apply step delay
        if delay > 0:
            time.sleep(delay)
        
if __name__ == "__main__":
    # Define inputs and outputs for the Gradio interface
    inputs = [
        gr.Slider(minimum=10, maximum=100, step=1, label="Array Size", value=50),
        gr.Slider(minimum=10, maximum=100, step=1, label="Array Max", value=50),
        gr.Slider(minimum=0, maximum=1, step=0.1, label="Step Delay (s)", value=0)
    ]

    output = gr.Image()

    # Create the Gradio interface
    gr.Interface(
        fn=visualize_sort,
        inputs=inputs,
        outputs=output,
        title="Bubble Search App",
        description="sorts an integer array using the bubble sort algorithm while displaying operations and array states with a real-time visualizer"
    ).launch()


