(function(){
	var app = {
		init : function(){
			this.setUpListeners();	
		},
		setUpListeners : function (){
			$('form').on("submit", app.submitForm);
		},
		submitForm : function (data){
			data.preventDefault();
			var form = $(this);
			if (app.validataeForm(form)){
				$.ajax({
					url: '/',
					type: 'POST',
					data: app.getAllInputs(form)
				})
				 $(document).ready(function(){
				$("#myModalBox").modal('show');
				});
   				
				// $(location).attr('href',url);
			}
		},
		getAllInputs: function(form){
			var dump = form.find("input","select");
			array = new Object();
			$.each(dump,function(key, value){
				array[value.name] = value.value
			})
			// array['day'] = $("#day").value
			array['day'] = window.document.getElementById('day').selectedIndex
			array['mondey'] = window.document.getElementById('mondey').selectedIndex
			array['year'] = window.document.getElementById('year').selectedIndex

			// array['monday'] = $("#mondey").value
			// array['year'] = $("#year").value
			return array

		}
		,
		validataeForm: function(form){
			var inputs = form.find("input");
			valid = true;
			inputs.tooltip('destroy');

			$.each(inputs,function(index, val){
				var input = $(val);
				val = input.val();
				formGroup = input.parents('.form-group');
				label = formGroup.find('label').text().toLowerCase();
				textError = "Ведіть " + label;

				if (val.length === 0){
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
	}
	app.init();


}());

$(".finish").click(function(){
	var url = "/";
	window.location.href = url;
});