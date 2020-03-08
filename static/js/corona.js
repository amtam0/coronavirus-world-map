var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
today = mm + '/' + dd + '/' + yyyy;

Plotly.d3.csv('static/data/corona.csv', function(err, rows){
      function unpack(rows, key) {
          return rows.map(function(row) { return row[key]; });
      }

    var data = [{
        type: 'choropleth',
        locationmode: "ISO-3",
        locations: unpack(rows, 'iso_alpha'),
        z: unpack(rows, 'TotalCases'),
        text: unpack(rows, 'text'),
        colorscale : 'Portland',
        autocolorscale: false,
        reversescale: false,

        zmin: 0,
        zmax: 2000,
        colorbar: {
            title: 'Number of cases',
            // thickness: 1
        },
    }];

    var layout = {
      title: `Daily Coronavirus Cases in the World [${ today }] <br>Source: <a href="https://www.worldometers.info/coronavirus/"> Worldometers</a>`,
    //   width: 500,
      height: 800,
      geo: {
          showframe: false,
        //   projection: {
        //       type: 'robinson'
        //   }
      }
    };

    Plotly.newPlot("myDiv", data, layout, {showLink: false});

});

