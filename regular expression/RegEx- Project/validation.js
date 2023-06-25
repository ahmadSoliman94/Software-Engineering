const ipattern = document.querySelectorAll('input');

// Define your Regular Expression pattern for each fields of the form
const forms = {
    fname: /^[A-Za-z]*$/, // First names usually consist just of alphabetic characters.
    lname: /^[A-Za-z]*$/, // Last names usually consist of alphabetic characters.
    username: /^[a-zA-Z0-9_.-]{3,20}$/, // matches any alphanumeric character, underscore and specifies the minimum and maximum length of the username
    password: /^[A-Za-z\d_\.]{4,11}$/, // matches any alphanumeric character, underscore and specifies the minimum and maximum length of the password
    email: /^$/,
    mobile: /^\+963\d{9}$/
};


// Function to validate each fields in the form
function isValidForm(label, regexp){

    //mark the field name as valid
	if(regexp.test(label.value)){
        label.className = 'valid';
    } else {
		//mark the field name as invalid
        label.className = 'invalid';
    }

}

// Add EvenListener to each input fields
ipattern.forEach((input) => {
    input.addEventListener('keyup', (e) => {
            isValidForm(e.target, forms[e.target.attributes.name.value]);
    });
});
