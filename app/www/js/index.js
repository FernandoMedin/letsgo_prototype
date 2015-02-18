var main = {
    get_name: function(){
        return localStorage.id_user;
    },

    show_name: function(){
        var str = document.getElementById("name").innerHTML;
        var name = this.get_name();
        console.log(name);
        var res = str.replace("nameID", name);

        document.getElementById("name").innerHTML = res;
    },

    get_user_data: function(){
        $('form').submit(function(){
            var landmarkID = $(this).parent().attr('data-landmark-id');
            var postData = $(this).serialize();

            $.ajax({
                type: 'POST',
                data: postData+'&amp;lid='+landmarkID,
                url: 'http://localhost:8000/test/',
                success: function(data){
                    console.log(data);
                    if(data == "Error"){
                        alert('Fucking Error!!');
                    }else{
                        alert(data);
                        var id_user = data.replace(/\"/g, '');
                    }
                },
                error: function(){
                    console.log(data);
                    alert('There was an error in the Database.');
                }
            });
        return false;
        });
    }
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
                        var id_user = data.replace(/\"/g, '');
                        localStorage.id_user = id_user;
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
