function submitFunction() {
	const barriers_check = document.querySelectorAll('.barriers:checked');
	const exercise_check = document.querySelectorAll('.exercise:checked');
	const prevents_check = document.querySelectorAll('.prevents:checked');
	const motivation_check = document.querySelectorAll('.motivation:checked');	
	
	if (barriers_check.length == 0) {
		document.getElementById("b_1").required = true;
		document.getElementById("b_1").setCustomValidity('Please select at least one of these options.');
	}
	else {
		document.getElementById("b_1").required = false;
		document.getElementById("b_1").setCustomValidity('');
	}
	
	if (exercise_check.length == 0) {
		document.getElementById("e_1").required = true;
		document.getElementById("e_1").setCustomValidity('Please select at least one of these options.');
	}
	else {
		document.getElementById("e_1").required = false;
		document.getElementById("e_1").setCustomValidity('');
	}

	if (prevents_check.length == 0) {
		document.getElementById("pb_1").required = true;
		document.getElementById("pb_1").setCustomValidity('Please select at least one of these options.');
	}
	else {
		document.getElementById("pb_1").required = false;
		document.getElementById("pb_1").setCustomValidity('');
	}
	
	if (motivation_check.length == 0) {
		document.getElementById("m_1").required = true;
		document.getElementById("m_1").setCustomValidity('Please select at least one of these options.');
	}
	else {
		document.getElementById("m_1").required = false;
		document.getElementById("m_1").setCustomValidity('');
		document.getElementById("m_1").setCustomValidity('');
		document.getElementById("m_1").setCustomValidity('');
	}
}
	
function clearFunction(){
	var result = confirm("This will remove your answers from all questions, and cannot be undone.");
	if(result){
		document.getElementById("myform").reset();
	}
}