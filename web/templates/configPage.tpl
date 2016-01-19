<!DOCTYPE html>
<html>
<head>
    <title>The configuration page</title>
    <script src="/jquery-2.1.4.min.js"></script>
    <script src="/jquery.tablesorter.min.js"></script>
    <script src="/multifilter.min.js"></script>
    <link rel="stylesheet" type="text/css" href="/Table_muted.css">
</head>
<body>

<h1> The Configuration page for <font color="indianred">{{key}}</font> </h1>

<p>Please use this page for inserting all configuration information for the different views.</p>

% keys = info.keys()

% for v in info[keys[0]]:
    <input class="filter" name="{{v}}" placeholder="{{v}}" data-col="{{v}}">
% end

<div style='width:100%; height:600px; overflow-y:scroll; overflow-x:scroll;'>
    <table id="test">
        <thead>
            <tr>
                <th></th>
                <th></th>
                % for v in info[keys[0]]:
                <th> 
                    {{v}} 
                </th>
                % end
            </tr>
        </thead>

        % for i, k in enumerate(keys[1:]):
            <tr>
                <td><a href="http://localhost:8080/config/{{key}}/duplicate/{{i}}">
                    [<font color="#00ad17">duplicate</font>]
                </a></td>
                <td><a href="http://localhost:8080/config/{{key}}/delete/{{i}}">
                    [<font color="#b30039">delete</font>]
                </a></td>
                % for v in info[keys[k]]:
                <td contenteditable="true">{{v}}</td>
                % end
            </tr>
        % end

    </table>
</div>

<script type="text/javascript">
    function sendData() {

        // First get the data into a string ...
        var tbl = $('table#test').html();

        $.ajax({
                  type : "POST",
                  url  : '/config/{{key}}/Update',
                  data : "content="+tbl,
                  success: function(data) {
                      window.location.href = "http://localhost:8080/config/{{key}}/success";
                  },
                  error : function() {
                  }
            });
    }

    $(document).ready(function(){
        $("#test").tablesorter();
        $('.filter').multifilter();
    }); 

</script>

<p>
<button onclick="sendData()">Update</button>
</p>

</body>
</html>
