var main = {
    get_name: function(){
        return localStorage.name;
    },

    show_name: function(){
        var str = document.getElementById("name").innerHTML;
        var name = this.get_name();
        console.log(name);
        var res = str.replace("nameID", name);

        document.getElementById("name").innerHTML = res;
    },

    show_user: function(){
        document.getElementById("name").innerHTML = localStorage.name;
        document.getElementById("last_name").innerHTML = localStorage.last_name;
        document.getElementById("email").innerHTML = localStorage.email;
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

var data = {
    get_user: function(){
        $.ajax({
            type: 'POST',
            data: 'id_user=' + localStorage.id_user + '&passwd=' + localStorage.passwd,
            url: 'http://localhost:8000/get_user_data/',
            success: function(data){
                console.log(data);
                if(data == "Error"){
                    alert('Error');
                    localStorage.clear();
                    window.location.replace('index.html');
                }else{
                    alert("We found your data!");
                }
            },
            error: function(){
                console.log(data);
                alert('Database Error');
            }
        });
    return false;
    }
};
