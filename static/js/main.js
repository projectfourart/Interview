window.onload = function (){
	var elm = window.document.getElementsByTagName("select");
		for (var j = 0; j <= 31; j ++ ){
			var option = document.createElement('option')
			if (j == 0) option.innerHTML="--"
			else option.innerHTML = j;
			elm[0].appendChild(option)
		}
		array = ['Січень', 'Лютий', 'Березень', 'Квітень','Травень', 'Червень', 'Липень', 'Серпень','Вересень','Жовтень','Листопад','Грудень']
		for (var j = 0; j < array.length; j ++ ){
			var option = document.createElement('option')

			if (j == 0) option.innerHTML = "--"
			else option.innerHTML = array[j];

			elm[1].appendChild(option)
		}
		for (var j = 1980; j <= 1999; j ++ ){
			var option = document.createElement('option')
			if (j == 1980) option.innerHTML="--"
			else option.innerHTML = j;
			elm[2].appendChild(option)
		}
}
