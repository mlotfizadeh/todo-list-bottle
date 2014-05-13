<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Open tasks</title>
</head>
<body>
    %#template to generate a HTML from a list of tuples
    <p>The open items are as follows:</p>
    <ul>
    %for row in rows:
        <li><a href='edit/{{row[0]}}'>{{row[1]}}</a></li>
    %end
    </ul>
</body>
</html>
