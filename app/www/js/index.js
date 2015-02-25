var app = {
    meController: function($scope){
        $scope.name = function(){ return localStorage.name; }
        $scope.last_name = function(){ return localStorage.last_name; }
        $scope.email = function(){ return localStorage.email; }
        $scope.fullname = function(){ return localStorage.name + " " + localStorage.last_name; }
    },

    mainController: function($scope){
        $scope.name = function(){ return localStorage.name; }
    },
};

var login = {
    validate: function(){
        var val_email = document.getElementById("email").value;
        var val_pass = document.getElementById("passwd").value;

        if(val_email.length == 0){
            alert("Please, write your email.");
        }else if(val_pass.length == 0){
            alert("Please, write your password.");
        }else{
            this.auth(val_email, val_pass);
        }
    },

    auth: function(email, pass){
        $.ajax({
            type: 'POST',
            data: 'email=' + email + '&passwd=' + pass,
            url: 'http://localhost:8000/login/',
            success: function(data){
                console.log(data);
                if(data == "Error"){
                    alert('There was an error finding you account.');
                }else{
                    alert('Now you are loged! Enjoy it!');
                    var obj = JSON.parse(data);
                    localStorage.id_user = obj.id_user;
                    localStorage.name = obj.name;
                    localStorage.last_name = obj.last_name;
                    localStorage.email = obj.email;
                    localStorage.passwd = obj.passwd;
                    window.location.replace('main.html');
                }
            },
            error: function(){
                console.log(data);
                alert('There was an error in the Database.');
            }
        });
    },

    get_create_data: function(){
        var val_name = document.getElementById("name").value;
        var val_last_name = document.getElementById("last_name").value;
        var val_email = document.getElementById("email").value;
        var val_pass = document.getElementById("passwd").value;
        var val_birth = document.getElementById("born").value;
        var val_sex = document.getElementById("sex").value;

        if(val_name.length < 1){
            alert("Please, write your name.");
        }else if(val_last_name.length < 1){
            alert("Please, write your last name.");
        }else if(val_email.length < 5){
            alert("Please, write your email");
        }else if(val_pass.length < 5){
            alert("Your password need at least 6 characters.");
        }else if(val_birth.length < 6){
            alert("Please, select your birth date.");
        }else if(val_sex == 1 || val_sex == 2){
            this.create(val_name, val_last_name, val_email, val_pass, val_birth, val_sex);
        }else{
            alert("Please, choose your sex.");
        }
    },

    create: function(name, last, email, pass, birth, sex){
        $.ajax({
            type: 'POST',
            data: 'name=' + name + '&last_name=' + last + '&email=' + email + '&passwd=' + pass + '&born=' + birth + '&sex=' + sex,
            url: 'http://localhost:8000/new_user/',
            success: function(data){
                console.log(data);
                if(data == "Error"){
                    alert('There was an error creating your account.');
                }else{
                    alert('Your account was create!');
                    window.location.replace('index.html');
                }
            },
            error: function(){
                console.log(data);
                alert('There was an error in the Database.');
            }
        });
    },
};
