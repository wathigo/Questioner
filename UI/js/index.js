
function signUpUser(event) {
    /*
    Function to perform user signup
    */

    let data = {};
    let fieldnames = [
      'firstname',
      'lastname',
      'othername',
      'email',
      'phonenumber',
      'password',
      'repeatpassword'
    ];
    let signupUrl = 'http://0.0.0.0:5000/api/v2/auth/admin/signup';

    for (let name of fieldnames) {
            data[name] = document.getElementById(name).value;
        }

    fetch(signupUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: data
    })
        .then((response) => response.json())
        .then((data => {
            if (data.status === 201){
                console.log('Success:', JSON.stringify(data));
            }
            else{
                console.log(data.message);
            }
        }))
}
