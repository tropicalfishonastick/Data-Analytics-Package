# CODE EXPLAINED : rw_visuals.ipynb

## Random Walk Generator and Visualizer

This Python script generates and visualizes random walks using the Matplotlib library. 

## How It Works

### Importing Libraries

The script begins by importing the necessary libraries:
- `matplotlib.pyplot` for plotting.
- `choice` from the `random` module for making random decisions during the walk.

### Creating the RandomWalk Class

A Python class named `RandomWalk` is defined to generate random walks. In the class's constructor (`__init__` method), the following attributes are initialized:
- `num_points`: The number of points in the walk (default is set to 5000).
- `x_values` and `y_values`: Lists to store the x- and y-coordinates of each point in the walk, starting at (0, 0).

### Defining the `fill_walk` Method

The `fill_walk` method calculates all the points in the walk:
- It uses a `while` loop that continues until the desired number of points (`num_points`) is reached.
- Inside the loop, random decisions are made for the direction and distance of each step:
  - `x_direction` and `y_direction` are randomly chosen to determine right (+1) or left (-1) movement in the x and y directions.
  - `x_distance` and `y_distance` are randomly chosen values that dictate the step's length in each direction.
  - `x_step` and `y_step` are calculated based on direction and distance.
- Steps with both `x_step` and `y_step` equal to zero are rejected, ensuring the walk doesn't stand still.
- The new coordinates (`x` and `y`) are calculated by adding the step values to the last stored coordinates.
- These new coordinates are appended to the `x_values` and `y_values` lists.

### Generating and Visualizing Random Walks

The script generates and visualizes multiple random walks interactively:
- An infinite loop (`while True`) is set up to generate walks until the user decides to stop.
- Inside the loop:
  - An instance of the `RandomWalk` class with 50,000 points is created, and the `fill_walk` method is called to generate the walk data.
  - A range of point numbers (`point_numbers`) is created for coloring the points, resulting in a color gradient.
  - The size of the figure is adjusted for better screen fit using `plt.subplots(figsize=(15, 9))`.
  - `ax.scatter` is used to plot the x and y values of the walk, with points colored based on `point_numbers`.
  - The first and last points are emphasized by plotting them in green and red with larger markers.
  - Axes are hidden to create a cleaner visual (`ax.get_xaxis().set_visible(False)` and `ax.get_yaxis().set_visible(False)`).
  - The aspect ratio is set to 'equal' to avoid distortion (`ax.set_aspect('equal')`).
  - A title is added to the plot using `plt.title("Random Walk")`.
  - The plot is displayed using `plt.show()`.

### Asking for User Input

After displaying each walk, the user is prompted for input to determine whether they'd like to generate another walk. Entering 'n' stops the program.

In summary, this script allows interactive exploration of random walks, generating and visualizing them until the user decides to stop. Each walk is unique and can display various patterns due to the random decisions made during the walk generation process.

Feel free to run the script and explore the fascinating world of random walks!
