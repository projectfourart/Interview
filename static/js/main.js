(function(){
	var app = {
		init : function(){
			this.setUpListeners();	

		},
		setUpListeners : function (){
			if ($('#form_reg').length != 0){
				$('form').on("submit", app.submitForm );
			}
			else if ($('#form_auth').length != 0){
				 $('form').on("submit", app.validataeFormAuth)
				}

		},
		validataeFormAuth : function(data){
			data.preventDefault();
			var form = $(this)
			if (app.test(form)){
				// console.log("+")	
				data = {}
				var inputs = form.find("input");
				for (var i = 0; i < inputs.length; i++){
					data[inputs[i].name] =  inputs[i].value
				}
				
				$.ajax({
				  url: '/',
				  data: data,
				  type: "POST",
				  success: function(){
					 window.location.reload();
				  }
				});

			}


		},
		test :function(data){

			var inputs = data.find("input");
			valid = true;
			inputs.tooltip('destroy');


			$.each(inputs,function(index, val){
				var input = $(val);
				value = input.val();
				formGroup = input.parents('.form-group');
				label = formGroup.find('label').text().toLowerCase();
				textError = "Ведіть " + label;



				if (value.length === 0){
					formGroup.addClass('has-error').removeClass('has-success');
					input.tooltip({
						trigger: 'manual',
						placement: 'top',
						title: textError
					}).tooltip('show');

					valid = false;
				}else {
					formGroup.addClass('has-success').removeClass('has-error');
				}			
			});


			return valid;

		}
		,
		submitForm : function (data){
			data.preventDefault();
			form = $(this)
			data = {}
			if (app.validataeForm(form) == true){
				var inputs = form.find("input");
				for (var i = 0; i < inputs.length; i++){
					data[inputs[i].name] =  inputs[i].value
				}
				
				$.ajax({
				  url: '/',
				  data: data,
				  type: "POST",
				  success: function(){
					    $('#myModalBox').modal('show');
				  }
				});
			}
				
		},
		validataeForm: function(form){
			var inputs = form.find("input");
			valid = true;
			inputs.tooltip('destroy');


			$.each(inputs,function(index, val){
				var input = $(val);
				value = input.val();
				formGroup = input.parents('.form-group');
				label = formGroup.find('label').text().toLowerCase();
				textError = "Ведіть " + label;



				if (value.length === 0){
					formGroup.addClass('has-error').removeClass('has-success');
					input.tooltip({
						trigger: 'manual',
						placement: 'top',
						title: textError
					}).tooltip('show');

					valid = false;
				}else {
					formGroup.addClass('has-success').removeClass('has-error');
				}			
			});

			valid  = app.repeat_password(valid)

			return valid;
		}
		, repeat_password : function(valid){

			var password = $('[name=password]')[0];
			var password_two = $('[name=password_repeat]')[0];

			var group_one = $(password).parents('.form-group')
			var group_two = $(password_two).parents('.form-group')
			
			if ( password.value == password_two.value && valid == true ){
				$(group_one).addClass('has-success').removeClass('has-error');
				$(group_two).addClass('has-success').removeClass('has-error');
			}else {
				$(group_two).addClass('has-error').removeClass('has-success');
					$(password_two).tooltip({
						trigger: 'manual',
						placement: 'top',
						title: "Паролі не співпадають"
					}).tooltip('show');

					valid = false;
			}
			return valid
		}

	}
	app.init();
}());

$("#finish").click(function (){
	window.location = "/";
});

window.onload = function(){
	if (window.location.search == "?exit=True"){
		window.location.href = "/";
	}
};
