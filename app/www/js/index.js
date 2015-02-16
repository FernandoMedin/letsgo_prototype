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
                        var name = data.replace(/\"/g, '');
                        localStorage.name = name;
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
                url: 'http://localhost:8000/debug/',
                success: function(data){
                    console.log(data);
                    if(data == "Error"){
                        alert('Error');
                    }else{
                        alert('Hell Yeah!');
                        window.location.replace('index.html');
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
