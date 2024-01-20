document.querySelectorAll(".add-song").forEach(button => {
    button.addEventListener("click", addSong);
  });
  
  function addSong(event) {
    const row = document.createElement('tr');
    const songTitle = document.createElement('td');
    songTitle.textContent = event.target.parentNode.parentNode.parentNode.parentNode.querySelectorAll('.in-song-table')[0].innerText;
    row.appendChild(songTitle);
  
    const artistName = document.createElement('td');
    artistName.textContent = artistName.value;
    row.appendChild(artistName);
  
    const addButton = document.createElement('td');
    const button = document.createElement('button');
    button.textContent = 'Add to Playlist';
    button.addEventListener('click', () => {
      const playlist = document.querySelector('#playlist');
      if (playlist) {
        playlist.appendChild(row);
      }
    });
    addButton.appendChild(button);
    row.appendChild(addButton);
  
    fetch('/add_song', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        'song_name': event.target.parentNode.parentNode.parentNode.parentNode.querySelectorAll('.in-song-table')[0].innerText,
        'duration': event.target.parentNode.parentNode.querySelectorAll('td')[0].innerText,
      })
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
  
    const table = document.querySelector('#songs-table');
    if (table) {
      table.appendChild(row);
    }
  }