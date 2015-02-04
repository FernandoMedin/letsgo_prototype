<?php

    class LetsController{

        $postData = new ArrayObject($_POST, ArrayObject::ARRAY_AS_PROPS);

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
