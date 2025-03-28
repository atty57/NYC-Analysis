
from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from src.visualizations import setup_chart, line_chart
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Create sample data for yearly collisions
    years = list(range(2018, 2023))
    collisions = [45000, 43000, 29000, 35000, 40000]
    
    # Create plot using existing visualization function
    fig, ax = setup_chart(
        figsize=(10, 6),
        title="Annual NYC Collisions",
        xlabel="Year",
        ylabel="Number of Collisions"
    )
    
    line_chart(
        [(years, collisions)],
        style="default",
        markerstyle="o",
        markersize=8,
        linewidth=3
    )
    
    # Convert plot to base64 for web display
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    
    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
