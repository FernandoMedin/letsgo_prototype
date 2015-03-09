function get_pic(){
    navigator.camera.getPicture(onSuccess, onFail, { quality: 50,
        destinationType: Camera.DestinationType.DATA_URL,
        sourceType: navigator.camera.PictureSourceType.PHOTOLIBRARY
    });
}

function onSuccess(imageData) {
    var image = document.getElementById('myImage');
    image.src = "data:image/jpeg;base64," + imageData;
}

function onFail(message) {
    alert('Failed because: ' + message);
}

var event_data = {
    validate: function(){
        var id_user = localStorage.id_user;
        var name = document.getElementById("name").value;
        var local = document.getElementById("location").value;
        var date = document.getElementById("event_date").value;
        var begin = document.getElementById("event_begin").value;
        var end = document.getElementById("event_end").value;
        var event_type = document.getElementById("event_type").value;
        var event_category = document.getElementById("event_category").value;
        var description = document.getElementById("description").value;

        if(!id_user){
            alert("You are offline. Please, login with your account.");
            location.href="index.html";
        }else if(!name){
            alert("Please, write an event name.");
        }else if(!local){
            alert("Please, write the location of your event.");
        }else if(!date){
            alert("Please, choose an event date,.");
        }else if(!begin){
            alert("Please, select a begin event time.");
        }else if(!end){
            alert("Please, select an end event time.");
        }else if(!event_type){
            alert("Please, select an event type.");
        }else if(!event_category){
            alert("Please, select an event category");
        }else{
            this.create_event(id_user, name, local, date, begin, end, event_type, event_category, description);
        }
    },

    create_event: function(id, name, local, date, begin, end, type, category, desc){
        $.ajax({
            type: 'POST',
            data: 'id_user=' + id + '&event_name=' + name + '&location=' + local + '&event_date=' + date + '&begin=' + begin + '&end=' + end + '&event_type=' + type + '&event_category=' + category + '&description=' + desc,
            url: 'http://localhost:8000/new_event/',
            success: function(data){
                console.log(data);
                if(data == "Error"){
                    alert('There was an error creating your event.');
                }else{
                    alert('Event created!');
                    location.href="main.html"
                }
            },
            error: function(){
                console.log(data);
                alert('There was an error in the Database.');
            }
        });
    },
}

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
