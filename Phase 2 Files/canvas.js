<!DOCTYPE HTML>
<html>

<head>
    <script type="text/javascript">
        window.onload = function() {
            var dps = []; //dataPoints.

            var chart = new CanvasJS.Chart("chartContainer", {
                title: {
                    text: "Accepting DataPoints from User Input"
                },
                data: [{
                    type: "line",
                    dataPoints: dps
                }]
            });


            function addDataPointsAndRender() {
                xValue = Number(document.getElementById("xValue").value);
                yValue = Number(document.getElementById("yValue").value);
                dps.push({
                    x: xValue,
                    y: yValue
                });
                chart.render();
            }

            var renderButton = document.getElementById("renderButton");
            renderButton.addEventListener("click", addDataPointsAndRender);
        }
    </script>

</head>

<body>
    X Value:
    <input id="xValue" type="number" step="any" placeholder="Enter X-Value"> Y Value:
    <input id="yValue" type="number" step="any" placeholder="Enter Y-Value">
    <button id="renderButton">Add DataPoint & Render</button>
    <div id="chartContainer" style="height: 270px; width: 100%;">
    </div>
</body>

</html>
