const btn = document.getElementById('button')

btn.addEventListener('click', () => {
    // AJAX Call
    const xhr = new XMLHttpRequest()
    const url = `https://api.themoviedb.org/3/search/movie?api_key=473ce42b7b92f1fcd1bb5f06b4217fdb&query=`
    
    const movieName = document.getElementById('search').value

    const newURL = `${url}${movieName}`

    xhr.open('GET', newURL)

    xhr.onreadystatechange = () => {
        if(xhr.status === 200 && xhr.readyState === 4) {
            const response = JSON.parse(xhr.responseText)
            console.log(response)

            let output = ``

            for(let i=0; i < response.results.length; i++) {
                const image = `<img style="margin: 10px; border: 2px solid black; padding: 5px;" src="https://image.tmdb.org/t/p/w500/${response.results[i].poster_path}" >`
                output += ` ${image} <br /> <br /> <b> <u> ${response.results[i].title} </u> </b>
                 <small> Relaesed in ${response.results[i].release_date} </small><br/><br/>
                 <b>  Overview: ${response.results[i].overview}  </b> <br/><br/>
                 <b>  Vote Count: ${response.results[i].vote_count}  </b><br/><br/> 
                 <b>  Average Of Vote: ${response.results[i].vote_average}  </b> <br /> <br /> <hr /> <hr />`
            }

            const container = document.getElementById('main-div')
            container.innerHTML = output
         }
    }

    xhr.send()
})