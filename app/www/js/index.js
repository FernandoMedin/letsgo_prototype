var app = {
    meController: function($scope){
        $scope.name = function(){ return localStorage.name; }
        $scope.last_name = function(){ return localStorage.last_name; }
        $scope.email = function(){ return localStorage.email; }
        $scope.fullname = function(){ return localStorage.name + " " + localStorage.last_name; }
    },
};

var login = {
    auth: function(){
        $('form').submit(function(){
            var landmarkID = $(this).parent().attr('data-landmark-id');
            var postData = $(this).serialize();

            $.ajax({
                type: 'POST',
                data: postData+'&amp;lid='+landmarkID,
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
        return false;
        });
    },

    create: function(){
        $('form').submit(function(){
            var landmarkID = $(this).parent().attr('data-landmark-id');
            var postData = $(this).serialize();

            $.ajax({
                type: 'POST',
                data: postData+'&amp;lid='+landmarkID,
                url: 'http://localhost:8000/new_user/',
                success: function(data){
                    console.log(data);
                    if(data == "Error"){
                        alert('There was an error creating your account.');
                    }else{
                        alert('Your login was successfully created');
                        window.location.replace('index.html');
                    }
                },
                error: function(){
                    console.log(data);
                    alert('There was an error creating your login');
                }
            });
        return false;
        });
    }
};

var events = {
    create: function(){
        $('form').submit(function(){
            var landmarkID = $(this).parent().attr('data-landmark-id');
            var postData = $(this).serialize();

            $.ajax({
                type: 'POST',
                data: postData+'&amp;lid='+landmarkID,
                url: 'http://localhost:8000/new_event/',
                success: function(data){
                    console.log(data);
                    if(data == "Error"){
                        alert('Error');
                    }else{
                        alert("Your event was created!");
                        window.location.replace('main.html');
                    }
                },
                error: function(){
                    console.log(data);
                    alert('Database Error');
                }
            });
        return false;
        });
    }
};
