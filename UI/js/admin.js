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
  .then(response => response.json())
  .then(data => {
    if (data.status === 201) {
      window.alert('meetup created successfully!');
    }
    else{
      window.alert(data);
    }
  })

}

function openForm(fid) {
  document.getElementById(fid).style.display = "block";
}

function closeForm(fid){
  document.getElementById(fid).style.display = "none";
}

function get_meetups(){
  let Url = 'https://questioner-api-048.herokuapp.com/api/v2/meetups/upcoming';

  fetch(Url, {
    method: "get",
    header: {
      "Content-Type": "application/json"
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 200) {
      console.log('successful', data.status)
      let meetup_container = document.getElementById('meetup_container');
      let meetup_data = data.data;
      meetup_data = meetup_data.slice(0, 6)
      return meetup_data.map(function(meetup_record) {
        let meetup = createNode('div');
        meetup.classList.add('meetups')
        let date = createNode('p');
        let delete_meetup = createNode('button');
        delete_meetup.classList.add('delbtn');
        delete_meetup.setAttribute('type', 'button');
        let meetupid = meetup_record.json_build_object.meetupid;
        delete_meetup.addEventListener("click", function meetups(){delete_meetup_record(meetupid);});
        let title = createNode('h4');
        let description = createNode('p');
        let venue = createNode('venue');
        delete_meetup.innerHTML = `delete`;
        date.innerHTML = `Date: ${meetup_record.json_build_object.date}`;
        title.innerHTML = `Title: ${meetup_record.json_build_object.title}`;
        description.innerHTML = `Description: ${meetup_record.json_build_object.description}`;
        venue.innerHTML = `Venue: ${meetup_record.json_build_object.vanue}`;
        append(date, delete_meetup);
        append(meetup, date);
        append(meetup, title);
        append(meetup, description);
        append(meetup, venue);
        append(meetup_container, meetup);
    })
  }
    else{
      console.log(data.message);
    }

})
    .catch((err)=>console.log(err));
  }

function delete_meetup_record(meetupid){
  /*
  Function to delete a meetup
  */
  event.preventDefault();
  Url = `https://questioner-api-048.herokuapp.com/api/v2/meetups/${meetupid}`;
  fetch(Url, {
    method: "DELETE",
    headers: {
      'Content-Type': 'application/json',
      'Authorization' : 'Bearer ' + localStorage.getItem('token')
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.status === 200){
      window.alert('meetup delete succssfully');
      window.location.href = './admin.html';
    }
  });
}

  function createNode(element) {
      return document.createElement(element);
  }

  function append(parent, el) {
    return parent.appendChild(el);
  }
