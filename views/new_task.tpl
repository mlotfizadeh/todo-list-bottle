<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Add a new task</title>
</head>
<body>
    <p>Add a new task to the ToDo list:</p>
    <form action="/new" method="POST" acept-charset="utf-8">
        <input type="text" size="100" maxlength="100" name="task">
        <input type="submit" name="save" value="save">
    </form>
</body>
</html>
