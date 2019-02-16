document.getElementById('meetup_form').addEventListener('submit', create_meetup);

function create_meetup(){
  /*
  Function to create a meetup
  */
  event.preventDefault();
  Url = `https://questioner-api-048.herokuapp.com/api/v2/meetups`;
  fetch(Url, {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Authorization' : 'Bearer ' + localStorage.getItem('token')
      },
      body: JSON.stringify({
        'title' : document.getElementById('title').value,
        'description' : document.getElementById('description').value,
        'date' : document.getElementById('date').value,
        'location' : document.getElementById('location').value
      })
  })

}

function openForm(fid) {
  document.getElementById(fid).style.display = "block";
}
