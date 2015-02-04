<?php
    header("Access-Control-Allow-Origin: *"); ?>
<?php

    $server = "localhost";
    $username = "root";
    $password = "ddude352314d";
    $database = "test";

    $con = mysql_connect($server, $username, $password) or die ("Could not connect: " . mysql_error());

    mysql_select_db($database, $con);

    $name = mysql_real_escape_string($_POST["name"]);
    $last_name = mysql_real_escape_string($_POST["last_name"]);
    $email = mysql_real_escape_string($_POST["email"]);
    $passwd = mysql_real_escape_string($_POST["passwd"]);

    if(strlen($name) < 1){
        die('Error: Please, write your name.');
    }
    elseif(strlen($last_name) < 1){
        die('Error: Please, write your last name.');
    }
    elseif(strlen($email) < 1){
        die('Error: Please, write your email.');
    }
    elseif(strlen($passwd) < 6){
        die('Error: Your password need at least 6 characters.');
    }

    $sql = "INSERT INTO users (name, last_name, email, passwd, singup_date) ";
    $sql .= "VALUES ('$name', '$last_name', '$email', '$passwd', now())";

    if (!mysql_query($sql, $con)) {
      die('Error: ' . mysql_error());
    } else {
      echo "Fuck Yeah! :D";
    }

    mysql_close($con);
?>
