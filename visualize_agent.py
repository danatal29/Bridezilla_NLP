from graphviz import Digraph
from IPython.display import Image, display
import imageio
import cv2
import numpy as np

def create_custom_graph_new(nodes, special_node, edges, main_color, special_color, i, size='8,8', dpi='300', ranksep='0.5', nodesep='0.5'):
    # Create a new directed graph
    dot = Digraph()

    # Set graph size, resolution, and spacing attributes
    dot.attr(size=size, dpi=dpi, ranksep=ranksep, nodesep=nodesep, ratio='fill', pad='0.5')

    # Define node styles
    node_style = {
        'style': 'filled',
        'shape': 'box',
        'fontname': 'Helvetica-Bold',
        'fontsize': '14',
        'fontcolor': 'black',
        'width': '2.5',
        'height': '1.0',
        'fixedsize': 'true'
    }

    special_node_style = {
        'style': 'filled',
        'shape': 'ellipse',
        'fontname': 'Helvetica-Bold',
        'fontsize': '14',
        'fontcolor': 'black',
        'width': '2.5',
        'height': '1.0',
        'fixedsize': 'true'
    }

    # Add nodes with custom labels and font attributes
    for node in nodes:
        if node == special_node:
            dot.node(node, node, **special_node_style, color=special_color)
        else:
            dot.node(node, node, **node_style, color=main_color)

    # Define edge styles
    solid_edge_style = {
        'style': 'solid',
        'fontname': 'Helvetica-Bold',
        'fontsize': '12',
        'fontcolor': 'black'
    }

    dashed_edge_style = {
        'style': 'dashed',
        'fontname': 'Helvetica-Bold',
        'fontsize': '12',
        'fontcolor': 'black'
    }

    dotted_edge_style = {
        'style': 'dotted',
        'fontname': 'Helvetica-Bold',
        'fontsize': '12',
        'fontcolor': 'black'
    }

    # Add edges with labels and font attributes
    for edge in edges:
        start, end, label, style = edge
        if style == 'solid':
            dot.edge(start, end, label=label, **solid_edge_style)
        elif style == 'dashed':
            dot.edge(start, end, label=label, **dashed_edge_style)
        elif style == 'dotted':
            dot.edge(start, end, label=label, **dotted_edge_style)

    # Render and save the graph as an image file
    filename = f'frame_{i}'
    dot.render(filename, format='png', view=False)
    display(Image(filename=f'{filename}.png'))

# Function to create video from frames
def create_video_from_frames_new(frame_count, output_filename='graph_video.mp4', fps=1):
    with imageio.get_writer(output_filename, fps=fps) as writer:
        for i in range(frame_count):
            filename = f'frame_{i}.png'
            image = imageio.imread(filename)
            print(f'{i} {image.shape}')
            writer.append_data(image)
    print(f"Video created: {output_filename}")


def get_place_name(input):
  url = input['url']
  place_name = url.split('place/')[1].split('/')[0].replace('+', ' ')
  return place_name
