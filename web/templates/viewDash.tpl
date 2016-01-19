<html>
    <head>
        <script src="/plotly-latest.min.js"></script>
        <link rel="stylesheet" type="text/css" href="/Table_web20.css">
    </head>

    <body>
    
    <h1>Display for configuration <font color="indianred">{{config}}</font></h1>
    <p>
        The compiled data is shown below ...
    </p>

    <div style="width: 100%; overflow-x: scroll;">
        {{!data}}
    </div>

    <p>
        The Line graphs are shownbelow ...
    </p>

    {{!line}}

    </body>
</html>