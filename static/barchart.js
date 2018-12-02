function loadBar(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/json", true);
    xmlhttp.responseType = "json";
    xmlhttp.send();
    xmlhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            var barparams = getbarparam(this.response);
            Plotly.plot('graph', barparams.data, barparams.layout, {responsive:true});
        }
    };
}

function setData(arr){
    var data = [{
        x: arr.site_name,
        y: arr.pwncount,
        marker:{color: 'rgb(255, 255, 255)'},
        text: arr.site_breach_date,
        type: 'bar'
    }];
    return data;
}

function setLayout(){
    var layout = {
        hoverlabel: {bgcolor: 'white'},
        title: 'Ten Most Recent Breach Sites',
        paper_bgcolor: 'rgba(200, 222, 247, 0.3)',
        plot_bgcolor: 'rgba(0, 0, 0, 0)'
    }
    return layout;
}

function getbarparam(json){

    var dataA = setData(json);
    var layoutA = setLayout(json);
    var object = {data: dataA, layout: layoutA};
    return object;
}
