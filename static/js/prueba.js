var trace1 = {
    x:['Zebras', 'Lions', 'Pelicans'],
    y: [90, 40, 60],
    type: 'bar',
    name: 'New York Zoo'
};

var trace2 = {
    x:['Zebras', 'Lions', 'Pelicans'],
    y: [10, 80, 45],
    type: 'bar',
    name: 'San Francisco Zoo'
};

var data = [trace1, trace2];

var layout = {
    title: {
        text: 'Hide the Modebar'
    },
    showlegend: true
};

Plotly.newPlot('myDiv', data, layout, {displayModeBar: false});
