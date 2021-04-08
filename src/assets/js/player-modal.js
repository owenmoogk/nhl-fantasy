function showPlayerStats(){
    statsDiv = document.getElementById('all-stats')

    if (statsDiv.style.display == 'block'){
        statsDiv.style.display = "none"
    }
    else{
        statsDiv.style.display = 'block'
    }
}