<?php

    class LetsController{

        $postData = new ArrayObject($_POST, ArrayObject::ARRAY_AS_PROPS);

        public function con_db(){
            $server = "localhost";
            $username = "root";
            $password = "ddude352314d";
            $database = "test";

            $con = mysql_connect($server, $username, $password) or die ("Could not connect: " . mysql_error());

            mysql_select_db($database, $con);
        }

        public function close_con(){
            mysql_close($con);
        }

        public function sign_up($name, $last_name, $email, $passwd){
            if(strlen($name) < 1){
                echo "Please, write your name.";
            }
            elseif(strlen($last_name) < 1){
                echo "Please, write your last name.";
            }
            elseif(strlen($email) < 1){
                echo "Please, write your email.";
            }
            elseif(strlen($passwd) < 6){
                echo "Your password need at least 6 characters.";
            }

        }

        public function login($email, $passwd){
            if(strlen($name) < 1){
                echo "Please, write your email.";
            }
            elseif(strlen($passwd) < 6){
                echo "Your password need at least 6 characters.";
            }

        }

    }
?>
