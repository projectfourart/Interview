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
			if ( window.document.getElementById('day') != null && 
				 window.document.getElementById('mondey') != null &&
				  window.document.getElementById('year') != null
				){

				array['day'] = window.document.getElementById('day').selectedIndex
				array['mondey'] = window.document.getElementById('mondey').selectedIndex
				array['year'] = window.document.getElementById('year').selectedIndex	

				dump = window.document.getElementsByName("role");
				for (var i = 0; i < dump.length; i++){
					if (dump[i].checked == true){
						role = dump[i].defaultValue;
					}
				}
				console.log(role)
				array['role']	= role;

			}

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

(function(){
	app = {
		init : function(){
			app.setUpListeners()
		},
		setUpListeners : function (){
			$('#add_quation').on("click", app.add_quation);
			$("#clear_btn").on("click", app.clear);
			$("#loading-example-btn").on("click", app.save);
			$("#reset").on('click',app.reset);

		},
		reset : function(){
			window.location.reload()
		},

		save : function (){
			    var btn = $(this)
			    btn.button('loading')
				var list = app.get_active_quation();
				var all_elm = app.get_all_quation() // get all
				var result = app.get_active_quation()	// get ACITVE elm
				var question = ""
			    
			    window.setTimeout(function(){
				    btn.button('reset')
					for (var i = 0 ; i < result.length; i ++){
						if (result[i] == true){
							question += ""+String(i+1)+" : "
						}
					}
					var reg = /\/profile\/(\d+)/ig
					var id_user = reg.exec(window.location.href)[1]
					// console.log(id_user)
					// console.log(question)


				     $.ajax({
					   type: "POST",
					   url: "/",
					   data: "id="+String(id_user)+"&data="+String(question)+""
					 });
				    
				    $("#Modal").modal('show')
			    },500)

			// var right_quation = $("#list_select_quation")
			


				// console.log()
			    
		},

		clear : function(){
				var right_quation = $("#list_select_quation")	
				var list_quation = $('#list_quation');
				var inputs = list_quation.find("input");
				var li = right_quation.find("li");
				li.remove();
				$.each(inputs,function(index, value){
					value.checked = false
				})


			}
		,
		add_quation : function (){
			var all_elm = app.get_all_quation() // get all
			var result = app.get_active_quation()	// get ACITVE elm
			var right_quation = $("#list_select_quation")

			for (var i = 0 ; i < result.length; i ++){
				if (result[i] == true){
					right_quation.append("<li class='list-group-item'>"+ all_elm[i] +"</li>")
				}
			}
			// ....
		}, 
		get_all_quation : function (){
			var list_quation = $('#list_quation');
			var inputs = list_quation.find("input");
			var result = []
			$.each(inputs,function(index, value){
				input = $(value)
				InputGroup = input.parents('.input-group');
				span_text = InputGroup.find('span').text().toLowerCase();
				result.push(span_text)
				})
			return result
		},
		get_active_quation : function (){
			var list_quation = $('#list_quation');
			var inputs = list_quation.find("input");
			var result = []
			$.each(inputs,function(index, value){
				result.push(value.checked)
				})
			return result
		},

	}


	app.init();	
}());
