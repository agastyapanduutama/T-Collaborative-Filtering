<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skincare Recommendation</title>
</head>

<body>

    <form action="process.php" method="POST">
        <ul>
            Pilih jenis kulit
            <li><input name="jenis_kulit" required type="radio" value="Combination">Combination</li>
            <li><input name="jenis_kulit" required type="radio" value="Dry">Dry</li>
            <li><input name="jenis_kulit" required type="radio" value="Normal">Normal</li>
            <li><input name="jenis_kulit" required type="radio" value="Oily">Oily</li>
            <li><input name="jenis_kulit" required type="radio" value="sensitif">sensitif</li>
        </ul>
        <button type="submit">Kirim</button>
    </form>

</body>

</html>