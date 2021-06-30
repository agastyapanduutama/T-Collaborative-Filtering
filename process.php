<?php

// Get data Post
$post =  $_POST['jenis_kulit'];

// Execute Python Program
$execute = shell_exec("python3 /opt/lampp/htdocs/collaborativefiltering/recommend/skinRecommendation.py " .  $post);


// Get Result from variable execute
if ($execute != NULL) {
    echo "Jenis Produk yang direkomendasikan <br>";
    echo $execute;
}else{
    echo "Terjadi kesalahan";
}
