
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$(document).ready(function() {

    $("li").click(function( event ) {
	var id  = $(this).attr('value');
	$.ajax({
	    type: "DELETE",

	    //this is ugly and should be changed.
	    url: $("h2")[0].textContent + "/" + id.toString(),

	    beforeSend: function(xhr, settings) {
		var csrftoken = getCookie('csrftoken');

	    	if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
	    	    xhr.setRequestHeader("X-CSRFToken", csrftoken);
	    	}
	    },

	    success: function(data){
		$(this).remove();
	    },
	});

	$(this).remove();
	$("#id_name").focus();
	event.preventDefault();
    });
});

$("#id_name").focus();
