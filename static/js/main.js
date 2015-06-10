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

(function(){
	app = {
		init : function(){
			app.setUpListeners();
		},
		setUpListeners : function(){
			$("#add_quation").on("click", app.eventClickAdd)
			$("#clear_btn").on("click", app.clear)
			$('#loading-example-btn').on("click", app.load)
			$("#reset").on("click", app.reset)
			$("#btn-save-interview").on("click", app.save_interview)
			$('#btn-save-change').on('click', app.save_change)
		},
		save_change : function (){
			// console.log(app.selected)
			var original = app.selected;
			var chenges = []
			$.each($('.type_user'),function(i,v){
				// chenges.push(v.dataset.name)
				// console.log(v.selectedIndex)
				if (v.selectedIndex == 0)
					chenges.push("user")
				else if (v.selectedIndex == 1)
					chenges.push('admin')
				else if (v.selectedIndex == 2)
					chenges.push('interviewer')
			});
			// console.log(original)
			// console.log(chenges)
			var new_array = {}
			new_array['btn-save-changes'] = 'true'
			var j = 0
			for (var i = 0; i < original.length ;i++) {
				if (chenges[i] != original[i]){
					new_array[i+1] = chenges[i]
					j ++;
				}
			};
			// console.log(new_array.length)
				if (j != 0){
					$.ajax({
					  url: '/',
					  data: new_array,
					  type: "POST",
					  success: function(){
							 window.location.reload();
					  }
					});
		
				}
						
			}
		,
		reset : function(){
			window.location.href = "/"
		},
		save_interview : function (){
			var list = $("#list-group-interview")
			var inputs = list.find('li')
			// console.log(inputs[0])
			var array = {}
			// console.log(inputs)
			$.each(inputs, function(i, v){
				console.log(v)
				if (v.children[1].value == "--"){
					array[v.children[0].innerHTML] = ""
				}else
					array[v.children[0].innerHTML] = v.children[1].value
			});

			array['send-new-interview']	= 'ok'
			$.ajax({
				  url: '/',
				  data: array,
				  type: "POST",
				  success: function(){
					    // $('#myModalBox').modal('show');
					    app.reset();
				  }
				});
		}
		,
		load : function (){

			    var btn = $(this)
			    btn.button('loading')

				var question = ""
			    var all_question = app.getAllQuestion(".form-control")
			    var active_question = app.getActiveInputs()
			    for (var i =0 ; i < all_question[0].length; i++){
				// console.log(active[i])
						if (active_question[i] == true){
							question += ""+String(i+1)+" : "
						}
				}

				var reg = /\/profile\/(\d+)/ig
				var id_user = reg.exec(window.location.href)[1]
			    $.ajax({
			    	method: "POST",
			    	data: "id="+String(id_user)+"&data="+String(question)+"",
			    	url: "/",
			    }).done(function () {
			      window.setTimeout(function(){

			      	$('#Modal').modal('show')
				    btn.button('reset')
			      },2000);
			    });

		},

		clear : function(){
			window.location.reload()
		}
		,
		eventClickAdd : function(){
			var all_question = app.getAllQuestion(".form-control")
			var active_question = app.getActiveInputs()
			app.generateQuesition(all_question, active_question)

		},
		generateQuesition : function (all, active){
			var elm = $('#list_select_quation')
			elm.append()
			for (var i =0 ; i < all[0].length; i++){
				// console.log(active[i])
				if (active[i] == true){
					elm.append("<li class='list-group-item'> <div class='input-group'> <span > "+all[0][i]+" </span> <span style='float:right;'>"+all[1][i]+"</span></div></li>")
				}
			}
		}
		,
		getActiveInputs : function (){
			var list = $("#list-group")
			var inputs = list.find('input')
			array_result = []
			$.each(inputs, function(index, value){
				if (value.checked == true){
					array_result.push(true)
				}
				else{
					array_result.push(false)
				}

			});	
			return array_result
		},
		getAllQuestion : function (class_name){
			var lists = $(class_name);
			var bals = $(".bals");
			var question = []
			var bals_list = []
			$.each(lists, function(index, value){
				question.push(value.firstChild.data)

			});

			$.each(bals, function(index, value){
				bals_list.push(value.firstChild.nodeValue)

			});
			
			return [question, bals_list]
		},

	};
	app.init();
}());

window.onload = function (){

	if ((/^\?\.*/.test(window.location.search) )){
		window.location.href = "/";
	}
	
	var bals = $('.bal');
	sum = 0
	$.each(bals, function(i,v){
		// array.push(v.textContent)
		sum += Number(v.textContent)
	});
	// $('#result').innerHTML = sum;
	if ($("#result")[0]){
		$('#result')[0].innerHTML  = sum.toFixed(1)
	}

	app.selected = function(){
		// this.selectedIndex = index;
		// console.log(index)
		array = []
		var selected = $('.type_user');
		$.each(selected, function(index, value){
			// console.log(value.dataset.name)
			array.push( value.dataset.name )
			if (value.dataset.name == "user")
				value.selectedIndex = 0
			else if (value.dataset.name == "interviewer")
				value.selectedIndex = 2
			else if (value.dataset.name == "admin")
				value.selectedIndex = 1
		});
		return array
	}()
};

function confirmDelete(id) {
	value =  confirm("Ви підтверджуєте видалення?");
	if (value) 
		window.location.href="?drop_sourse="+String(id)
}
