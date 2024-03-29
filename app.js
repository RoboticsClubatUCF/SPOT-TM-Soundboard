const sounds = ['Test'];

sounds.forEach((sounds) => {
    const btn = document.createElement('button');
    btn.classList.add('btn');

    btn.innerText = sounds;
    btn.addEventListener('click', ()=>{
        // if you want the previous sound to play before the next one is played
        // stopSongs();
        // what happens when the button is pressed - needs to be changed
        document.getElementById(sounds).play();
    })

    document.getElementById('buttons').appendChild(btn);
})

function stopSongs(){
    sounds.forEach((sounds) => {
        const song = document.getElementById(sounds);

        song.pause();
        song.currentTime = 0;
    });
}