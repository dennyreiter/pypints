function csrfSafeMethod(method) {
    // These HTTP methods don't require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var getCookie = function (cookie) {
        var cookieValue = null;
 
        try {
            cookieValue = document.cookie.split(';')
                .map(function (x) {
                    return x.trim().split('=');
                })
                .filter(function (x) {
                    return x[0] == cookie;
                })
                .map(function (x) {
                    return x[1];
                })[0];
        } catch (e) {
            console.error(e);
        }
        return cookieValue;
};

$.ajaxSetup({
    crossDomain: false, // Obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            var csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

