<!DOCTYPE html>
<html>
<head>
    <title>Config Summary</title>
    <link rel="stylesheet" type="text/css" href="/Table_muted.css">
</head>
<body>

<h1> Please select the page you want to see ... </h1>

<p>
The following are links to the values that you may wish to view/configure. 
</p>

% for k in sorted(configFiles.keys()):
<a href="http://localhost:8080/config/{{k}}"> {{k}} </a> <br>
% end

</body>
</html>
