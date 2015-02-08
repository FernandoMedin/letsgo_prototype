var main = {
    get_name: function(){
        var url = window.location.href;
        var query_string = url.split("?");
        var param_item = query_string[1].split("=");
        var name = param_item[1];

        return name;
    },

    show_name: function(){
        var str = document.getElementById("name").innerHTML;
        var name = this.get_name();
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
                url: 'http://localhost/lets_request/login.php',
                success: function(data){
                    console.log(data);
                    alert('Now you are loged! Enjoy it!');
                    var name = data.replace(/\"/g, '');
                    window.location.replace('main.html?name=' + name);
                },
                error: function(){
                    alert('Incorrect email or password.');
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
                url: 'http://localhost/lets_request/signup.php',
                success: function(data){
                    console.log(data);
                    alert('Your login was successfully created');
                    window.location.replace('index.html');
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

