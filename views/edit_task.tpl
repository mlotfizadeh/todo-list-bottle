<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit a task</title>
</head>
<body>

    <p>Edit the task with ID = {{no}}</p>
    <form action="/edit/{{no}}" method="POST" acept-charset="utf-8">
        <input type="text" name="task" value="{{task}}" size="100" maxlength="100">
        <select name="status">
            <option>open</option>
            %if status == 0:
            <option selected>closed</option>
            %else:
            <option>closed</option>
            %end
        </select>
        <input type="submit" name="save" value="save">
    </form>

</body>
</html>