const inputTxt = document.getElementById('inputTxt');
const searchBtn = document.getElementById('searchBtn');
var weatherSection = document.querySelector('section.flexbox');

inputTxt.addEventListener('keypress', eventPara => {
    if (eventPara.key == 'Enter' && inputTxt.value != '') {
        mainLogic();
    }
});

searchBtn.addEventListener('click', eventPara => {
    eventPara.preventDefault();
    mainLogic();
});

const mainLogic = () => {
    weatherSection.style.display = 'flex';
    let cityName = inputTxt.value;
    const APIKEY = '57be3d870d8df9e19244ba0b281f7b51';
    const Http = new XMLHttpRequest();
    let url = `https://api.openweathermap.org/data/2.5/weather?units=metric&lang=en&q=${cityName}&appid=${APIKEY}`;
    Http.open('GET', url);
    Http.send();
    Http.onreadystatechange = () => {
        if (Http.readyState === 4 && Http.status === 200) {
            const response = JSON.parse(Http.responseText);
            let heading1Element = document.querySelector('section h1');
            let imgElement = document.querySelector('section img');
            let pElement = document.querySelector('section p');
            let locationElement = document.getElementById('location');
            let feelsLikeElement = document.querySelector('.feels-like');
            let humidityElement = document.querySelector('.humidity');
            let city = response.name;
            let country = response.sys.country;
            if (country == "IN") {
                country = "India";
            }
            let description = response.weather[0].description;
            let weatherCondition = response.weather[0].main.toLowerCase();
            let img = document.createElement('img');
            if (weatherCondition == "clear") {
                img.setAttribute('src', 'images/clear.svg');
            }
            else if (weatherCondition == "cloud") {
                img.setAttribute('src', 'images/cloud.svg');
            }
            else if (weatherCondition == "haze") {
                img.setAttribute('src', 'images/haze.svg');
            }
            else if (weatherCondition == "rain") {
                img.setAttribute('src', 'images/rain.svg');
            }
            else if (weatherCondition == "snow") {
                img.setAttribute('src', 'images/snow.svg');
            }
            else {
                img.setAttribute('src', 'images/storm.svg');
            }
            let humidity = response.main.humidity;
            let tempInC = response.main.temp;
            let feelsLike = response.main.feels_like;
            heading1Element.innerHTML = `${tempInC} °C`
            imgElement.setAttribute('src', img.src);
            pElement.innerHTML = `${description}`;
            locationElement.innerHTML = `<i class='bx bx-map'></i><span>${city}, ${country}</span>`;
            feelsLikeElement.innerHTML = `<i class='bx bxs-thermometer'></i>${feelsLike}°C Feels Like`;
            humidityElement.innerHTML = `<i class='bx bxs-droplet-half'></i>${humidity}% Humidity`;
            let i = document.querySelectorAll('i');
            i.forEach(element => {
                element.className += ' margin-right';
            });
            console.log(everyThing);
        }
    }
};