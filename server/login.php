<?php
    header("Access-Control-Allow-Origin: *"); ?>
<?php

    $server = "localhost";
    $username = "root";
    $password = "ddude352314d";
    $database = "test";

    $con = mysql_connect($server, $username, $password) or die ("Could not connect: " . mysql_error());

    mysql_select_db($database, $con);

    $email = mysql_real_escape_string($_POST["email"]);
    $passwd = mysql_real_escape_string($_POST["passwd"]);

    if(strlen($email) < 1){
        die('Error: Please, write your email.');
    }
    elseif(strlen($passwd) < 1){
        die('Error: Your password need at least 6 characters.');
    }

    $result = mysql_query("SELECT name FROM users WHERE email = '$email' and passwd = '$passwd';");

    if(mysql_num_rows($result) == 1){
        session_start();
        $_SESSION['token'] = $_POST['email'];
        $message = "Now you are Log in! Enjoy it!";
        echo json_encode(mysql_result($result, 0));
    }else{
        $data = array('type' => 'error', 'message' => 'Incorrect email or password');
                header('HTTP/1.1 400 Bad Request');
                header('Content-Type: application/json; charset=UTF-8');
                echo json_encode($data);
    }

    mysql_close($con);
?>
