var data = {'1184212800': 2136520, '1207281600': 252216, '1214884800': 359420698};

function loadHeatMap(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/h-json", true);
    xmlhttp.responseType = "json";
    xmlhttp.send();
    xmlhttp.onreadystatechange = function(){
        if (this.readyState == 4 && this.status == 200){
            createHeatMap(this.response);
        }
    };
}

function createHeatMap(data){
    var cal = new CalHeatMap();
    cal.init({
        itemSelector: document.getElementById("heatmap"),
        domain: "month",
        subDomain: "day",
        start: new Date(2007, 0),
        minDate: new Date(2007, 0),
        domainLabelFormat: "%m",
        domainGutter: 20,
        cellSize: 5,
        verticalOrientation: false,
        domainMargin: 10,
        animationDuration: 800,
        //nextSelector: document.getElementById("domainDynamicDimension-next"),
        //previousSelector: document.getElementById("domainDynamicDimension-previous"),
        legendCellPadding: 5,
        legendColors: {
            min: "#efefef",
            max: "steelblue",
            empty: "white"
        },
        data: data
    });
    //document.getElementById("domainDynamicDimension-next").onclick = cal.previous(6);
    //document.getElementById("domainDynamicDimension-previous").onclick = cal.next(6);
}
