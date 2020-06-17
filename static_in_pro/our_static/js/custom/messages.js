function displayFlashMessage(message) {
	var template = "<div class='container container-alert-flash'>" + 
	"<div class='col-sm-8'> " + 
	"<div class='alert alert-success alert-dismissible' role='alert'>" + 
	"<button type='button' class='close' data-dismiss='alert' aria-label='Close'>" +
	"<span aria-hidden='true'>&times;</span></button>" 
	+ message + "</div></div></div>"
	$("body").append(template);
	$(".container-alert-flash").fadeIn();
	setTimeout(function(){ 
		$(".container-alert-flash").fadeOut();
	}, 1800);
}

function displayAlertMessage(title, content) {
	$.alert({
            title: title,
            content: content,
            theme: "supervan",
          })
	}

// Displaying a spinner upon forms submission
function displaySpinner(submitBtn, defaultText, spinText, doSubmit){
      if (doSubmit){
        submitBtn.addClass("disabled")
        submitBtn.html("<i class='fa fa-spin fa-spinner'></i> " + spinText + "")
      } else {
        submitBtn.removeClass("disabled")
        submitBtn.html(defaultText)
      }
      
    }





   