import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# Vocal Categories ranges 
categories = {
    'Soprano': {'range': [261.63, 1046.50], 'color': 'grey'},
    'Mezzo-Soprano': {'range': [220.00, 880.00], 'color': 'orange'},
    'Alto': {'range': [174.61, 698.46], 'color': 'cyan'},
    'Tenor': {'range': [130.81, 523.25], 'color': 'green'},
    'Baritone': {'range': [98.00, 392.00], 'color': 'blue'},
    'Bass': {'range': [82.41, 329.63], 'color': 'red'}
}

def draw_horizontal_shadows(plt, transparency):    
    for  category_name, v in categories.items():
        plt.axhspan(v["range"][0], v["range"][1], facecolor = v["color"], alpha = transparency)            

def draw_legend(plt, transparency):    
    handle_values = []
    for  category_name, v in categories.items():        
        handle_values.append(mpatches.Patch(color=v["color"], alpha=transparency, label= f'{category_name}-{v["range"]}' ))
    plt.legend(handles= handle_values, loc='upper left', bbox_to_anchor=(1, 1))